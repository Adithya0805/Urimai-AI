import uuid
from fastapi.testclient import TestClient
from fastapi import status


def get_auth_token_for_user(client: TestClient, phone: str = "+919876543210") -> str:
    """Helper to simulate phone OTP login and obtain JWT access token."""
    client.post("/auth/phone/send-otp", json={"phone": phone})
    res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert res.status_code == status.HTTP_200_OK
    return res.json()["access_token"]


def test_phone_otp_authentication_flow(client: TestClient):
    """Test phone OTP request, verification, session cookie, and /auth/me profile."""
    phone = "+919876543210"

    # 1. Send OTP
    send_res = client.post("/auth/phone/send-otp", json={"phone": phone})
    assert send_res.status_code == status.HTTP_200_OK
    assert send_res.json()["status"] == "success"

    # 2. Verify OTP
    verify_res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert verify_res.status_code == status.HTTP_200_OK
    data = verify_res.json()
    assert "access_token" in data
    token = data["access_token"]

    # Verify cookie was set
    assert "access_token" in verify_res.cookies

    # 3. Access /auth/me with Bearer token
    me_res = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me_res.status_code == status.HTTP_200_OK
    me_data = me_res.json()
    assert me_data["phone"] == phone

    # 4. Access /auth/me with cookie
    me_cookie_res = client.get("/auth/me", cookies={"access_token": token})
    assert me_cookie_res.status_code == status.HTTP_200_OK


def test_unauthenticated_request_to_owned_family_rejected(client: TestClient):
    """Test that an unauthenticated request to an authenticated citizen's family is rejected with 401."""
    token_user_a = get_auth_token_for_user(client, phone="+919876543210")

    # User A creates family
    fam_res = client.post(
        "/families",
        json={
            "composition_type": "nuclear",
            "district": "Madurai",
            "taluk": "Madurai North",
            "address": "15, South Masi Street",
            "ration_card_type": "green",
            "total_household_income": 12000.0,
        },
        headers={"Authorization": f"Bearer {token_user_a}"},
    )
    assert fam_res.status_code == status.HTTP_201_CREATED
    family_id = fam_res.json()["id"]

    # Anonymous / unauthenticated request to User A's family must be rejected
    client.cookies.clear()
    anon_res = client.get(f"/families/{family_id}")
    assert anon_res.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Authentication required" in anon_res.json()["detail"]



