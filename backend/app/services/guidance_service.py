import logging
from datetime import date
from typing import List, Tuple, Dict, Optional
from uuid import UUID
from app.config import get_settings
from app.models.enums import ApplicationMode, RuleOperator
from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme
from app.schemas.eligibility import FailedRuleDetail
from app.schemas.guidance import (
    EligibleSchemeGuidance,
    PartiallyEligibleSchemeGuidance,
    PersonGuidanceResponse,
    FamilyGuidanceResponse,
)
from app.services.matching_engine import evaluate_person_eligibility, evaluate_family_eligibility

logger = logging.getLogger(__name__)

# 180 days (approx. 6 months) staleness threshold
STALENESS_DAYS_THRESHOLD = 180
STALE_DISCLAIMER_TAMIL = (
    "இந்த தகவல் கடைசியாக சரிபார்க்கப்பட்டு 6 மாதங்களுக்கு மேல் ஆகிறது. "
    "அதிகாரப்பூர்வ தளத்தை சரிபார்க்கவும்."
)

GENDER_TAMIL = {
    "female": "பெண்கள்",
    "male": "ஆண்கள்",
    "transgender": "மூன்றாம் பாலினத்தவர்",
}

MARITAL_STATUS_TAMIL = {
    "unmarried": "திருமணமாகாதவர்",
    "married": "திருமணமானவர்",
    "widow": "விதவை",
    "destitute_widow": "ஆதரவற்ற விதவை",
    "deserted": "கணவனால் கைவிடப்பட்டவர்",
    "divorced": "விவாகரத்து பெற்றவர்",
}

CASTE_TAMIL = {
    "sc": "பட்டியலினம் (SC)",
    "st": "பழங்குடியினர் (ST)",
    "bc": "பிற்படுத்தப்பட்டோர் (BC)",
    "mbc": "மிகவும் பிற்படுத்தப்பட்டோர் (MBC)",
    "general": "பொதுப்பிரிவு (General)",
}

EDUCATION_TAMIL = {
    "none": "படிப்பறிவில்லை",
    "primary": "தொடக்கக் கல்வி (1-5)",
    "secondary": "உயர்நிலைக் கல்வி (10th)",
    "higher_secondary": "மேல்நிலைக் கல்வி (12th)",
    "graduate": "பட்டப்படிப்பு",
    "postgraduate": "முதுகலை",
    "dropout": "பள்ளி இடைநிற்றல்",
}

OCCUPATION_TAMIL = {
    "farmer": "விவசாயி",
    "daily_wage": "கூலித் தொழிலாளி",
    "self_employed": "சுயதொழில்",
    "govt_employee": "அரசு ஊழியர்",
    "private_employee": "தனியார் ஊழியர்",
    "unemployed": "வேலையில்லாதவர்",
    "student": "மாணவர்",
    "homemaker": "குடும்பத்தலைவி",
    "retired": "ஓய்வுபெற்றவர்",
}

RATION_CARD_TAMIL = {
    "phh": "முன்னுரிமை அட்டை (PHH)",
    "aay": "அந்தியோதயா அன்ன யோஜனா (AAY)",
    "nphh": "முன்னுரிமையற்ற அட்டை (NPHH)",
    "nphhs": "சர்க்கரை அட்டை (NPHH-S)",
    "nphhnc": "பொருளற்ற அட்டை (NPHH-NC)",
    "none": "குடும்ப அட்டை இல்லை",
}


def is_scheme_stale(scheme: Scheme) -> bool:
    """Checks if the scheme data hasn't been verified in > 180 days (6 months)."""
    if not scheme.last_verified_date:
        return True
    days = (date.today() - scheme.last_verified_date).days
    return days > STALENESS_DAYS_THRESHOLD


