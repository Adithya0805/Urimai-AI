import uuid
import pytest
from unittest.mock import patch, MagicMock
from fastapi import status

from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme
from app.models.llm_call_log import LlmCallLog
from app.models.enums import (
    CompositionType,
    RationCardType,
    Gender,
    EducationLevel,
    Occupation,
    MaritalStatus,
    CasteCategory,
    ApplicationMode,
)
from app.services.matching_engine import evaluate_person_eligibility
from app.services.guidance_service import generate_person_guidance
from app.services.tamil_nlu import extract_with_llm_fallback


def test_eligibility_firewall_llm_cannot_alter_decision(client, db_session):
    """CRITICAL CONSTRAINT TEST:
    Asserts that the eligibility DECISION comes strictly from matching_engine (Phase 3)
    and can NEVER be modified, overridden, or altered by the LLM or RAG layer.

    We test a citizen profile with both:
    1) LLM / RAG completely disabled (fallback mode)
    2) LLM / RAG enabled with simulated/mocked LLM output

    Both must produce the exact same eligible schemes, partially eligible schemes,
    failed rule reasons, and ineligible count.
    """
    # Create test family & person
    family = Family(
        composition_type=CompositionType.NUCLEAR,
        district="மதுரை",
        taluk="மதுரை வடக்கு",
        address="10, நேதாஜி சாலை",
        ration_card_type=RationCardType.GREEN,
        total_household_income=8000,
    )
    db_session.add(family)
    db_session.commit()

    person = Person(
        family_id=family.id,
        name="மீனாட்சி அம்மாள்",
        age=65,
        gender=Gender.FEMALE,
        education_level=EducationLevel.NONE,
        occupation=Occupation.UNEMPLOYED,
        marital_status=MaritalStatus.WIDOWED,
        caste_category=CasteCategory.BC,
        disability_status=False,
        special_flags=["destitute", "widow"],
    )
    db_session.add(person)
    db_session.commit()

    active_schemes = db_session.query(Scheme).filter(Scheme.is_active == True).all()

    # 1. Pure deterministic matching result
    baseline_match = evaluate_person_eligibility(person, family, active_schemes)
    baseline_eligible_codes = sorted([s.scheme_code for s in baseline_match.eligible_schemes])
    baseline_partial_codes = sorted([s.scheme_code for s in baseline_match.partially_eligible_schemes])

    # 2. Guidance with LLM/RAG disabled
    with patch("app.config.Settings.llm_available", False), patch("app.config.Settings.rag_available", False):
        guidance_no_llm = generate_person_guidance(person, family, active_schemes, db=db_session)
        no_llm_eligible_codes = sorted([s.scheme_code for s in guidance_no_llm.eligible_schemes_guidance])
        no_llm_partial_codes = sorted([s.scheme_code for s in guidance_no_llm.partially_eligible_schemes_guidance])

    # 3. Guidance with Mocked LLM/RAG returning hallucinations / altered text
    mock_llm_response = MagicMock()
    mock_llm_response.content = "இந்த நபர் தகுதியற்றவர் என்று தவறாக கூறினாலும் விதிகள் மாறாது."

    with patch("app.config.Settings.llm_available", True), \
         patch("app.config.Settings.rag_available", True), \
         patch("app.services.rag_service.retrieve_scheme_context", return_value=(["Official GO snippet..."], 0.95)), \
         patch("langchain_google_genai.ChatGoogleGenerativeAI.invoke", return_value=mock_llm_response):
        
        guidance_with_llm = generate_person_guidance(person, family, active_schemes, db=db_session)
        with_llm_eligible_codes = sorted([s.scheme_code for s in guidance_with_llm.eligible_schemes_guidance])
        with_llm_partial_codes = sorted([s.scheme_code for s in guidance_with_llm.partially_eligible_schemes_guidance])

    # Assert firewall: The eligibility counts and scheme codes MUST BE IDENTICAL
    assert baseline_eligible_codes == no_llm_eligible_codes == with_llm_eligible_codes
    assert baseline_partial_codes == no_llm_partial_codes == with_llm_partial_codes
    assert guidance_no_llm.eligible_schemes_count == guidance_with_llm.eligible_schemes_count
    assert guidance_no_llm.partially_eligible_schemes_count == guidance_with_llm.partially_eligible_schemes_count
    assert guidance_no_llm.ineligible_schemes_count == guidance_with_llm.ineligible_schemes_count


