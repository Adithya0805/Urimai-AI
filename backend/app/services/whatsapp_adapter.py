"""Urimai AI — WhatsApp Channel Interaction Adapter
======================================================
Adapts intake dialogues, numbered quick-replies, chunked guidance delivery,
multi-day resume handling, 24h template requirements, and proactive opt-in consent.
"""

import re
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional, Tuple


# Option maps for numbered quick replies
COMPOSITION_OPTIONS = {
    "1": "single",
    "2": "couple",
    "3": "nuclear",
    "4": "joint",
}

RATION_CARD_OPTIONS = {
    "1": "green",       # அரிசி அட்டை
    "2": "white",       # சர்க்கரை அட்டை
    "3": "phh_aay",     # அந்தியோதயா அன்ன யோஜனா
    "4": "khaki",       # காக்கி அட்டை
    "5": "none",        # அட்டை இல்லை
    "6": "other",       # பிற
}

GENDER_OPTIONS = {
    "1": "female",      # பெண்
    "2": "male",        # ஆண்
    "3": "transgender", # மூன்றாம் பாலினத்தவர்
    "4": "other",
}

EDUCATION_OPTIONS = {
    "1": "none",              # படிப்பறிவில்லை
    "2": "primary",           # தொடக்கக் கல்வி (1-5)
    "3": "secondary",         # 10-ஆம் வகுப்பு
    "4": "higher_secondary",  # 12-ஆம் வகுப்பு
    "5": "graduate",          # பட்டப்படிப்பு
    "6": "postgraduate",      # முதுகலை
    "7": "dropout",           # பள்ளி இடைநிற்றல்
}

OCCUPATION_OPTIONS = {
    "1": "farmer",            # விவசாயி
    "2": "daily_wage",        # கூலித் தொழிலாளி
    "3": "self_employed",     # சுயதொழில் / சிறு வியாபாரம்
    "4": "govt_employee",     # அரசு ஊழியர்
    "5": "private_employee",  # தனியார் ஊழியர்
    "6": "unemployed",        # வேலையில்லாதவர்
    "7": "student",           # மாணவர்
    "8": "homemaker",         # குடும்பத்தலைவி
    "9": "retired",           # ஓய்வுபெற்றவர்
}

MARITAL_STATUS_OPTIONS = {
    "1": "married",     # திருமணமானவர்
    "2": "single",      # திருமணமாகாதவர்
    "3": "widowed",     # விதவை / ஆதரவற்ற விதவை
    "4": "divorced",    # விவாகரத்து பெற்றவர்
}

CASTE_OPTIONS = {
    "1": "BC",          # பிற்படுத்தப்பட்டோர் (BC)
    "2": "MBC",         # மிகவும் பிற்படுத்தப்பட்டோர் (MBC)
    "3": "SC",          # பட்டியலினம் (SC)
    "4": "ST",          # பழங்குடியினர் (ST)
    "5": "DNC",         # சீர்மரபினர் (DNC)
    "6": "General",     # பொதுப்பிரிவு (General)
}

YES_NO_OPTIONS = {
    "1": "yes",
    "2": "no",
}


def normalize_phone_number(phone: str) -> str:
    """Normalizes phone numbers to standard E.164 format (+91XXXXXXXXXX)."""
    clean = re.sub(r"[^\d+]", "", phone.strip())
    if clean.startswith("whatsapp:"):
        clean = clean.replace("whatsapp:", "")
    if clean.startswith("91") and len(clean) == 12:
        clean = "+" + clean
    elif not clean.startswith("+") and len(clean) == 10:
        clean = "+91" + clean
    elif clean.startswith("0") and len(clean) == 11:
        clean = "+91" + clean[1:]
    return clean


def is_within_24h_window(last_message_time: Optional[datetime]) -> bool:
    """WhatsApp 24-hour customer service window rule."""
    if not last_message_time:
        return False
    if last_message_time.tzinfo is None:
        last_message_time = last_message_time.replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    return (now - last_message_time) <= timedelta(hours=24)


