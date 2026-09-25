import uuid
from fastapi import status


def test_intake_full_conversation_flow_persists_to_database(client):
    """Test complete Tamil conversational flow end-to-end and verify DB persistence."""
    session_id = f"test_session_{uuid.uuid4().hex[:8]}"

    def send(msg):
        res = client.post("/intake/message", json={"session_id": session_id, "message": msg})
        assert res.status_code == status.HTTP_200_OK
        return res.json()

    # 1. Greet
    r = send("வணக்கம்")
    assert "குடும்ப அமைப்பை குறிப்பிடவும்" in r["reply"]

    # 2. Family Composition
    r = send("அணு குடும்பம்")
    assert "மாவட்டம்" in r["reply"]

    # 3. District
    r = send("மதுரை")
    assert "வட்டம்" in r["reply"]

    # 4. Taluk
    r = send("மதுரை வடக்கு")
    assert "முகவரி" in r["reply"]

    # 5. Address
    r = send("15, தெற்கு மாசி வீதி, மதுரை")
    assert "குடும்ப அட்டை" in r["reply"]

    # 6. Ration Card
    r = send("பச்சை அரிசி அட்டை")
    assert "வருமானம்" in r["reply"]

    # 7. Household Income
    r = send("ரூபாய் 8000")
    assert "நபர்களின்" in r["reply"]



    # 8. Person Count (1 person)
    r = send("1 நபர்")
    assert "முழு பெயர்" in r["reply"]

    # 9. Person Name
    r = send("மீனாட்சி")
    assert "வயது என்ன" in r["reply"]

    # 10. Person Age
    r = send("62 வயது")
    assert "பாலினம்" in r["reply"]

    # 11. Person Gender
    r = send("பெண்")
    assert "கல்வித் தகுதி" in r["reply"]

    # 12. Education Level
    r = send("படிக்கவில்லை")
    assert "தொழில் என்ன" in r["reply"]

    # 13. Occupation
    r = send("வேலையில்லை")
    assert "திருமண நிலை" in r["reply"]

    # 14. Marital Status
    r = send("விதவை, கணவர் இறந்துவிட்டார்")
    assert "சமூகப் பிரிவு" in r["reply"]

    # 15. Caste Category
    r = send("BC பிற்படுத்தப்பட்டோர்")
    assert "மாற்றுத்திறனாளி நிலை" in r["reply"]

    # 16. Disability Status (No -> skips disability type)
    r = send("இல்லை")
    assert "சிறப்பு பிரிவுகள்" in r["reply"]

    # 17. Special Flags
    r = send("ஆதரவற்ற விதவை")
    # Should display summary
    assert "பதிவு செய்யப்பட்ட விவரங்களின் சுருக்கம்" in r["reply"]
    assert "மீனாட்சி" in r["reply"]
    assert "62" in r["reply"]
    assert "BC" in r["reply"]
    assert r["current_step"] == "confirm_summary"
    assert not r["is_completed"]

    # 18. Confirmation
    r = send("ஆம், விவரங்கள் சரி")
    assert r["is_completed"] is True
    assert "வெற்றிகரமாக பதிவு செய்யப்பட்டன" in r["reply"]
    assert r["saved_family_id"] is not None

    saved_family_id = r["saved_family_id"]
    saved_person_ids = r["saved_person_ids"]
    assert len(saved_person_ids) == 1

    # Verify via Phase 1 endpoint: GET /families/{id}
    fam_res = client.get(f"/families/{saved_family_id}")
    assert fam_res.status_code == status.HTTP_200_OK
    fam_data = fam_res.json()
    assert fam_data["district"] == "மதுரை"
    assert fam_data["ration_card_type"] == "green"
    assert len(fam_data["persons"]) == 1
    p_data = fam_data["persons"][0]
    assert p_data["name"] == "மீனாட்சி"
    assert p_data["age"] == 62
    assert p_data["gender"] == "female"
    assert p_data["marital_status"] == "widowed"
    assert "destitute" in p_data["special_flags"]

    # Verify via Phase 3 endpoint: GET /families/{id}/eligibility
    elig_res = client.get(f"/families/{saved_family_id}/eligibility")
    assert elig_res.status_code == status.HTTP_200_OK
    elig_data = elig_res.json()
    p_elig = elig_data["persons_eligibility"][0]
    eligible_schemes = [s["scheme_code"] for s in p_elig["eligible_schemes"]]
    assert "TN-SW-OAP" in eligible_schemes
    assert "TN-SW-DWP" in eligible_schemes