def test_tamil_glossary_term_extraction_via_llm_fallback(db_session):
    """Tests that when an unconventional Tamil phrase fails regex extraction,
    the LLM fallback extracts the exact required enum value.
    """
    session_id = f"test_nlu_{uuid.uuid4().hex[:8]}"

    # Unconventional phrasing not in regex dictionary
    unusual_tamil_input = "நாங்கள் இருவர் மட்டுமே வாழும் தம்பதியர் இல்லம்"

    mock_llm_instance = MagicMock()
    mock_llm_instance.invoke.return_value = MagicMock(content="couple")

    mock_settings = MagicMock()
    mock_settings.llm_available = True
    mock_settings.rag_available = True
    mock_settings.GOOGLE_API_KEY = "mock-key"
    mock_settings.RAG_SIMILARITY_THRESHOLD = 0.70

    with patch("app.config.get_settings", return_value=mock_settings), \
         patch("app.services.llm_nlu.get_settings", return_value=mock_settings), \
         patch("app.services.tamil_nlu.get_settings", return_value=mock_settings), \
         patch("langchain_google_genai.ChatGoogleGenerativeAI", return_value=mock_llm_instance):

        # extractor_fn simulates regex failing
        dummy_regex_fn = lambda text: (None, False, "Clarification needed")

        val, is_valid, clarif = extract_with_llm_fallback(
            text=unusual_tamil_input,
            field_name="composition_type",
            valid_values=["single", "couple", "nuclear", "joint"],
            extractor_fn=dummy_regex_fn,
            db=db_session,
            session_id=session_id,
        )

        assert is_valid is True
        assert val == "couple"
        assert clarif is None

    # Check that LLM call was logged
    log = db_session.query(LlmCallLog).filter(LlmCallLog.session_id == session_id).first()
    assert log is not None
    assert log.call_type == "nlu_extraction"
    assert "composition_type" in log.prompt_text
    assert log.llm_output == "couple"


def test_low_retrieval_score_falls_back_gracefully(db_session):
    """Tests that when Pinecone retrieval score is below threshold (< 0.70),
    the system safely falls back to structured SCHEME fields and flags:
    used_rag = False, retrieval_source = 'structured_data_only'.
    """
    family = Family(
        composition_type=CompositionType.SINGLE,
        district="சென்னை",
        taluk="மயிலாப்பூர்",
        address="1, காமராஜர் சாலை",
        ration_card_type=RationCardType.GREEN,
        total_household_income=5000,
    )
    db_session.add(family)
    db_session.commit()

    person = Person(
        family_id=family.id,
        name="அரவிந்த்",
        age=62,
        gender=Gender.MALE,
        education_level=EducationLevel.PRIMARY,
        occupation=Occupation.UNEMPLOYED,
        marital_status=MaritalStatus.SINGLE,
        caste_category=CasteCategory.SC,
        disability_status=False,
        special_flags=["destitute"],
    )
    db_session.add(person)
    db_session.commit()

    active_schemes = db_session.query(Scheme).filter(Scheme.is_active == True).all()

    mock_settings = MagicMock()
    mock_settings.llm_available = True
    mock_settings.rag_available = True
    mock_settings.GOOGLE_API_KEY = "mock-key"
    mock_settings.RAG_SIMILARITY_THRESHOLD = 0.70

    # Simulate low retrieval similarity score (0.45 < 0.70 threshold)
    with patch("app.config.get_settings", return_value=mock_settings), \
         patch("app.services.guidance_service.get_settings", return_value=mock_settings), \
         patch("app.services.rag_service.retrieve_scheme_context", return_value=(["Unrelated passage..."], 0.45)):

        guidance = generate_person_guidance(person, family, active_schemes, db=db_session)

        # Must have eligible schemes
        assert len(guidance.eligible_schemes_guidance) > 0
        for item in guidance.eligible_schemes_guidance:
            # Fallback asserts
            assert item.used_rag is False
            assert item.retrieval_source == "structured_data_only"
            assert item.rag_retrieval_score == 0.45


