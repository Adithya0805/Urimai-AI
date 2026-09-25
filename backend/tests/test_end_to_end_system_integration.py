import uuid
from fastapi.testclient import TestClient
from fastapi import status


def test_complete_new_user_end_to_end_journey(client: TestClient):
    """Full End-to-End User Journey:
    1. Citizen logs in via Phone OTP (+91 94441 23456)
    2. Sets up family in Thanjavur (Paddy farming household)
    3. Adds Father (Farmer, 48) and Daughter (12th Std Student, 17)
    4. Evaluates Family & Individual Eligibility across Agriculture & Education
    5. Retrieves Tamil Guidance Action Plan for Father's scheme
    6. Starts application tracking with pending documents
    7. Tracks application status lifecycle
    """
    phone = "+919444123456"

    # 1. Login via OTP
    send_res = client.post("/auth/phone/send-otp", json={"phone": phone})
    assert send_res.status_code == status.HTTP_200_OK

    verify_res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert verify_res.status_code == status.HTTP_200_OK
    auth_data = verify_res.json()
    token = auth_data["access_token"]
    user_id = auth_data["user"]["id"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Family
    fam_payload = {
        "composition_type": "nuclear",
        "district": "Thanjavur",
        "taluk": "Papanasam",
        "address": "14, West Street, Ganapathi Agraharam",
        "ration_card_type": "green",
        "total_household_income": 9500.0,
    }
    fam_res = client.post("/families", json=fam_payload, headers=headers)
    assert fam_res.status_code == status.HTTP_201_CREATED
    fam_data = fam_res.json()
    family_id = fam_data["id"]
    assert fam_data["user_id"] == user_id

    # 3. Add Member 1: Father (Farmer)
    father_payload = {
        "name": "முருகேசன் (Murugesan)",
        "age": 48,
        "gender": "male",
        "education_level": "primary",
        "occupation": "farmer",
        "marital_status": "married",
        "caste_category": "BC",
        "disability_status": False,
        "special_flags": [],
        "land_holding_acres": 2.0,
        "crop_type": "paddy",
    }
    father_res = client.post(f"/families/{family_id}/persons", json=father_payload, headers=headers)
    assert father_res.status_code == status.HTTP_201_CREATED
    father_id = father_res.json()["id"]

    # Add Member 2: Daughter (Student)
    daughter_payload = {
        "name": "கனிமொழி (Kanimozhi)",
        "age": 17,
        "gender": "female",
        "education_level": "higher_secondary",
        "occupation": "student",
        "marital_status": "single",
        "caste_category": "BC",
        "disability_status": False,
        "special_flags": [],
    }
    daughter_res = client.post(f"/families/{family_id}/persons", json=daughter_payload, headers=headers)
    assert daughter_res.status_code == status.HTTP_201_CREATED
    daughter_id = daughter_res.json()["id"]

    # 4. Evaluate Multi-Member Family Eligibility
    fam_elig_res = client.get(f"/families/{family_id}/eligibility", headers=headers)
    assert fam_elig_res.status_code == status.HTTP_200_OK
    fam_elig = fam_elig_res.json()
    assert fam_elig["total_persons"] == 2
    assert len(fam_elig["persons_eligibility"]) == 2

    # 5. Evaluate Father Guidance Plan
    father_guide_res = client.get(f"/persons/{father_id}/guidance", headers=headers)
    assert father_guide_res.status_code == status.HTTP_200_OK
    father_guide = father_guide_res.json()
    assert father_guide["eligible_schemes_count"] >= 1
    selected_scheme = father_guide["eligible_schemes_guidance"][0]
    scheme_id = selected_scheme["scheme_id"]

    assert len(selected_scheme["required_documents"]) >= 1
    assert len(selected_scheme["steps_tamil"]) >= 1

    # 6. Start Application Tracking for Father's scheme
    track_res = client.post(
        "/applications",
        json={
            "person_id": father_id,
            "scheme_id": scheme_id,
            "status": "documents_pending",
            "pending_documents": ["பட்டா / சிட்டா நகல் (Patta / Chitta)", "வங்கி கணக்கு புத்தகம்"],
            "next_action_note": "வேளாண்மை உதவி இயக்குநர் அலுவலகத்தில் ஆவணங்களை சமர்ப்பிக்கவும்",
        },
        headers=headers,
    )
    assert track_res.status_code == status.HTTP_201_CREATED
    app_id = track_res.json()["id"]

    # 7. Check Application Status via /tracker
    user_apps_res = client.get(f"/persons/{father_id}/applications", headers=headers)
    assert user_apps_res.status_code == status.HTTP_200_OK
    assert len(user_apps_res.json()) >= 1
    assert user_apps_res.json()[0]["id"] == app_id


def test_returning_user_session_and_resume_journey(client: TestClient):
    """Test returning citizen journey:
    1. User logs in with existing phone
    2. /auth/me returns existing family IDs
    3. User resumes mid-way intake without re-entering prior questions
    """
    phone = "+919444123456"

    # 1. Login
    send_res = client.post("/auth/phone/send-otp", json={"phone": phone})
    assert send_res.status_code == status.HTTP_200_OK

    login_res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert login_res.status_code == status.HTTP_200_OK
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Pre-create a family linked to user in this isolated test session
    client.post(
        "/families",
        json={
            "composition_type": "nuclear",
            "district": "Madurai",
            "taluk": "Madurai North",
            "address": "10, Main Road",
            "ration_card_type": "green",
            "total_household_income": 12000.0,
        },
        headers=headers,
    )

    # 2. Check /auth/me profile
    me_res = client.get("/auth/me", headers=headers)
    assert me_res.status_code == status.HTTP_200_OK
    me_data = me_res.json()
    assert len(me_data["family_ids"]) >= 1

    # 3. Start a new intake, answer 2 steps
    session_id = f"session_e2e_{uuid.uuid4().hex[:6]}"
    r1 = client.post(
        "/intake/message",
        json={"session_id": session_id, "message": "வணக்கம்"},
        headers=headers,
    )
    assert r1.status_code == status.HTTP_200_OK

    r2 = client.post(
        "/intake/message",
        json={"session_id": session_id, "message": "தனி நபர்"},
        headers=headers,
    )
    assert r2.status_code == status.HTTP_200_OK

    # 4. Resume where left off
    resume_res = client.get("/intake/resume", headers=headers)
    assert resume_res.status_code == status.HTTP_200_OK
    resume_data = resume_res.json()
    assert resume_data["session_id"] == session_id
    assert resume_data["current_step"] == "family_district"


def test_backend_health_check_response(client: TestClient):
    """Confirm backend health check returns 200 with service identifier."""
    res = client.get("/health")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data["status"] == "healthy"
    assert data["service"] == "urimai-ai-backend"