def test_intake_validation_and_clarification_on_invalid_enum(client):
    """When an invalid or unrecognized value is submitted, ask clarifying question."""
    session_id = f"test_session_{uuid.uuid4().hex[:8]}"

    # Greet
    client.post("/intake/message", json={"session_id": session_id, "message": "தொடங்கு"})

    # Send gibberish composition
    res = client.post("/intake/message", json={"session_id": session_id, "message": "ஏலியன் குடும்பம்"})
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    # Must ask polite clarification with choices
    assert "தங்கள் குடும்ப அமைப்பை தயவுசெய்து குறிப்பிடவும்" in data["reply"]
    assert "தனி நபர்" in data["reply"]


def test_intake_mid_conversation_correction(client):
    """User updates a field at the summary stage."""
    session_id = f"test_session_{uuid.uuid4().hex[:8]}"

    def send(msg):
        return client.post("/intake/message", json={"session_id": session_id, "message": msg}).json()

    send("தொடங்கு")
    send("தனி நபர்")
    send("சென்னை")
    send("மைலாப்பூர்")
    send("10, பாரதி சாலை")
    send("வெள்ளை அட்டை")
    send("10000")
    send("1")
    send("கண்ணன்")
    send("45")
    send("ஆண்")
    send("பட்டதாரி")
    send("சுயதொழில்")
    send("திருமணமானவர்")
    send("General")
    send("இல்லை")
    summary = send("எதுவுமில்லை")
    assert "வயது: 45" in summary["reply"]

    # User corrects age to 55
    corrected = send("வயது 55")
    assert "வயது: 55" in corrected["reply"]


def test_intake_adaptive_disability_flow(client):
    """When disability is 'ஆம்', agent asks for disability type."""
    session_id = f"test_session_{uuid.uuid4().hex[:8]}"

    def send(msg):
        return client.post("/intake/message", json={"session_id": session_id, "message": msg}).json()

    send("தொடங்கு")
    send("தனி நபர்")
    send("சேலம்")
    send("சேலம் தெற்கு")
    send("காந்தி நகர்")
    send("பச்சை அட்டை")
    send("6000")
    send("1")
    send("ரமேஷ்")
    send("30")
    send("ஆண்")
    send("பத்தாம் வகுப்பு")
    send("தினக்கூலி")
    send("திருமணமாகாதவர்")
    send("SC")
    # Answer YES to disability
    r_dis = send("ஆம், மாற்றுத்திறனாளி")
    # Must ask disability type
    assert "மாற்றுத்திறன் வகையை குறிப்பிடவும்" in r_dis["reply"]


def test_intake_extraction_audit_logs(client):
    """Verify extraction audit logs are recorded."""
    session_id = f"test_session_{uuid.uuid4().hex[:8]}"

    client.post("/intake/message", json={"session_id": session_id, "message": "தொடங்கு"})
    client.post("/intake/message", json={"session_id": session_id, "message": "கூட்டுக் குடும்பம்"})

    # Check extraction logs endpoint
    res = client.get(f"/intake/logs?session_id={session_id}")
    assert res.status_code == status.HTTP_200_OK
    logs = res.json()
    assert len(logs) >= 1
    assert any(l["target_field"] == "family.composition_type" for l in logs)


def test_intake_chat_ui_endpoint(client):
    """GET /intake/chat returns HTML page."""
    res = client.get("/intake/chat")
    assert res.status_code == status.HTTP_200_OK
    assert "text/html" in res.headers["content-type"]
    assert "உரிமை AI" in res.text
