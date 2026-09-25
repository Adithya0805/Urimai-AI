import os
import re
from typing import Tuple, Optional, Any, List, Callable
from app.models.enums import (
    CompositionType,
    RationCardType,
    Gender,
    EducationLevel,
    Occupation,
    MaritalStatus,
    CasteCategory,
)
from app.config import get_settings


TAMIL_NUMBER_MAP = {
    "பூஜ்ஜியம்": 0, "ஒன்று": 1, "இரண்டு": 2, "மூன்று": 3, "நான்கு": 4, "ஐந்து": 5,
    "ஆறு": 6, "ஏழு": 7, "எட்டு": 8, "ஒன்பது": 9, "பத்து": 10,
    "இருபது": 20, "முப்பது": 30, "நாற்பது": 40, "ஐம்பது": 50,
    "அறுபது": 60, "எழுபது": 70, "எண்பது": 80, "தொண்ணூறு": 90,
    "நூறு": 100, "ஆயிரம்": 1000, "ஐந்தாயிரம்": 5000, "பத்தாயிரம்": 10000,
    "பதினைந்தாயிரம்": 15000, "இருபதாயிரம்": 20000, "இருபத்தைந்தாயிரம்": 25000,
}


def extract_number(text: str) -> Optional[int]:
    """Extract integer from numeric digits or Tamil number phrases."""
    digits = re.findall(r"\d+", text)
    if digits:
        return int(digits[0])

    text_lower = text.strip().lower()
    for word, num in TAMIL_NUMBER_MAP.items():
        if word in text_lower:
            return num
    return None


def extract_composition_type(text: str) -> Tuple[Optional[CompositionType], bool, Optional[str]]:
    """Maps free text to CompositionType enum or returns clarification request."""
    t = text.lower()
    if any(k in t for k in ["தனி", "single", "ஒருவர்", "ஒரு நபர்", "தனியாக"]):
        return CompositionType.SINGLE, True, None
    if any(k in t for k in ["தம்பதி", "couple", "கணவன் மனைவி", "இருவர் மட்டும்"]):
        return CompositionType.COUPLE, True, None
    if any(k in t for k in ["அணு", "nuclear", "பெற்றோர் குழந்தை", "சின்ன குடும்பம்", "4 பேர்", "நால்வர்", "நான்கு பேர்"]):
        return CompositionType.NUCLEAR, True, None
    if any(k in t for k in ["கூட்டு", "joint", "தாத்தா பாட்டி", "பெரிய குடும்பம்"]):
        return CompositionType.JOINT, True, None

    return None, False, (
        "தங்கள் குடும்ப அமைப்பை தயவுசெய்து குறிப்பிடவும்: "
        "1) தனி நபர் (Single), 2) தம்பதியர் (Couple), 3) அணு குடும்பம் (Nuclear), 4) கூட்டுக் குடும்பம் (Joint)."
    )


def extract_ration_card_type(text: str) -> Tuple[Optional[RationCardType], bool, Optional[str]]:
    """Maps free text to RationCardType enum or returns clarification request."""
    t = text.lower()
    if any(k in t for k in ["அரிசி", "பச்சை", "green", "phh", "முன்னுரிமை"]):
        return RationCardType.GREEN, True, None
    if any(k in t for k in ["அந்தியோதயா", "aay", "phh_aay", "வறுமை"]):
        return RationCardType.PHH_AAY, True, None
    if any(k in t for k in ["சர்க்கரை", "வெள்ளை", "white", "sugar", "பொருளற்ற", "nphh"]):
        return RationCardType.WHITE, True, None
    if any(k in t for k in ["காவல்துறை", "காக்கி", "khaki", "police"]):
        return RationCardType.KHAKI, True, None
    if any(k in t for k in ["இல்லை", "card illai", "no card", "none"]):
        return RationCardType.NONE, True, None
    if any(k in t for k in ["மஞ்சள்", "yellow"]):
        return RationCardType.YELLOW, True, None
    if any(k in t for k in ["ஆரஞ்சு", "orange"]):
        return RationCardType.ORANGE, True, None
    if any(k in t for k in ["பிற", "other"]):
        return RationCardType.OTHER, True, None

    return None, False, (
        "தங்களின் குடும்ப அட்டை வகையை தயவுசெய்து உறுதிப்படுத்தவும்: "
        "1) பச்சை / அரிசி அட்டை (Green/PHH), 2) வெள்ளை / சர்க்கரை அட்டை (White/NPHH), "
        "3) அந்தியோதயா (PHH-AAY), 4) காவல்துறை அட்டை (Khaki), 5) அட்டை இல்லை (None)."
    )