def translate_failed_rule_to_tamil(rule: FailedRuleDetail) -> Tuple[str, str]:
    """Translates a failed rule into:
    (missing_condition_tamil, how_to_resolve_tamil)
    """
    field = rule.field_name
    act = rule.actual_value or "இல்லை"
    exp = rule.expected_value or ""

    if field == "age":
        if rule.operator in (RuleOperator.GREATER_OR_EQUAL, RuleOperator.GREATER_THAN):
            missing = f"வயது {act} மட்டுமே உள்ளது, இத்திட்டத்திற்கு குறைந்தபட்சம் {exp} வயது பூர்த்தியடைந்திருக்க வேண்டும்."
            resolve = f"தங்களுக்கு {exp} வயது பூர்த்தியடையும் போது இத்திட்டத்திற்கு விண்ணப்பிக்க தகுதி பெறுவீர்கள்."
        elif rule.operator in (RuleOperator.LESS_OR_EQUAL, RuleOperator.LESS_THAN):
            missing = f"வயது {act} உள்ளது, இத்திட்டத்திற்கு அதிகபட்ச வயது வரம்பு {exp} ஆகும்."
            resolve = "வயது வரம்பைத் தாண்டியதால் இத்திட்டத்திற்கு விண்ணப்பிக்க இயலாது. தங்களுக்குரிய பிற திட்டங்களை பரிசீலிக்கலாம்."
        else:
            missing = f"வயது {act} உள்ளது, ஆனால் விதிமுறைப்படி {exp} இருக்க வேண்டும்."
            resolve = "வயது சான்றிதழ் (ஆதார் / பிறப்புச் சான்றிதழ்) விவரங்களை சரிபார்க்கவும்."
        return missing, resolve

    if field == "gender":
        exp_tn = GENDER_TAMIL.get(exp.lower(), exp)
        act_tn = GENDER_TAMIL.get(act.lower(), act)
        missing = f"இத்திட்டம் {exp_tn} பிரிவினருக்கு மட்டுமே பொருந்தும் (தற்போதைய பதிவு: {act_tn})."
        resolve = "பாலினம் மாற்ற இயலாத தகுதி என்பதால், தங்களுக்குப் பொருந்தும் பிற நலத்திட்டங்களை அணுகலாம்."
        return missing, resolve

    if field == "marital_status":
        exp_tn = MARITAL_STATUS_TAMIL.get(exp.lower(), exp)
        act_tn = MARITAL_STATUS_TAMIL.get(act.lower(), act)
        missing = f"திருமண நிலை '{exp_tn}' என இருக்க வேண்டும் (தற்போதைய பதிவு: {act_tn})."
        if "destitute_widow" in exp.lower() or "widow" in exp.lower():
            resolve = "வருவாய்த்துறை அல்லது வட்டாட்சியரிடம் ஆதரவற்ற விதவைச் சான்றிதழ் (Destitute Widow Certificate) பெற்றிருப்பின் சுயவிவரத்தில் புதுப்பிக்கவும்."
        elif "deserted" in exp.lower():
            resolve = "வட்டாட்சியர் அல்லது சமூக நல அலுவலரிடம் கணவனால் கைவிடப்பட்டவர் சான்றிதழ் பெற்று விவரத்தைப் புதுப்பிக்கவும்."
        else:
            resolve = f"இத்திட்டம் {exp_tn} பிரிவினருக்கு மட்டுமே உரியது."
        return missing, resolve

    if field == "total_household_income":
        missing = f"குடும்பத்தின் மாத/ஆண்டு வருமானம் ₹{act} ஆக உள்ளது, ஆனால் இத்திட்டத்திற்கு ₹{exp} அல்லது அதற்குக் குறைவாக இருக்க வேண்டும்."
        resolve = "வருமானச் சான்றிதழில் உள்ள சரியான வருமான விவரங்களை கிராம நிர்வாக அலுவலரிடம் (VAO) சரிபார்த்து புதுப்பிக்கவும்."
        return missing, resolve

    if field == "caste_category":
        exp_tn = CASTE_TAMIL.get(exp.lower(), exp)
        act_tn = CASTE_TAMIL.get(act.lower(), act)
        missing = f"இத்திட்டம் {exp_tn} வகுப்பினருக்கு மட்டுமே உரியது (தற்போதைய பதிவு: {act_tn})."
        resolve = "சமூகப் பிரிவு (ஜாதி சான்றிதழ்) மாற்ற இயலாத தகுதி என்பதால், தங்களின் பிரிவுக்குரிய பிற திட்டங்களை அணுகவும்."
        return missing, resolve

    if field == "education_level":
        exp_tn = EDUCATION_TAMIL.get(exp.lower(), exp)
        act_tn = EDUCATION_TAMIL.get(act.lower(), act)
        missing = f"கல்வித் தகுதி {exp_tn} பெற்றிருக்க வேண்டும் (தற்போதைய பதிவு: {act_tn})."
        resolve = "கல்வித் தகுதிச் சான்றிதழைப் பெற்று அல்லது கல்வி நிலையை சுயவிவரத்தில் புதுப்பிக்கவும்."
        return missing, resolve

    if field == "occupation":
        exp_tn = OCCUPATION_TAMIL.get(exp.lower(), exp)
        act_tn = OCCUPATION_TAMIL.get(act.lower(), act)
        missing = f"தொழில் நிலை '{exp_tn}' ஆக இருக்க வேண்டும் (தற்போதைய பதிவு: {act_tn})."
        resolve = "தொழில் சார்ந்த அரசு அமைப்பு அல்லது நல வாரியத்தில் (Welfare Board) உறுப்பினராகப் பதிவு செய்து விவரத்தைப் புதுப்பிக்கவும்."
        return missing, resolve

    if field == "disability_status":
        missing = "இத்திட்டம் மாற்றுத்திறனாளிகளுக்கான சிறப்புத் திட்டம் ஆகும்."
        resolve = "மாற்றுத்திறனாளிகள் நலத்துறை வழங்கும் தேசிய அடையாள அட்டை (UDID Card) பெற்றிருப்பின் சுயவிவரத்தைப் புதுப்பிக்கவும்."
        return missing, resolve

    if field == "ration_card_type":
        exp_tn = RATION_CARD_TAMIL.get(exp.lower(), exp)
        act_tn = RATION_CARD_TAMIL.get(act.lower(), act)
        missing = f"குடும்ப அட்டை வகை '{exp_tn}' ஆக இருக்க வேண்டும் (தற்போதைய பதிவு: {act_tn})."
        resolve = "உணவுப்பொருள் வழங்கல் துறையின் (TNPDS) போர்ட்டல் மூலம் குடும்ப அட்டை வகையை புதுப்பிக்க விண்ணப்பிக்கலாம்."
        return missing, resolve

    if field == "special_flags":
        missing = f"தேவையான சிறப்புத் தகுதி அல்லது சான்றிதழ் ({exp}) இணைக்கப்படவில்லை."
        resolve = "வட்டாட்சியர் அலுவலகம் அல்லது சம்பந்தப்பட்ட துறை அலுவலகத்தில் உரிய சான்றிதழ் பெற்று விவரங்களை இணைக்கவும்."
        return missing, resolve

    if field == "land_holding_acres":
        if rule.operator in (RuleOperator.LESS_OR_EQUAL, RuleOperator.LESS_THAN):
            missing = f"நிலத்தின் அளவு {act} ஏக்கர் உள்ளது, ஆனால் இத்திட்டத்திற்கு அதிகபட்சம் {exp} ஏக்கர் அல்லது அதற்கும் குறைவாக இருக்க வேண்டும் (சிறு/குறு விவசாயி)."
            resolve = "பட்டா / சிட்டா ஆவணங்களை கிராம நிர்வாக அலுவலரிடம் (VAO) சரிபார்த்து சரியான நில பரப்பளவை புதுப்பிக்கவும்."
        elif rule.operator in (RuleOperator.GREATER_OR_EQUAL, RuleOperator.GREATER_THAN):
            missing = f"நிலத்தின் அளவு {act} ஏக்கர் உள்ளது, ஆனால் இத்திட்டத்திற்கு குறைந்தபட்சம் {exp} ஏக்கர் இருக்க வேண்டும்."
            resolve = "நில ஆவணங்களை சரிபார்த்து சுயவிவரத்தில் புதுப்பிக்கவும்."
        else:
            missing = f"நிலத்தின் அளவு {act} ஏக்கர் உள்ளது, தேவைப்படும் அளவு: {exp} ஏக்கர்."
            resolve = "உழவர் அட்டை மற்றும் நில ஆவணங்களை சரிபார்க்கவும்."
        return missing, resolve

    if field == "crop_type":
        missing = f"பயிரிடப்படும் பயிர் '{exp}' ஆக இருக்க வேண்டும் (தற்போதைய பதிவு: {act})."
        resolve = "பயிர் அடங்கல் (Adangal) பதிவில் உள்ள விவரங்களை VAO அலுவலகத்தில் உறுதி செய்து புதுப்பிக்கவும்."
        return missing, resolve

    return rule.reason, "விதிமுறையை சரிபார்த்து உரிய ஆவணங்களை சமர்ப்பிக்கவும்."