def test_user_cannot_access_another_users_family_data(client: TestClient):
    """SECURITY TEST: User B attempts to access and modify User A's family using guessed UUID.
    Must be blocked with 403 Forbidden.
    """
    token_user_a = get_auth_token_for_user(client, phone="+919876543210")
    token_user_b = get_auth_token_for_user(client, phone="+919876543211")

    # 1. User A creates family and adds a person
    fam_res = client.post(
        "/families",
        json={
            "composition_type": "single",
            "district": "Chennai",
            "taluk": "Mylapore",
            "address": "45, Luz Church Road",
            "ration_card_type": "green",
            "total_household_income": 8000.0,
        },
        headers={"Authorization": f"Bearer {token_user_a}"},
    )
    assert fam_res.status_code == status.HTTP_201_CREATED
    family_a_id = fam_res.json()["id"]

    person_res = client.post(
        f"/families/{family_a_id}/persons",
        json={
            "name": "User A Citizen",
            "age": 45,
            "gender": "female",
            "education_level": "secondary",
            "occupation": "homemaker",
            "marital_status": "married",
            "caste_category": "BC",
            "disability_status": False,
            "special_flags": [],
        },
        headers={"Authorization": f"Bearer {token_user_a}"},
    )
    assert person_res.status_code == status.HTTP_201_CREATED
    person_a_id = person_res.json()["id"]

    # 2. User B tries to GET User A's family -> FORBIDDEN
    get_res = client.get(
        f"/families/{family_a_id}",
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert get_res.status_code == status.HTTP_403_FORBIDDEN
    assert "Access denied" in get_res.json()["detail"]

    # 3. User B tries to GET User A's person -> FORBIDDEN
    person_get_res = client.get(
        f"/persons/{person_a_id}",
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert person_get_res.status_code == status.HTTP_403_FORBIDDEN

    # 4. User B tries to PATCH User A's family -> FORBIDDEN
    patch_res = client.patch(
        f"/families/{family_a_id}",
        json={"district": "Malicious Change"},
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert patch_res.status_code == status.HTTP_403_FORBIDDEN

    # 5. User B tries to ADD a person to User A's family -> FORBIDDEN
    add_res = client.post(
        f"/families/{family_a_id}/persons",
        json={
            "name": "Hacker Person",
            "age": 25,
            "gender": "male",
            "education_level": "graduate",
            "occupation": "unemployed",
            "marital_status": "single",
            "caste_category": "General",
            "disability_status": False,
            "special_flags": [],
        },
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert add_res.status_code == status.HTTP_403_FORBIDDEN


def test_community_volunteer_can_manage_multiple_families(client: TestClient):
    """Test that a community volunteer account can create and manage multiple families."""
    token_volunteer = get_auth_token_for_user(client, phone="+919876543299")

    # Volunteer creates Family 1 (for an elderly widow)
    f1_res = client.post(
        "/families",
        json={
            "composition_type": "single",
            "district": "Thanjavur",
            "taluk": "Kumbakonam",
            "address": "10, Temple Street",
            "ration_card_type": "green",
            "total_household_income": 3000.0,
        },
        headers={"Authorization": f"Bearer {token_volunteer}"},
    )
    assert f1_res.status_code == status.HTTP_201_CREATED
    f1_id = f1_res.json()["id"]

    # Volunteer creates Family 2 (for a farmer household)
    f2_res = client.post(
        "/families",
        json={
            "composition_type": "nuclear",
            "district": "Thanjavur",
            "taluk": "Papanasam",
            "address": "22, Agragaram",
            "ration_card_type": "green",
            "total_household_income": 8000.0,
        },
        headers={"Authorization": f"Bearer {token_volunteer}"},
    )
    assert f2_res.status_code == status.HTTP_201_CREATED
    f2_id = f2_res.json()["id"]

    # Volunteer can list all managed families
    list_res = client.get("/families", headers={"Authorization": f"Bearer {token_volunteer}"})
    assert list_res.status_code == status.HTTP_200_OK
    managed_ids = [f["id"] for f in list_res.json()]
    assert f1_id in managed_ids
    assert f2_id in managed_ids


def test_resume_where_i_left_off_intake_flow(client: TestClient):
    """Test that an authenticated user who starts intake mid-way can resume exactly
    where they left off on returning without starting over.
    """
    token_citizen = get_auth_token_for_user(client, phone="+919876543210")
    session_id = f"session_resume_{uuid.uuid4().hex[:8]}"

    # Step 1: Citizen says "வணக்கம்"
    r1 = client.post(
        "/intake/message",
        json={"session_id": session_id, "message": "வணக்கம்"},
        headers={"Authorization": f"Bearer {token_citizen}"},
    )
    assert r1.status_code == status.HTTP_200_OK

    # Step 2: Citizen enters family composition "அணு குடும்பம்"
    r2 = client.post(
        "/intake/message",
        json={"session_id": session_id, "message": "அணு குடும்பம்"},
        headers={"Authorization": f"Bearer {token_citizen}"},
    )
    assert r2.status_code == status.HTTP_200_OK
    assert r2.json()["current_step"] == "family_district"

    # Step 3: Citizen closes browser or navigates away.
    # On return, calls GET /intake/resume with their auth token
    resume_res = client.get("/intake/resume", headers={"Authorization": f"Bearer {token_citizen}"})
    assert resume_res.status_code == status.HTTP_200_OK
    resume_data = resume_res.json()

    assert resume_data["session_id"] == session_id
    assert resume_data["current_step"] == "family_district"
    assert "மாவட்டம்" in resume_data["reply"]
    assert resume_data["is_completed"] is False
