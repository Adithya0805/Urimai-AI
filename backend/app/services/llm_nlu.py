"""LLM NLU Service — Gemini fallback for Tamil field extraction.

This module is called ONLY when the primary regex-based extractors in
tamil_nlu.py cannot parse a user's input. It sends a tightly constrained
prompt to Gemini so the model maps free Tamil text to a specific enum value.

Critical constraint: This module NEVER receives or returns eligibility results.
Its only job is: Tamil text → one structured field value.
"""
from __future__ import annotations

import logging
from typing import List, Optional, Tuple
from app.config import get_settings

logger = logging.getLogger(__name__)


# ── Enum-to-Tamil hint map (helps the prompt be more accurate) ─────────────────
_FIELD_HINTS: dict[str, str] = {
    "composition_type": "single, couple, nuclear, joint",
    "ration_card_type": "none, green, white, khaki, phh_aay, orange, yellow, other",
    "gender": "male, female, transgender, other",
    "education_level": "none, primary, secondary, higher_secondary, graduate, postgraduate, dropout",
    "occupation": "farmer, daily_wage, self_employed, govt_employee, private_employee, unemployed, student, homemaker, retired, other",
    "marital_status": "single, married, widowed, divorced",
    "caste_category": "SC, ST, BC, MBC, DNC, General",
}


def _build_nlu_prompt(raw_text: str, field_name: str, valid_values: List[str]) -> str:
    """Constructs a tight, zero-shot prompt for Gemini NLU extraction."""
    values_str = ", ".join(valid_values)
    return (
        f"You are a Tamil language intake assistant for a Tamil Nadu government welfare scheme platform.\n"
        f"Your only task is to extract the value of the field '{field_name}' from the user's Tamil input.\n\n"
        f"User input: \"{raw_text}\"\n\n"
        f"Valid values for '{field_name}': {values_str}\n\n"
        f"Instructions:\n"
        f"- Reply with EXACTLY ONE value from the valid values list above.\n"
        f"- Do NOT explain. Do NOT add punctuation. Just the value.\n"
        f"- If you cannot extract a clear match, reply with: not_understood\n\n"
        f"Your answer:"
    )


def gemini_extract_field(
    raw_text: str,
    field_name: str,
    valid_values: List[str],
    db=None,
    session_id: Optional[str] = None,
) -> Tuple[Optional[str], bool, Optional[str]]:
    """Calls Gemini to extract a structured field value from Tamil free text.

    This is the LLM fallback called only when regex NLU fails.

    Args:
        raw_text:     The raw Tamil user input.
        field_name:   The field being extracted (e.g. "composition_type").
        valid_values: The allowed enum values. Gemini must pick one of these.
        db:           SQLAlchemy session (for logging). Optional.
        session_id:   Intake session ID (for logging). Optional.

    Returns:
        (extracted_value, is_valid, clarification_message)
        - If Gemini returns a valid enum value: (value, True, None)
        - If Gemini returns "not_understood" or an invalid value:
          (None, False, clarification_message)
    """
    settings = get_settings()

    if not settings.llm_available:
        return None, False, None

    try:
        from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
        from langchain_core.messages import HumanMessage  # type: ignore

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.0,  # Deterministic extraction
            max_tokens=20,    # We need only a short enum value
        )

        prompt_text = _build_nlu_prompt(raw_text, field_name, valid_values)
        response = llm.invoke([HumanMessage(content=prompt_text)])
        llm_output = response.content.strip().lower().strip(".")

        # Normalise: compare lowercased
        valid_lower = {v.lower(): v for v in valid_values}

        if llm_output in valid_lower:
            extracted = valid_lower[llm_output]
            _log_nlu_call(db, session_id, field_name, prompt_text, None, 0.0, llm_output)
            return extracted, True, None

        if "not_understood" in llm_output:
            _log_nlu_call(db, session_id, field_name, prompt_text, None, 0.0, llm_output)
            return None, False, _build_clarification(field_name, valid_values)

        # Gemini returned something unexpected — treat as not understood
        logger.warning(
            "Gemini NLU returned unexpected value '%s' for field '%s'. Input: '%s'",
            llm_output, field_name, raw_text,
        )
        _log_nlu_call(db, session_id, field_name, prompt_text, None, 0.0, llm_output)
        return None, False, _build_clarification(field_name, valid_values)

    except Exception as exc:
        logger.error("Gemini NLU call failed for field '%s': %s", field_name, exc)
        return None, False, None


def _build_clarification(field_name: str, valid_values: List[str]) -> str:
    """Builds a Tamil clarification message listing valid choices."""
    values_str = ", ".join(valid_values[:8])  # Cap at 8 for readability
    return (
        f"தயவுசெய்து '{field_name}' விவரத்தை தெளிவாக குறிப்பிடவும். "
        f"ஏற்றுக்கொள்ளக்கூடிய மதிப்புகள்: {values_str}."
    )


def _log_nlu_call(
    db,
    session_id: Optional[str],
    field_name: str,
    prompt_text: str,
    retrieved_context: Optional[str],
    retrieval_score: float,
    llm_output: str,
) -> None:
    """Persist the LLM call to LlmCallLog. Silently ignores errors."""
    if db is None:
        return
    try:
        from app.models.llm_call_log import LlmCallLog
        entry = LlmCallLog(
            call_type="nlu_extraction",
            session_id=session_id,
            scheme_code=field_name,  # Reuse scheme_code col to log which field was extracted
            prompt_text=prompt_text,
            retrieved_context=retrieved_context,
            retrieval_score=retrieval_score if retrieval_score else None,
            used_rag=False,
            llm_output=llm_output,
        )
        db.add(entry)
        db.commit()
    except Exception as exc:
        logger.error("Failed to log NLU call: %s", exc)