def extract_gender(text: str) -> Tuple[Optional[Gender], bool, Optional[str]]:
    """Maps free text to Gender enum."""
    t = text.lower()
    if any(k in t for k in ["பெண்", "female", "woman", "மகள்", "அம்மா", "மனைவி", "தாய்", "பாட்டி"]):
        return Gender.FEMALE, True, None
    if any(k in t for k in ["ஆண்", "male", "man", "மகன்", "அப்பா", "கணவர்", "தந்தை", "தாத்தா"]):
        return Gender.MALE, True, None
    if any(k in t for k in ["திருநங்கை", "transgender", "மூன்றாம் பாலினம்"]):
        return Gender.TRANSGENDER, True, None
    if any(k in t for k in ["பிற", "other"]):
        return Gender.OTHER, True, None

    return None, False, "தயவுசெய்து பாலினத்தை குறிப்பிடவும்: பெண் (Female), ஆண் (Male), அல்லது திருநங்கை (Transgender)."


def extract_education_level(text: str) -> Tuple[Optional[EducationLevel], bool, Optional[str]]:
    """Maps free text to EducationLevel enum."""
    t = text.lower()
    if any(k in t for k in ["படிக்கவில்லை", "none", "படிப்பறிவு இல்லை", "எழுத படிக்க தெரியாது"]):
        return EducationLevel.NONE, True, None
    if any(k in t for k in ["தொடக்க", "primary", "1 முதல் 5", "5th", "5 ஆம்"]):
        return EducationLevel.PRIMARY, True, None
    if any(k in t for k in ["நடுநிலை", "secondary", "10th", "10 ஆம்", "பத்தாம்", "sslc", "8th", "6 முதல் 10"]):
        return EducationLevel.SECONDARY, True, None
    if any(k in t for k in ["மேல்நிலை", "higher secondary", "higher_secondary", "12th", "12 ஆம்", "பன்னிரண்டாம்", "+2", "hsc"]):
        return EducationLevel.HIGHER_SECONDARY, True, None
    if any(k in t for k in ["பட்டதாரி", "graduate", "டிகிரி", "degree", "கல்லூரி", "b.a", "b.sc", "b.com", "b.e"]):
        return EducationLevel.GRADUATE, True, None
    if any(k in t for k in ["முதுகலை", "postgraduate", "pg", "m.a", "m.sc", "m.com", "m.e"]):
        return EducationLevel.POSTGRADUATE, True, None
    if any(k in t for k in ["இடைநின்றவர்", "dropout", "படிப்பை நிறுத்தியவர்"]):
        return EducationLevel.DROPOUT, True, None

    return None, False, (
        "கல்வித் தகுதியை தேர்வு செய்யவும்: "
        "1) படிக்கவில்லை, 2) தொடக்கக் கல்வி (1-5), 3) பத்தாம் வகுப்பு (Secondary), "
        "4) 12-ஆம் வகுப்பு (Higher Secondary), 5) பட்டதாரி (Graduate), 6) முதுகலை (Postgraduate)."
    )