def format_whatsapp_intake_question(step: str, raw_question: str) -> str:
    """Converts a standard intake step into a mobile-first numbered quick-reply question."""
    if step == "greet":
        return (
            "🏛️ *வணக்கம்! உரிமை AI (Urimai AI) உதவி மையத்திற்கு நல்வரவு.*\n\n"
            "தமிழ்நாடு அரசின் நலத்திட்டங்களை தங்களுக்கு எளிதில் பெற்றுத்தர சில அடிப்படை விவரங்களை பதிவு செய்வோம்.\n\n"
            "தொடங்க தங்கள் குடும்ப அமைப்பை தேர்வு செய்யவும்:\n"
            "1️⃣ தனி நபர் (Single)\n"
            "2️⃣ தம்பதியர் (Couple)\n"
            "3️⃣ அணு குடும்பம் (Nuclear)\n"
            "4️⃣ கூட்டுக் குடும்பம் (Joint)\n\n"
            "👉 _உங்கள் எண்ணை (1/2/3/4) அனுப்பவும்._"
        )
    elif step == "family_composition":
        return (
            "தங்கள் குடும்ப அமைப்பை தேர்வு செய்யவும்:\n"
            "1️⃣ தனி நபர் (Single)\n"
            "2️⃣ தம்பதியர் (Couple)\n"
            "3️⃣ அணு குடும்பம் (Nuclear)\n"
            "4️⃣ கூட்டுக் குடும்பம் (Joint)\n\n"
            "👉 _எண் 1, 2, 3 அல்லது 4 என அனுப்பவும்._"
        )
    elif step == "family_ration_card":
        return (
            "தங்களிடம் உள்ள *குடும்ப அட்டை (Ration Card)* வகை என்ன?\n"
            "1️⃣ அரிசி அட்டை (Green / PHH)\n"
            "2️⃣ சர்க்கரை அட்டை (White / NPHH-S)\n"
            "3️⃣ அந்தியோதயா அட்டை (AAY)\n"
            "4️⃣ காவல் / இதர அட்டை (Khaki / Other)\n"
            "5️⃣ குடும்ப அட்டை இல்லை (None)\n\n"
            "👉 _எண் 1 முதல் 5 வரை தேர்வு செய்யவும்._"
        )
    elif step == "person_gender":
        return (
            "பாலினம் தேர்வு செய்யவும்:\n"
            "1️⃣ பெண் (Female)\n"
            "2️⃣ ஆண் (Male)\n"
            "3️⃣ மூன்றாம் பாலினத்தவர் (Transgender)\n\n"
            "👉 _எண் 1, 2 அல்லது 3 என அனுப்பவும்._"
        )
    elif step == "person_education":
        return (
            "கல்வித் தகுதியை தேர்வு செய்யவும்:\n"
            "1️⃣ படிப்பறிவில்லை\n"
            "2️⃣ தொடக்கக் கல்வி (1-5)\n"
            "3️⃣ 10-ஆம் வகுப்பு (10th)\n"
            "4️⃣ 12-ஆம் வகுப்பு (12th)\n"
            "5️⃣ பட்டப்படிப்பு (Graduate)\n"
            "6️⃣ முதுகலை (Postgraduate)\n"
            "7️⃣ பள்ளி இடைநிற்றல் (Dropout)\n\n"
            "👉 _எண் 1 முதல் 7 வரை அனுப்பவும்._"
        )
    elif step == "person_occupation":
        return (
            "தற்போதைய தொழில் / வேலை என்ன?\n"
            "1️⃣ விவசாயி (Farmer)\n"
            "2️⃣ கூலித் தொழிலாளி (Daily wage)\n"
            "3️⃣ சுயதொழில் / சிறு வியாபாரம் (Self-employed)\n"
            "4️⃣ அரசு ஊழியர் (Govt Employee)\n"
            "5️⃣ தனியார் ஊழியர் (Private Employee)\n"
            "6️⃣ வேலையில்லாதவர் (Unemployed)\n"
            "7️⃣ மாணவர் (Student)\n"
            "8️⃣ குடும்பத்தலைவி (Homemaker)\n"
            "9️⃣ ஓய்வுபெற்றவர் (Retired)\n\n"
            "👉 _எண் 1 முதல் 9 வரை அனுப்பவும்._"
        )
    elif step in ("person_marital", "person_marital_status"):
        return (
            "திருமண நிலை:\n"
            "1️⃣ திருமணமானவர் (Married)\n"
            "2️⃣ திருமணமாகாதவர் (Single)\n"
            "3️⃣ விதவை / ஆதரவற்ற விதவை (Widow/Destitute)\n"
            "4️⃣ விவாகரத்து பெற்றவர் (Divorced)\n\n"
            "👉 _எண் 1, 2, 3 அல்லது 4 என அனுப்பவும்._"
        )
    elif step == "person_caste":
        return (
            "சமூகப் பிரிவு (Caste Category):\n"
            "1️⃣ BC (பிற்படுத்தப்பட்டோர்)\n"
            "2️⃣ MBC (மிகவும் பிற்படுத்தப்பட்டோர்)\n"
            "3️⃣ SC (பட்டியலினம்)\n"
            "4️⃣ ST (பழங்குடியினர்)\n"
            "5️⃣ DNC (சீர்மரபினர்)\n"
            "6️⃣ General (பொதுப்பிரிவு)\n\n"
            "👉 _எண் 1 முதல் 6 வரை அனுப்பவும்._"
        )
    elif step == "person_disability":
        return (
            "மாற்றுத்திறனாளியா (Disability Status)?\n"
            "1️⃣ ஆம் (Yes)\n"
            "2️⃣ இல்லை (No)\n\n"
            "👉 _1 அல்லது 2 என அனுப்பவும்._"
        )
    elif step in ("person_flags", "person_special_flags"):
        return (
            "தங்களுக்கு பொருந்தும் சிறப்பு தகுதிகள் ஏதேனும் உண்டா?\n"
            "1️⃣ ஆதரவற்றோர் / கணவனால் கைவிடப்பட்டவர்\n"
            "2️⃣ பதிவுசெய்த கட்டுமானத் தொழிலாளி\n"
            "3️⃣ நாட்டுப்புறக் கலைஞர் / நெசவாளர்\n"
            "4️⃣ எதுவும் இல்லை (None)\n\n"
            "👉 _எண் 1 முதல் 4 வரை அனுப்பவும் (அல்லது நேரடியாக தட்டச்சு செய்யவும்)._"
        )
    elif step == "person_crop_type":
        return (
            "விவசாய நிலத்தில் பயிரிடப்படும் முதன்மை பயிர் எது?\n"
            "1️⃣ நெல் (Paddy)\n"
            "2️⃣ கரும்பு (Sugarcane)\n"
            "3️⃣ வாழை / தோட்டக்கலை பயிர்கள்\n"
            "4️⃣ பருத்தி / தானியங்கள்\n"
            "5️⃣ பிற பயிர்கள்\n\n"
            "👉 _எண் 1 முதல் 5 வரை அனுப்பவும்._"
        )
    elif step == "confirm_summary":
        return (
            f"{raw_question}\n\n"
            "மேற்கண்ட விவரங்கள் சரியானவையா?\n"
            "1️⃣ ஆம், விவரங்கள் சரி (Confirm)\n"
            "2️⃣ திருத்தம் செய்ய வேண்டும் (Edit)\n\n"
            "👉 _1 அல்லது 2 என அனுப்பவும்._"
        )
    return raw_question


