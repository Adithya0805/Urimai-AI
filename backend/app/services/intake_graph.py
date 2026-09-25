import uuid
from typing import Dict, Any, Tuple
from sqlalchemy.orm import Session
from app.models.family import Family
from app.models.person import Person
from app.models.intake_log import IntakeExtractionLog
from app.services.intake_state import IntakeState
from app.services.tamil_nlu import (
    extract_number,
    extract_composition_type,
    extract_ration_card_type,
    extract_gender,
    extract_education_level,
    extract_occupation,
    extract_marital_status,
    extract_caste_category,
    extract_disability_status,
    extract_special_flags,
    extract_land_holding,
    extract_crop_type,
    extract_with_llm_fallback,
)


def log_extraction(
    db: Session,
    session_id: str,
    raw_input: str,
    target_field: str,
    extracted_val: Any,
    is_valid: bool = True,
    error_msg: str = None,
    confirmed_val: str = None,
):
    """Persist extraction audit log."""
    log_entry = IntakeExtractionLog(
        session_id=session_id,
        raw_tamil_input=raw_input,
        target_field=target_field,
        extracted_value=str(extracted_val),
        confirmed_value=str(confirmed_val) if confirmed_val else None,
        is_valid=is_valid,
        error_message=error_msg,
    )
    db.add(log_entry)
    db.commit()