def extract_occupation(text: str) -> Tuple[Optional[Occupation], bool, Optional[str]]:
    """Maps free text to Occupation enum."""
    t = text.lower()
    if any(k in t for k in ["விவசாயி", "விவசாயம்", "farmer", "வேளாண்மை", "உழவர்"]):
        return Occupation.FARMER, True, None
    if any(k in t for k in ["கூலி", "தினக்கூலி", "daily wage", "daily_wage", "சுமை தூக்கும்", "சித்தாள்", "தொழிலாளி"]):
        return Occupation.DAILY_WAGE, True, None
    if any(k in t for k in ["சுயதொழில்", "தையல்", "வியாபாரம்", "கடை", "self employed", "self_employed", "business"]):
        return Occupation.SELF_EMPLOYED, True, None
    if any(k in t for k in ["அரசு", "govt", "government", "govt_employee", "அரசு ஊழியர்", "ஆசிரியர்", "அலுவலகம்"]):
        return Occupation.GOVT_EMPLOYEE, True, None
    if any(k in t for k in ["தனியார்", "private", "private_employee", "ஐடி", "நிறுவனம்", "கம்பெனி"]):
        return Occupation.PRIVATE_EMPLOYEE, True, None
    if any(k in t for k in ["வேலையில்லை", "unemployed", "வேலை தேடுகிறார்", "வேலை இல்லை"]):
        return Occupation.UNEMPLOYED, True, None
    if any(k in t for k in ["மாணவர்", "மாணவி", "student", "படிக்கிறார்", "பள்ளியில்", "கல்லூரியில்"]):
        return Occupation.STUDENT, True, None
    if any(k in t for k in ["இல்லத்தரசி", "வீட்டு வேலை", "homemaker", "ஹவுஸ் ஒய்ப்"]):
        return Occupation.HOMEMAKER, True, None
    if any(k in t for k in ["ஓய்வு", "retired", "பென்ஷன்"]):
        return Occupation.RETIRED, True, None
    if any(k in t for k in ["பிற", "other"]):
        return Occupation.OTHER, True, None

    return None, False, (
        "தங்கள் தொழில் விவரத்தை குறிப்பிடவும்: "
        "1) விவசாயி (Farmer), 2) தினக்கூலி (Daily Wage), 3) சுயதொழில்/தையல் (Self Employed), "
        "4) அரசு ஊழியர் (Govt), 5) தனியார் ஊழியர் (Private), 6) இல்லத்தரசி (Homemaker), "
        "7) மாணவர் (Student), 8) வேலையில்லை (Unemployed), 9) ஓய்வு பெற்றவர் (Retired), 10) பிற (Other)."
    )


def extract_marital_status(text: str) -> Tuple[Optional[MaritalStatus], bool, Optional[str]]:
    """Maps free text to MaritalStatus enum."""
    t = text.lower()
    if any(k in t for k in ["விதவை", "widow", "widowed", "கணவர் இறந்துவிட்டார்", "கணவர் மறைந்துவிட்டார்"]):
        return MaritalStatus.WIDOWED, True, None
    if any(k in t for k in ["பிரிந்தவர்", "விவாகரத்து", "கைவிடப்பட்டவர்", "divorced", "deserted"]):
        return MaritalStatus.DIVORCED, True, None
    if any(k in t for k in ["திருமணமாகாதவர்", "திருமணமாகவில்லை", "திருமணம் ஆகவில்லை", "single", "கன்னி", "சிங்கிள்"]):
        return MaritalStatus.SINGLE, True, None
    if any(k in t for k in ["திருமணமானவர்", "திருமணம் ஆகியுள்ளது", "திருமணம்", "married"]):
        return MaritalStatus.MARRIED, True, None

    return None, False, "திருமண நிலையை தெரிவிக்கவும்: திருமணமாகாதவர் (Single), திருமணமானவர் (Married), விதவை (Widowed), விவாகரத்து/பிரிந்தவர் (Divorced)."