def test_high_retrieval_score_uses_rag_and_logs_audit(db_session):
    """Tests that when Pinecone retrieval score >= 0.70, Gemini generates grounded guidance,
    sets used_rag=True, retrieval_source='pinecone', and records an audit log.
    """
    family = Family(
        composition_type=CompositionType.SINGLE,
        district="திருச்சி",
        taluk="திருச்சி மேற்கு",
        address="5, தில்லை நகர்",
        ration_card_type=RationCardType.GREEN,
        total_household_income=4000,
    )
    db_session.add(family)
    db_session.commit()

    person = Person(
        family_id=family.id,
        name="சுந்தரம்",
        age=68,
        gender=Gender.MALE,
        education_level=EducationLevel.NONE,
        occupation=Occupation.UNEMPLOYED,
        marital_status=MaritalStatus.SINGLE,
        caste_category=CasteCategory.BC,
        disability_status=False,
        special_flags=["destitute"],
    )
    db_session.add(person)
    db_session.commit()

    active_schemes = db_session.query(Scheme).filter(Scheme.is_active == True).all()

    grounded_tam_text = "முதியோர் ஓய்வூதியத் திட்டத்தின் கீழ் தங்களுக்கு மாதம் ₹1,000 வழங்கப்படும்."
    mock_llm_instance = MagicMock()
    mock_llm_instance.invoke.return_value = MagicMock(content=grounded_tam_text)

    mock_settings = MagicMock()
    mock_settings.llm_available = True
    mock_settings.rag_available = True
    mock_settings.GOOGLE_API_KEY = "mock-key"
    mock_settings.RAG_SIMILARITY_THRESHOLD = 0.70

    with patch("app.config.get_settings", return_value=mock_settings), \
         patch("app.services.guidance_service.get_settings", return_value=mock_settings), \
         patch("app.services.rag_service.retrieve_scheme_context", return_value=(["Official G.O. Ms. No. 123"], 0.88)), \
         patch("langchain_google_genai.ChatGoogleGenerativeAI", return_value=mock_llm_instance):

        guidance = generate_person_guidance(person, family, active_schemes, db=db_session)

        oap_item = next((s for s in guidance.eligible_schemes_guidance if s.scheme_code == "TN-SW-OAP"), None)
        assert oap_item is not None
        assert oap_item.used_rag is True
        assert oap_item.retrieval_source == "pinecone"
        assert oap_item.rag_retrieval_score == 0.88
        assert oap_item.benefit_summary_tamil == grounded_tam_text

    # Verify audit log in DB
    log = db_session.query(LlmCallLog).filter(
        LlmCallLog.scheme_code == "TN-SW-OAP",
        LlmCallLog.call_type == "guidance_generation",
    ).first()
    assert log is not None
    assert log.used_rag is True
    assert log.retrieval_score == 0.88
    assert "Official G.O. Ms. No. 123" in log.retrieved_context
    assert log.llm_output == grounded_tam_text


def test_full_guidance_endpoint_response_structure_with_rag(client, db_session):
    """Tests GET /persons/{id}/guidance endpoint returns RAG metadata correctly."""
    family = Family(
        composition_type=CompositionType.SINGLE,
        district="மதுரை",
        taluk="மதுரை வடக்கு",
        address="10, மெயின் ரோடு",
        ration_card_type=RationCardType.GREEN,
        total_household_income=5000,
    )
    db_session.add(family)
    db_session.commit()

    person = Person(
        family_id=family.id,
        name="காளியம்மாள்",
        age=63,
        gender=Gender.FEMALE,
        education_level=EducationLevel.NONE,
        occupation=Occupation.UNEMPLOYED,
        marital_status=MaritalStatus.WIDOWED,
        caste_category=CasteCategory.SC,
        disability_status=False,
        special_flags=["destitute", "widow"],
    )
    db_session.add(person)
    db_session.commit()

    res = client.get(f"/persons/{person.id}/guidance")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert "eligible_schemes_guidance" in data
    for scheme_guidance in data["eligible_schemes_guidance"]:
        assert "used_rag" in scheme_guidance
        assert "retrieval_source" in scheme_guidance
        assert scheme_guidance["retrieval_source"] in ("pinecone", "structured_data_only")