def build_where_to_apply_tamil(scheme: Scheme) -> str:
    """Builds clear Tamil text indicating where and how to apply."""
    if scheme.application_mode == ApplicationMode.ONLINE:
        url_text = scheme.online_application_url or "https://www.tnesevai.tn.gov.in"
        return f"இணையதளம் வழியாக மட்டுமே விண்ணப்பிக்க முடியும்: {url_text} அல்லது அருகில் உள்ள இ-சேவை மையம்."
    elif scheme.application_mode == ApplicationMode.OFFLINE:
        return f"நேரடியாக விண்ணப்பிக்க வேண்டிய அலுவலகம்: {scheme.application_office}."
    else:  # ApplicationMode.BOTH
        url_text = scheme.online_application_url or "https://www.tnesevai.tn.gov.in"
        return (
            f"இணையதளம் / இ-சேவை மையம் ({url_text}) மூலமாகவோ அல்லது "
            f"நேரடியாக {scheme.application_office} அலுவலகத்திலோ விண்ணப்பிக்கலாம்."
        )


def build_step_by_step_instructions_tamil(scheme: Scheme) -> List[str]:
    """Builds concrete numbered Tamil steps for an eligible scheme."""
    # Step 1: Documents
    if scheme.required_documents:
        docs_str = ", ".join(scheme.required_documents)
    else:
        docs_str = "ஆதார் அட்டை, குடும்ப அட்டை, வருமானச் சான்றிதழ்"
    step1 = f"1. தேவையான ஆவணங்களை தயார் செய்யவும்: {docs_str}."

    # Step 2: Where & How to Apply
    if scheme.application_mode == ApplicationMode.ONLINE:
        url = scheme.online_application_url or "https://www.tnesevai.tn.gov.in"
        step2 = f"2. {url} இணையதளத்திற்குச் சென்று அல்லது அருகில் உள்ள இ-சேவை மையத்தை அணுகி உரிய விண்ணப்பத்தை பூர்த்தி செய்து ஆவணங்களை பதிவேற்றவும்."
    elif scheme.application_mode == ApplicationMode.OFFLINE:
        step2 = f"2. {scheme.application_office} அலுவலகத்திற்கு நேரில் சென்று விண்ணப்பப் படிவத்தைப் பெற்று, பூர்த்தி செய்து தேவையான சான்றிதழ் நகல்களுடன் சமர்ப்பிக்கவும்."
    else:
        url = scheme.online_application_url or "https://www.tnesevai.tn.gov.in"
        step2 = f"2. அருகில் உள்ள இ-சேவை மையம் / {url} மூலமாகவோ அல்லது {scheme.application_office} அலுவலகத்திற்கு நேரடியாகச் சென்றோ விண்ணப்பத்தை சமர்ப்பிக்கவும்."

    # Step 3: Acknowledgment Slip
    step3 = "3. விண்ணப்பத்தை சமர்ப்பித்த பிறகு அதற்கான ஒப்புகைச் சீட்டு (Acknowledgment Slip) மற்றும் விண்ணப்ப பதிவு எண்ணைப் பெற்று பாதுகாப்பாக வைக்கவும்."

    # Step 4: Verification and Processing Timeline
    estimate = scheme.processing_time_estimate or "15 முதல் 30 நாட்கள்"
    step4 = f"4. கிராம நிர்வாக அலுவலர் (VAO) / வருவாய் ஆய்வாளர் (RI) / நலத்துறை அலுவலரின் சரிபார்ப்பிற்குப் பிறகு {estimate} காலத்தில் பயன் வழங்கப்படும்."

    return [step1, step2, step3, step4]