def extract_caste_category(text: str) -> Tuple[Optional[CasteCategory], bool, Optional[str]]:
    """Maps free text to CasteCategory enum."""
    t = text.upper()
    tl = text.lower()
    if "SC" in t or "ஆதிதிராவிடர்" in tl or "பட்டியல் சாதி" in tl or "அருந்ததியர்" in tl:
        return CasteCategory.SC, True, None
    if "ST" in t or "பழங்குடியினர்" in tl or "பழங்குடி" in tl:
        return CasteCategory.ST, True, None
    if "MBC" in t or "மிகவும் பிற்படுத்தப்பட்டோர்" in tl:
        return CasteCategory.MBC, True, None
    if "DNC" in t or "சீர்மரபினர்" in tl or "டிஎன்சி" in tl:
        return CasteCategory.DNC, True, None
    if "BC" in t or "பிற்படுத்தப்பட்டோர்" in tl:
        return CasteCategory.BC, True, None
    if "GENERAL" in t or "OC" in t or "பொதுப்பிரிவு" in tl or "முன்னேறிய" in tl:
        return CasteCategory.GENERAL, True, None

    return None, False, "சமூகப் பிரிவை (Caste Category) குறிப்பிடவும்: SC (ஆதிதிராவிடர்), ST (பழங்குடியினர்), BC (பிற்படுத்தப்பட்டோர்), MBC (மிகவும் பிற்படுத்தப்பட்டோர்), DNC (சீர்மரபினர்), General (பொதுப்பிரிவு)."


def extract_disability_status(text: str) -> Tuple[bool, bool, Optional[str]]:
    """Maps free text to boolean disability status."""
    t = text.lower()
    if any(k in t for k in ["ஆம்", "உண்டு", "yes", "மாற்றுத்திறனாளி", "ஊனமுற்றவர்", "பாதிக்கப்பட்டுள்ளது"]):
        return True, True, None
    if any(k in t for k in ["இல்லை", "no", "உடல் நலம்", "நன்றாக உள்ளார்"]):
        return False, True, None

    return False, False, "உடல் ஊனம் அல்லது மாற்றுத்திறனாளி நிலை உள்ளதா? ஆம் (Yes) அல்லது இல்லை (No) என தெரிவிக்கவும்."


def extract_special_flags(text: str) -> List[str]:
    """Extracts known welfare tags from free text."""
    flags = []
    t = text.lower()
    if any(k in t for k in ["ஆதரவற்ற", "destitute", "வருமானம் இல்லை", "யாரும் இல்லை"]):
        flags.append("destitute")
    if any(k in t for k in ["விதவை", "widow"]):
        flags.append("widow")
    if any(k in t for k in ["அனாதை", "orphan", "பெற்றோர் இல்லை"]):
        flags.append("orphan")
    if any(k in t for k in ["கலைஞர்", "நாட்டுப்புற", "folk artist"]):
        flags.append("folk_artist")
    if any(k in t for k in ["பத்திரிகையாளர்", "செய்தியாளர்", "journalist"]):
        flags.append("journalist")
    if any(k in t for k in ["கட்டுமான தொழிலாளி", "construction worker"]):
        flags.append("registered_construction_worker")
    if any(k in t for k in ["முன்னாள் படைவீரர்", "ராணுவம்", "ex-serviceman"]):
        flags.append("ex_serviceman")
    if any(k in t for k in ["உழவர் அட்டை", "உழவர் பாதுகாப்பு", "uzhavar"]):
        flags.append("uzhavar_card")
    if any(k in t for k in ["அமைப்புசாரா", "unorganized"]):
        flags.append("unorganized_worker")
    if any(k in t for k in ["முதல் தலைமுறை", "first graduate"]):
        flags.append("first_graduate")
    return flags


def extract_land_holding(text: str) -> Tuple[float, bool, Optional[str]]:
    """Extracts agricultural land holding in acres (supports float, integer, or 'none')."""
    t = text.lower().strip()
    if any(k in t for k in ["இல்லை", "நிலமில்லை", "நிலம் இல்லை", "0", "zero", "கூலி", "நிலமற்ற"]):
        return 0.0, True, None

    matches = re.findall(r"\d+(?:\.\d+)?", t)
    if matches:
        return float(matches[0]), True, None

    for word, num in TAMIL_NUMBER_MAP.items():
        if word in t:
            return float(num), True, None

    return 0.0, False, "விவசாய நிலத்தின் அளவை ஏக்கரில் குறிப்பிடவும் (உதாரணம்: 2.5 அல்லது 1 ஏக்கர், நிலமில்லை எனில் 0)."