def parse_numbered_input(step: str, text: str) -> str:
    """Maps numbered user input (e.g. '1', '2', '3') to valid domain text."""
    val = text.strip().lower()

    if step in ("greet", "family_composition"):
        if val in COMPOSITION_OPTIONS:
            return COMPOSITION_OPTIONS[val]
    elif step == "family_ration_card":
        if val in RATION_CARD_OPTIONS:
            return RATION_CARD_OPTIONS[val]
    elif step == "person_gender":
        if val in GENDER_OPTIONS:
            return GENDER_OPTIONS[val]
    elif step == "person_education":
        if val in EDUCATION_OPTIONS:
            return EDUCATION_OPTIONS[val]
    elif step == "person_occupation":
        if val in OCCUPATION_OPTIONS:
            return OCCUPATION_OPTIONS[val]
    elif step in ("person_marital", "person_marital_status"):
        if val in MARITAL_STATUS_OPTIONS:
            return MARITAL_STATUS_OPTIONS[val]
    elif step == "person_caste":
        if val in CASTE_OPTIONS:
            return CASTE_OPTIONS[val]
    elif step == "person_disability":
        if val == "1":
            return "ஆம்"
        elif val == "2":
            return "இல்லை"
    elif step in ("person_flags", "person_special_flags"):
        if val == "1":
            return "ஆதரவற்றோர்"
        elif val == "2":
            return "பதிவுசெய்த கட்டுமானத் தொழிலாளி"
        elif val == "3":
            return "நாட்டுப்புறக் கலைஞர்"
        elif val == "4":
            return "எதுவும் இல்லை"
    elif step == "person_crop_type":
        crop_map = {"1": "நெல்", "2": "கரும்பு", "3": "வாழை", "4": "பருத்தி", "5": "பிற"}
        if val in crop_map:
            return crop_map[val]
    elif step == "confirm_summary":
        if val == "1":
            return "ஆம்"
        elif val == "2":
            return "மாற்று"
    elif step == "consent_optin":
        if val == "1" or "ஆம்" in val or "yes" in val:
            return "yes"
        elif val == "2" or "இல்லை" in val or "no" in val:
            return "no"

    return text