def generate_grounded_tamil_explanation(
    scheme: Scheme,
    person: "Person",
    db=None,
    person_id: Optional[str] = None,
) -> Tuple[str, bool, Optional[float], str]:
    """Generate a Tamil explanation for an eligible scheme, grounded in RAG context.

    Flow:
      1. Query Pinecone for stored scheme document (by scheme_code).
      2. Check similarity score against RAG_SIMILARITY_THRESHOLD.
      3a. If score ≥ threshold → send scheme data + RAG passages to Gemini
          → returns grounded Tamil explanation.
      3b. If score < threshold OR RAG not available → return structured
          description_tamil from the SCHEME table directly.
          → flags response as "structured_data_only".
      4. Log the LLM call to LlmCallLog.

    Args:
        scheme:    The Scheme ORM object.
        person:    The Person ORM object (for personalisation).
        db:        SQLAlchemy session for LLM call logging.
        person_id: String UUID of person (for logging).

    Returns:
        (explanation_tamil, used_rag, retrieval_score, retrieval_source)
    """
    settings = get_settings()
    threshold = settings.RAG_SIMILARITY_THRESHOLD

    # ── Step 1: Try Pinecone retrieval ────────────────────────────────────────
    passages: List[str] = []
    best_score: float = 0.0

    if settings.rag_available:
        try:
            from app.services.rag_service import retrieve_scheme_context
            passages, best_score = retrieve_scheme_context(scheme.scheme_code)
        except Exception as exc:
            logger.warning("RAG retrieval failed for '%s': %s", scheme.scheme_code, exc)
            passages, best_score = [], 0.0

    # ── Step 2: Decide path ───────────────────────────────────────────────────
    use_rag = bool(passages) and best_score >= threshold and settings.llm_available

    if not use_rag:
        # Structured fallback — return description_tamil from DB unchanged
        return scheme.description_tamil, False, best_score if best_score else None, "structured_data_only"

    # ── Step 3: Grounded Gemini explanation ───────────────────────────────────
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI  # type: ignore
        from langchain_core.messages import HumanMessage  # type: ignore

        context_text = "\n\n".join(passages[:2])  # Use top 2 passages max
        docs_str = ", ".join(scheme.required_documents[:5]) if scheme.required_documents else "ஆதார் அட்டை, குடும்ப அட்டை"

        prompt = (
            f"You are a Tamil-language welfare assistance officer explaining a government scheme "
            f"to a citizen in simple, warm Tamil. The citizen's name is {person.name}, aged {person.age}.\n\n"
            f"Scheme: {scheme.name_tamil} ({scheme.name_english})\n"
            f"Benefit: {scheme.benefit_amount}\n"
            f"Department: {scheme.department}\n\n"
            f"Source document context (official):\n{context_text}\n\n"
            f"Required documents: {docs_str}\n\n"
            f"Write 2-3 sentences in Tamil explaining:\n"
            f"1. What benefit this person will receive\n"
            f"2. Why they qualify\n"
            f"Be warm, clear, and use simple Tamil. Do NOT add any eligibility conditions — "
            f"the system has already confirmed they qualify. Do NOT use English words.\n\n"
            f"Tamil explanation:"
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.3,
            max_tokens=200,
        )
        response = llm.invoke([HumanMessage(content=prompt)])
        explanation = response.content.strip()

        # Log the LLM call
        _log_guidance_call(
            db=db,
            person_id=person_id,
            scheme_code=scheme.scheme_code,
            prompt_text=prompt,
            retrieved_context=context_text,
            retrieval_score=best_score,
            used_rag=True,
            llm_output=explanation,
        )

        return explanation, True, best_score, "pinecone"

    except Exception as exc:
        logger.error("Gemini guidance generation failed for '%s': %s", scheme.scheme_code, exc)
        # Safe fallback on any LLM error
        return scheme.description_tamil, False, best_score, "structured_data_only"