def process_user_turn(state: IntakeState, user_input: str, db: Session) -> IntakeState:
    """Deterministic step-by-step Tamil intake state machine."""
    text = user_input.strip()
    step = state["current_step"]
    session_id = state["session_id"]
    state["latest_user_message"] = text

    # Global: Check if user asks for mid-conversation correction
    t_lower = text.lower()
    if step == "confirm_summary":
        if any(w in t_lower for w in ["ஆம்", "சரி", "yes", "ok", "correct", "உறுதி", "சரியாக உள்ளது"]):
            state["is_confirmed"] = True
            return step_save_to_database(state, db)
        elif any(w in t_lower for w in ["மாற்று", "தவறு", "change", "edit", "நோ", "இல்லை"]):
            state["reply"] = (
                "எந்த விவரத்தை மாற்ற வேண்டும் என்பதை குறிப்பிடவும். "
                "(உதாரணம்: 'வயது 60' அல்லது 'வருமானம் 10000' அல்லது 'தொழில் விவசாயி')"
            )
            return state
        else:
            # Check if user directly provided a correction (e.g. 'வயது 62' or 'வருமானம் 12000')
            if "வயது" in text or "age" in t_lower:
                num = extract_number(text)
                if num and state["persons_data"]:
                    state["persons_data"][0]["age"] = num
                    log_extraction(db, session_id, text, "person.age", num, True, confirmed_val=str(num))
                    return generate_summary(state)
            if "வருமானம்" in text or "income" in t_lower:
                num = extract_number(text)
                if num:
                    state["family_data"]["total_household_income"] = num
                    log_extraction(db, session_id, text, "family.income", num, True, confirmed_val=str(num))
                    return generate_summary(state)

    # 1. Greet / Start
    if step == "greet":
        state["current_step"] = "family_composition"
        state["reply"] = (
            "வணக்கம்! உரிமை AI (Urimai AI) தளத்திற்கு உங்களை வரவேற்கிறோம். "
            "தங்களுக்குரிய தமிழ்நாடு அரசு நலத்திட்டங்களை கண்டறிய குடும்ப விவரங்களை பதிவு செய்வோம்.\n\n"
            "தங்கள் குடும்ப அமைப்பை குறிப்பிடவும்: "
            "1) தனி நபர் (Single), 2) தம்பதியர் (Couple), 3) அணு குடும்பம் (Nuclear), 4) கூட்டுக் குடும்பம் (Joint)?"
        )
        return state

    # 2. Family Info Collection
    if step == "family_composition":
        comp, is_valid, clarif = extract_with_llm_fallback(
            text, "composition_type",
            ["single", "couple", "nuclear", "joint"],
            extract_composition_type, db, session_id,
        )
        log_extraction(db, session_id, text, "family.composition_type", comp, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        state["family_data"]["composition_type"] = comp.value if hasattr(comp, "value") else comp
        state["current_step"] = "family_district"
        state["reply"] = "தங்கள் மாவட்டம் எது? (உதாரணம்: மதுரை, சென்னை, கோயம்புத்தூர், திருச்சிராப்பள்ளி)"
        return state

    if step == "family_district":
        district = text.strip()
        state["family_data"]["district"] = district
        log_extraction(db, session_id, text, "family.district", district, True)
        state["current_step"] = "family_taluk"
        state["reply"] = f"தங்களின் மாவட்டம் {district}. தங்கள் வட்டம் (Taluk) எது? (உதாரணம்: மதுரை வடக்கு, மைலாப்பூர், பொள்ளாச்சி)"
        return state

    if step == "family_taluk":
        taluk = text.strip()
        state["family_data"]["taluk"] = taluk
        log_extraction(db, session_id, text, "family.taluk", taluk, True)
        state["current_step"] = "family_address"
        state["reply"] = "தங்களின் வீட்டு முகவரியை (Address) குறிப்பிடவும்:"
        return state

    if step == "family_address":
        address = text.strip()
        state["family_data"]["address"] = address
        log_extraction(db, session_id, text, "family.address", address, True)
        state["current_step"] = "family_ration_card"
        state["reply"] = (
            "தங்களின் குடும்ப அட்டை (Ration Card) வகை என்ன? "
            "1) பச்சை / அரிசி அட்டை (Green), 2) வெள்ளை / சர்க்கரை அட்டை (White), "
            "3) அந்தியோதயா (PHH-AAY), 4) காவல்துறை அட்டை (Khaki), 5) அட்டை இல்லை (None)?"
        )
        return state

    if step == "family_ration_card":
        card, is_valid, clarif = extract_with_llm_fallback(
            text, "ration_card_type",
            ["none", "green", "white", "khaki", "phh_aay", "orange", "yellow", "other"],
            extract_ration_card_type, db, session_id,
        )
        log_extraction(db, session_id, text, "family.ration_card_type", card, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        state["family_data"]["ration_card_type"] = card.value if hasattr(card, "value") else card
        state["current_step"] = "family_income"
        state["reply"] = "குடும்பத்தின் மொத்த மாதாந்திர வருமானம் (Monthly Household Income) தோராயமாக எவ்வளவு? (ரூபாயில்)"
        return state

    if step == "family_income":
        income = extract_number(text)
        if income is None or income < 0:
            clarif = "வருமானத்தை சரியான எண்ணாக (ரூபாயில்) குறிப்பிடவும். (உதாரணம்: 15000 அல்லது 'வருமானம் இல்லை' எனில் 0)"
            log_extraction(db, session_id, text, "family.total_household_income", income, False, clarif)
            state["reply"] = clarif
            return state

        state["family_data"]["total_household_income"] = income
        log_extraction(db, session_id, text, "family.total_household_income", income, True)
        state["current_step"] = "person_count"
        state["reply"] = "தங்கள் குடும்பத்தில் எத்தனை நபர்களின் விவரங்களை பதிவு செய்ய வேண்டும்?"
        return state

    if step == "person_count":
        cnt = extract_number(text)
        if cnt is None or cnt <= 0:
            state["reply"] = "நபர்களின் எண்ணிக்கையை 1 அல்லது அதற்கு மேற்பட்ட எண்ணாக குறிப்பிடவும். (உதாரணம்: 1, 2, 4)"
            return state

        state["total_persons_target"] = cnt
        state["current_person_idx"] = 0
        state["current_person_temp"] = {}
        state["current_step"] = "person_name"
        idx_label = "முதல்" if cnt > 1 else ""
        state["reply"] = f"நன்றி. {idx_label} நபரின் முழு பெயர் என்ன?"
        return state

    # 3. Person Info Collection Loop
    curr_temp = state["current_person_temp"]
    idx = state["current_person_idx"]

    if step == "person_name":
        name = text.strip()
        curr_temp["name"] = name
        log_extraction(db, session_id, text, f"person[{idx}].name", name, True)
        state["current_step"] = "person_age"
        state["reply"] = f"{name} அவர்களின் வயது என்ன?"
        return state

    if step == "person_age":
        age = extract_number(text)
        if age is None or age <= 0:
            clarif = "வயதை 0-வை விட அதிகமான எண்ணாக குறிப்பிடவும். (உதாரணம்: 34 அல்லது 62)"
            log_extraction(db, session_id, text, f"person[{idx}].age", age, False, clarif)
            state["reply"] = clarif
            return state

        curr_temp["age"] = age
        log_extraction(db, session_id, text, f"person[{idx}].age", age, True)
        state["current_step"] = "person_gender"
        state["reply"] = f"{curr_temp['name']} அவர்களின் பாலினம் என்ன? (பெண் / ஆண் / திருநங்கை)"
        return state

    if step == "person_gender":
        gender, is_valid, clarif = extract_with_llm_fallback(
            text, "gender",
            ["male", "female", "transgender", "other"],
            extract_gender, db, session_id,
        )
        log_extraction(db, session_id, text, f"person[{idx}].gender", gender, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["gender"] = gender.value if hasattr(gender, "value") else gender
        state["current_step"] = "person_education"
        state["reply"] = "கல்வித் தகுதி என்ன? (படிக்கவில்லை / தொடக்கக் கல்வி / பத்தாம் வகுப்பு / 12-ஆம் வகுப்பு / பட்டதாரி / முதுகலை)"
        return state

    if step == "person_education":
        edu, is_valid, clarif = extract_with_llm_fallback(
            text, "education_level",
            ["none", "primary", "secondary", "higher_secondary", "graduate", "postgraduate", "dropout"],
            extract_education_level, db, session_id,
        )
        log_extraction(db, session_id, text, f"person[{idx}].education_level", edu, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["education_level"] = edu.value if hasattr(edu, "value") else edu
        state["current_step"] = "person_occupation"
        state["reply"] = (
            "தொழில் என்ன? (விவசாயி / தினக்கூலி / சுயதொழில் / அரசு ஊழியர் / தனியார் ஊழியர் / "
            "இல்லத்தரசி / மாணவர் / வேலையில்லை / ஓய்வு பெற்றவர் / பிற)?"
        )
        return state

    if step == "person_occupation":
        occ, is_valid, clarif = extract_with_llm_fallback(
            text, "occupation",
            ["farmer", "daily_wage", "self_employed", "govt_employee", "private_employee",
             "unemployed", "student", "homemaker", "retired", "other"],
            extract_occupation, db, session_id,
        )
        log_extraction(db, session_id, text, f"person[{idx}].occupation", occ, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["occupation"] = occ.value if hasattr(occ, "value") else occ
        # Adaptive branching: if farmer, ask land holding and crop type
        if (occ.value if hasattr(occ, "value") else occ) == "farmer":
            state["current_step"] = "person_land_holding"
            state["reply"] = "விவசாய நிலத்தின் அளவு (ஏக்கரில்) எவ்வளவு? நிலமற்ற கூலி விவசாயி எனில் 0 எனக் குறிப்பிடவும்."
            return state

        # Adaptive branching: if other, ask details; else skip to marital status
        if (occ.value if hasattr(occ, "value") else occ) == "other":
            curr_temp["land_holding_acres"] = 0.0
            curr_temp["crop_type"] = None
            state["current_step"] = "person_occupation_detail"
            state["reply"] = "தயவுசெய்து தொழில் பற்றிய கூடுதல் விவரத்தை குறிப்பிடவும்:"
            return state

        curr_temp["land_holding_acres"] = 0.0
        curr_temp["crop_type"] = None
        curr_temp["occupation_detail"] = None
        state["current_step"] = "person_marital"
        state["reply"] = "திருமண நிலை என்ன? (திருமணமாகாதவர் / திருமணமானவர் / விதவை / விவாகரத்து)?"
        return state

    if step == "person_land_holding":
        land, is_valid, clarif = extract_land_holding(text)
        log_extraction(db, session_id, text, f"person[{idx}].land_holding_acres", land, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["land_holding_acres"] = land
        state["current_step"] = "person_crop_type"
        state["reply"] = "பயிரிடப்படும் முதன்மைப் பயிர் என்ன? (நெல் / சிறுதானியங்கள் / பருத்தி / கரும்பு / தோட்டக்கலை / பயறு வகைகள் / எண்ணெய் வித்துக்கள் / பிற)?"
        return state

    if step == "person_crop_type":
        crop, is_valid, clarif = extract_crop_type(text)
        log_extraction(db, session_id, text, f"person[{idx}].crop_type", crop, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["crop_type"] = crop
        curr_temp["occupation_detail"] = None
        state["current_step"] = "person_marital"
        state["reply"] = "திருமண நிலை என்ன? (திருமணமாகாதவர் / திருமணமானவர் / விதவை / விவாகரத்து)?"
        return state

    if step == "person_occupation_detail":
        curr_temp["occupation_detail"] = text.strip()
        state["current_step"] = "person_marital"
        state["reply"] = "திருமண நிலை என்ன? (திருமணமாகாதவர் / திருமணமானவர் / விதவை / விவாகரத்து)?"
        return state

    if step == "person_marital":
        mar, is_valid, clarif = extract_with_llm_fallback(
            text, "marital_status",
            ["single", "married", "widowed", "divorced"],
            extract_marital_status, db, session_id,
        )
        log_extraction(db, session_id, text, f"person[{idx}].marital_status", mar, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["marital_status"] = mar.value if hasattr(mar, "value") else mar
        state["current_step"] = "person_caste"
        state["reply"] = "சமூகப் பிரிவு (Caste Category) என்ன? (SC / ST / BC / MBC / DNC / General)?"
        return state

    if step == "person_caste":
        caste, is_valid, clarif = extract_with_llm_fallback(
            text, "caste_category",
            ["SC", "ST", "BC", "MBC", "DNC", "General"],
            extract_caste_category, db, session_id,
        )
        log_extraction(db, session_id, text, f"person[{idx}].caste_category", caste, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["caste_category"] = caste.value if hasattr(caste, "value") else caste
        state["current_step"] = "person_disability"
        state["reply"] = "உடல் ஊனம் அல்லது மாற்றுத்திறனாளி நிலை உள்ளதா? (ஆம் / இல்லை)?"
        return state

    if step == "person_disability":
        dis_status, is_valid, clarif = extract_disability_status(text)
        log_extraction(db, session_id, text, f"person[{idx}].disability_status", dis_status, is_valid, clarif)
        if not is_valid:
            state["reply"] = clarif
            return state

        curr_temp["disability_status"] = dis_status
        # Adaptive branching: if disabled, ask type; else skip
        if dis_status:
            state["current_step"] = "person_disability_type"
            state["reply"] = "மாற்றுத்திறன் வகையை குறிப்பிடவும் (உதாரணம்: locomotor, visual, hearing):"
            return state

        curr_temp["disability_type"] = None
        state["current_step"] = "person_flags"
        state["reply"] = "ஏதேனும் சிறப்பு பிரிவுகள் உள்ளதா? (ஆதரவற்றவர் / விதவை / அனாதை / நாட்டுப்புற கலைஞர் / கட்டுமான தொழிலாளி / ஏதுமில்லை)?"
        return state

    if step == "person_disability_type":
        curr_temp["disability_type"] = text.strip()
        state["current_step"] = "person_flags"
        state["reply"] = "ஏதேனும் சிறப்பு பிரிவுகள் உள்ளதா? (ஆதரவற்றவர் / விதவை / அனாதை / நாட்டுப்புற கலைஞர் / கட்டுமான தொழிலாளி / ஏதுமில்லை)?"
        return state

    if step == "person_flags":
        flags = extract_special_flags(text)
        # Inherit widow flag if marital status was widowed
        if curr_temp.get("marital_status") == "widowed" and "widow" not in flags:
            flags.append("widow")

        curr_temp["special_flags"] = flags
        log_extraction(db, session_id, text, f"person[{idx}].special_flags", flags, True)

        # Save this person into persons_data
        state["persons_data"].append(dict(curr_temp))
        state["current_person_temp"] = {}

        # Check if more persons need to be added
        if state["current_person_idx"] + 1 < state["total_persons_target"]:
            state["current_person_idx"] += 1
            next_num = state["current_person_idx"] + 1
            state["current_step"] = "person_name"
            state["reply"] = f"நன்றி. {next_num}-வது நபரின் முழு பெயர் என்ன?"
            return state
        else:
            return generate_summary(state)

    state["reply"] = "புரியவில்லை. தொடர தங்கள் பதிலை மீண்டும் தெரிவிக்கவும்."
    return state


def generate_summary(state: IntakeState) -> IntakeState:
    """Generate a clean Tamil summary for user confirmation."""
    fam = state["family_data"]
    persons = state["persons_data"]

    lines = [
        "📋 **பதிவு செய்யப்பட்ட விவரங்களின் சுருக்கம்:**",
        "",
        "🏠 **குடும்ப விவரங்கள்:**",
        f"- குடும்ப அமைப்பு: {fam.get('composition_type')}",
        f"- மாவட்டம்: {fam.get('district')}",
        f"- வட்டம்: {fam.get('taluk')}",
        f"- முகவரி: {fam.get('address')}",
        f"- குடும்ப அட்டை: {fam.get('ration_card_type')}",
        f"- மாதாந்திர வருமானம்: ₹{fam.get('total_household_income'):,}",
        "",
        f"👥 **உறுப்பினர்கள் ({len(persons)} நபர்):**",
    ]

    for i, p in enumerate(persons, 1):
        flags_str = ", ".join(p.get("special_flags", [])) or "எதுவுமில்லை"
        dis_str = f"ஆம் ({p.get('disability_type')})" if p.get("disability_status") else "இல்லை"
        agri_str = f", நிலம்: {p.get('land_holding_acres', 0)} ஏக்கர், பயிர்: {p.get('crop_type', 'இல்லை')}" if p.get("occupation") == "farmer" else ""
        lines.extend([
            f"{i}. **{p.get('name')}** (வயது: {p.get('age')}, {p.get('gender')})",
            f"   - கல்வி: {p.get('education_level')}, தொழில்: {p.get('occupation')}{agri_str}",
            f"   - திருமண நிலை: {p.get('marital_status')}, சமூகப் பிரிவு: {p.get('caste_category')}",
            f"   - மாற்றுத்திறன்: {dis_str}, சிறப்பு பிரிவுகள்: {flags_str}",
        ])

    lines.extend([
        "",
        "மேலே உள்ள தகவல்கள் சரியானவையா? உறுதிப்படுத்த **'ஆம்'** அல்லது **'சரி'** என பதிவிடவும். "
        "மாற்றம் செய்ய வேண்டுமெனில் குறிப்பிடவும்."
    ])

    summary_text = "\n".join(lines)
    state["summary_tamil"] = summary_text
    state["current_step"] = "confirm_summary"
    state["reply"] = summary_text
    return state


def step_save_to_database(state: IntakeState, db: Session) -> IntakeState:
    """Writes confirmed data to database using Phase 1 models."""
    fam_data = state["family_data"]
    user_id_val = state.get("user_id")
    family = Family(
        composition_type=fam_data["composition_type"],
        district=fam_data["district"],
        taluk=fam_data["taluk"],
        address=fam_data["address"],
        ration_card_type=fam_data["ration_card_type"],
        total_household_income=fam_data["total_household_income"],
        user_id=user_id_val,
        created_by=user_id_val,
    )
    db.add(family)
    db.flush()


    saved_person_ids = []
    for p_data in state["persons_data"]:
        person = Person(
            family_id=family.id,
            name=p_data["name"],
            age=p_data["age"],
            gender=p_data["gender"],
            education_level=p_data["education_level"],
            occupation=p_data["occupation"],
            occupation_detail=p_data.get("occupation_detail"),
            marital_status=p_data["marital_status"],
            caste_category=p_data["caste_category"],
            disability_status=p_data["disability_status"],
            disability_type=p_data.get("disability_type"),
            special_flags=p_data.get("special_flags", []),
            land_holding_acres=p_data.get("land_holding_acres", 0.0),
            crop_type=p_data.get("crop_type"),
        )
        db.add(person)
        db.flush()
        saved_person_ids.append(str(person.id))

    db.commit()

    state["saved_family_id"] = str(family.id)
    state["saved_person_ids"] = saved_person_ids
    state["is_completed"] = True
    state["current_step"] = "saved"
    state["reply"] = (
        f"✅ **தங்கள் குடும்ப விவரங்கள் வெற்றிகரமாக பதிவு செய்யப்பட்டன!**\n\n"
        f"- குடும்ப அடையாள எண் (Family ID): `{family.id}`\n"
        f"- பதிவு செய்யப்பட்ட உறுப்பினர்கள்: {len(saved_person_ids)} நபர்\n\n"
        f"தங்களுக்குரிய தமிழ்நாடு அரசு நலத்திட்டங்களை இப்போது கண்டறியலாம்."
    )
    return state