def split_guidance_into_whatsapp_messages(
    person_name: str,
    eligible_schemes: List[Dict[str, Any]],
    partially_eligible_schemes: List[Dict[str, Any]] = None,
) -> List[str]:
    """Splits long guidance results into sequential, short WhatsApp messages to avoid walls of text."""
    messages = []
    total_eligible = len(eligible_schemes)
    total_partial = len(partially_eligible_schemes or [])

    # Message 1: High level summary
    msg1 = (
        f"🎉 *நற்செய்தி {person_name}! தங்களுக்குரிய நலத்திட்டங்கள் கண்டறியப்பட்டன.*\n\n"
        f"✅ *முழு தகுதி பெற்ற திட்டங்கள்:* {total_eligible}\n"
    )
    if total_partial > 0:
        msg1 += f"⚠️ *கூடுதல் ஆவணம் / தகுதி தேவைப்படும் திட்டங்கள்:* {total_partial}\n"
    msg1 += "\n_ஒவ்வொரு திட்டத்தின் விவரங்கள் மற்றும் விண்ணப்பிக்கும் முறைகள் கீழே அனுப்பப்படுகின்றன._"
    messages.append(msg1)

    # Messages for each eligible scheme (Max 3 full schemes on WhatsApp to keep readable)
    for idx, s in enumerate(eligible_schemes[:3], 1):
        scheme_name = s.get("name_tamil") or s.get("scheme_name", "நலத்திட்டம்")
        benefit = s.get("benefit_amount", "அரசு உதவித்தொகை")
        office = s.get("application_office", "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்")
        mode = s.get("application_mode", "both")
        portal = s.get("online_application_url") or "https://www.tnesevai.tn.gov.in"
        docs = s.get("required_documents", [])

        docs_formatted = "\n".join([f"   📄 {doc}" for doc in docs]) if docs else "   📄 குடும்ப அட்டை & ஆதார்"

        steps = s.get("steps_tamil", [])
        steps_formatted = ""
        if steps:
            steps_formatted = "\n*விண்ணப்பிக்கும் படிகள்:*\n" + "\n".join([f"{i}. {st}" for i, st in enumerate(steps[:4], 1)])

        msg_scheme = (
            f"📋 *திட்டம் {idx}: {scheme_name}*\n"
            f"💰 *பயன்:* {benefit}\n"
            f"🏢 *விண்ணப்பிக்க வேண்டிய இடம்:* {office}\n"
            f"🌐 *இணையதளம்:* {portal}\n\n"
            f"*தேவையான ஆவணங்கள்:*\n{docs_formatted}\n"
            f"{steps_formatted}"
        )
        messages.append(msg_scheme)

    # Opt-in consent message
    consent_msg = (
        "🔔 *WhatsApp நினைவூட்டல் சேவை (Reminders Opt-In):*\n\n"
        "இத்திட்டங்களுக்கு விண்ணப்பிக்க தேவையான ஆவணங்கள் மற்றும் காலக்கெடு நினைவூட்டல்களை WhatsApp-ல் பெற விரும்புகிறீர்களா?\n\n"
        "1️⃣ ஆம், நினைவூட்டல்களை அனுப்பவும் (Yes)\n"
        "2️⃣ வேண்டாம் (No)\n\n"
        "👉 _1 அல்லது 2 என பதிலளிக்கவும்._"
    )
    messages.append(consent_msg)

    return messages


def format_proactive_whatsapp_reminder(
    notification_type: str,
    person_name: str,
    scheme_name: str,
    details: str,
    is_template: bool = False,
) -> str:
    """Formats an outbound follow-up reminder for documents pending or renewal due."""
    if is_template:
        # Pre-approved WhatsApp Business Message Template format
        return (
            f"🏛️ *உரிமை AI நலத்திட்ட நினைவூட்டல்*\n\n"
            f"வணக்கம் {person_name},\n"
            f"தங்களின் *{scheme_name}* நலத்திட்ட விண்ணப்பத்திற்கு:\n"
            f"{details}\n\n"
            f"உதவிக்கு 'வணக்கம்' என இப்பக்கத்திற்கு பதிலளிக்கவும்."
        )
    else:
        return (
            f"🏛️ *உரிமை AI — நலத்திட்ட நினைவூட்டல்*\n\n"
            f"வணக்கம் {person_name}!\n\n"
            f"தங்களின் '{scheme_name}' விண்ணப்பத்தின் நிலவரம்:\n"
            f"{details}\n\n"
            f"கூடுதல் உதவிக்கு எந்த நேரத்திலும் 'வணக்கம்' என அனுப்பலாம்."
        )