def _log_guidance_call(
    db,
    person_id: Optional[str],
    scheme_code: str,
    prompt_text: str,
    retrieved_context: str,
    retrieval_score: float,
    used_rag: bool,
    llm_output: str,
) -> None:
    """Persist a guidance LLM call to LlmCallLog. Silently ignores errors."""
    if db is None:
        return
    try:
        from app.models.llm_call_log import LlmCallLog
        entry = LlmCallLog(
            call_type="guidance_generation",
            person_id=person_id,
            scheme_code=scheme_code,
            prompt_text=prompt_text,
            retrieved_context=retrieved_context,
            retrieval_score=retrieval_score,
            used_rag=used_rag,
            llm_output=llm_output,
        )
        db.add(entry)
        db.commit()
    except Exception as exc:
        logger.error("Failed to log guidance LLM call: %s", exc)


def generate_person_guidance(
    person: "Person",
    family: "Family",
    schemes: List[Scheme],
    db=None,
) -> PersonGuidanceResponse:
    """Generates a complete, personalized Tamil guidance package for a Person."""
    # 1. Run deterministic matching engine
    eligibility_result = evaluate_person_eligibility(person, family, schemes)

    # 2. Build index of schemes by UUID
    schemes_by_id: Dict[UUID, Scheme] = {s.id: s for s in schemes}

    # 3. Process Eligible Schemes
    eligible_guidance_list: List[EligibleSchemeGuidance] = []
    for item in eligibility_result.eligible_schemes:
        scheme = schemes_by_id.get(item.scheme_id)
        if not scheme:
            continue

        stale = is_scheme_stale(scheme)
        disclaimer = STALE_DISCLAIMER_TAMIL if stale else None
        where_apply = build_where_to_apply_tamil(scheme)
        steps = build_step_by_step_instructions_tamil(scheme)

        explanation_tamil, used_rag, score, source = generate_grounded_tamil_explanation(
            scheme=scheme,
            person=person,
            db=db,
            person_id=str(person.id) if getattr(person, "id", None) else None,
        )

        eligible_guidance_list.append(
            EligibleSchemeGuidance(
                scheme_id=scheme.id,
                scheme_code=scheme.scheme_code,
                name_english=scheme.name_english,
                name_tamil=scheme.name_tamil,
                benefit_amount=scheme.benefit_amount,
                benefit_summary_tamil=explanation_tamil,
                required_documents=scheme.required_documents or [],
                where_to_apply_tamil=where_apply,
                application_mode=scheme.application_mode,
                online_application_url=scheme.online_application_url,
                processing_time_estimate=scheme.processing_time_estimate,
                steps_tamil=steps,
                is_stale=stale,
                disclaimer_tamil=disclaimer,
                used_rag=used_rag,
                rag_retrieval_score=score,
                retrieval_source=source,
            )
        )

    # 4. Process Partially Eligible Schemes
    partially_eligible_guidance_list: List[PartiallyEligibleSchemeGuidance] = []
    for item in eligibility_result.partially_eligible_schemes:
        scheme = schemes_by_id.get(item.scheme_id)
        if not scheme:
            continue

        stale = is_scheme_stale(scheme)
        disclaimer = STALE_DISCLAIMER_TAMIL if stale else None

        missing_conditions: List[str] = []
        resolutions: List[str] = []

        for rule in item.failed_rules:
            missing, resolve = translate_failed_rule_to_tamil(rule)
            missing_conditions.append(missing)
            resolutions.append(resolve)

        partially_eligible_guidance_list.append(
            PartiallyEligibleSchemeGuidance(
                scheme_id=scheme.id,
                scheme_code=scheme.scheme_code,
                name_english=scheme.name_english,
                name_tamil=scheme.name_tamil,
                benefit_amount=scheme.benefit_amount,
                missing_conditions_tamil=missing_conditions,
                how_to_resolve_tamil=resolutions,
                is_stale=stale,
                disclaimer_tamil=disclaimer,
            )
        )

    return PersonGuidanceResponse(
        person_id=person.id,
        person_name=person.name,
        family_id=family.id,
        eligible_schemes_count=len(eligible_guidance_list),
        partially_eligible_schemes_count=len(partially_eligible_guidance_list),
        ineligible_schemes_count=eligibility_result.ineligible_schemes_count,
        eligible_schemes_guidance=eligible_guidance_list,
        partially_eligible_schemes_guidance=partially_eligible_guidance_list,
    )


def generate_family_guidance(
    family: Family,
    schemes: List[Scheme],
    db=None,
) -> FamilyGuidanceResponse:
    """Generates complete Tamil guidance for every member of a Family."""
    persons_guidance: List[PersonGuidanceResponse] = []
    for person in family.persons:
        guidance = generate_person_guidance(person, family, schemes, db=db)
        persons_guidance.append(guidance)

    return FamilyGuidanceResponse(
        family_id=family.id,
        district=family.district,
        taluk=family.taluk,
        total_household_income=family.total_household_income,
        total_persons=len(family.persons),
        persons_guidance=persons_guidance,
    )