def extract_crop_type(text: str) -> Tuple[str, bool, Optional[str]]:
    """Extracts primary crop type or returns clarification."""
    t = text.lower().strip()
    if any(k in t for k in ["நெல்", "paddy", "அரிசி"]):
        return "paddy", True, None
    if any(k in t for k in ["சிறுதானியம்", "கேழ்வரகு", "கம்பு", "சோளம்", "millet", "millets"]):
        return "millets", True, None
    if any(k in t for k in ["பருத்தி", "cotton"]):
        return "cotton", True, None
    if any(k in t for k in ["கரும்பு", "sugarcane"]):
        return "sugarcane", True, None
    if any(k in t for k in ["தோட்டக்கலை", "வாழை", "மா", "காய்கறி", "பூக்கள்", "horticulture"]):
        return "horticulture", True, None
    if any(k in t for k in ["பயறு", "உளுந்து", "பாசிப்பயறு", "துவரை", "pulses"]):
        return "pulses", True, None
    if any(k in t for k in ["எண்ணெய்", "நிலக்கடலை", "எள்ளு", "oilseeds"]):
        return "oilseeds", True, None
    if any(k in t for k in ["தென்னை", "தேங்காய்", "coconut"]):
        return "coconut", True, None
    if any(k in t for k in ["இல்லை", "எதுவும் இல்லை", "none"]):
        return "none", True, None

    if len(t) >= 2:
        return t, True, None

    return "other", False, "பயிரின் பெயரை குறிப்பிடவும் (நெல் / சிறுதானியங்கள் / பருத்தி / கரும்பு / தோட்டக்கலை / பயறு வகைகள் / எண்ணெய் வித்துக்கள்)."


# ── LLM Fallback Wrapper ────────────────────────────────────────────────────────

def extract_with_llm_fallback(
    text: str,
    field_name: str,
    valid_values: List[str],
    extractor_fn: Callable,
    db=None,
    session_id: Optional[str] = None,
) -> Tuple[Optional[Any], bool, Optional[str]]:
    """Try regex extractor first; if it fails and LLM is available, call Gemini.

    This wrapper preserves the full original regex behaviour as the primary
    path. Gemini is only invoked when:
      1. The regex extractor returns is_valid=False (no match found), AND
      2. LLM is enabled (get_settings().llm_available is True), AND
      3. GOOGLE_API_KEY is present in the environment.

    The eligibility decision (matching_engine.py) is NEVER called from here.
    This function only extracts a single field value from user-provided text.

    Args:
        text:          Raw Tamil user input string.
        field_name:    Name of the field being extracted (for logging + prompt).
        valid_values:  List of allowed enum values for the field.
        extractor_fn:  The existing regex extractor (e.g. extract_gender).
        db:            SQLAlchemy session (for LLM call logging). Optional.
        session_id:    Intake session ID (for logging). Optional.

    Returns:
        (value_or_none, is_valid, clarification_or_none) — same shape as all
        existing extractor functions.
    """
    # ── Primary: Try regex extractor ──────────────────────────────────────────
    result = extractor_fn(text)

    if len(result) == 3:
        value, is_valid, clarification = result
    else:
        # Some extractors return only 2 values (e.g. extract_disability_status)
        value, is_valid = result[0], result[1]
        clarification = result[2] if len(result) > 2 else None

    if is_valid:
        return value, True, None

    # ── Secondary: Try Gemini LLM fallback ────────────────────────────────────
    settings = get_settings()
    if not settings.llm_available:
        # LLM disabled — return the regex result as-is
        return value, is_valid, clarification

    from app.services.llm_nlu import gemini_extract_field
    llm_value, llm_valid, llm_clarif = gemini_extract_field(
        raw_text=text,
        field_name=field_name,
        valid_values=valid_values,
        db=db,
        session_id=session_id,
    )

    if llm_valid and llm_value is not None:
        return llm_value, True, None

    # Both regex and LLM failed — return the original clarification message
    return value, False, clarification or llm_clarif
