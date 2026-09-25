"""End-to-End Test Suite with Throttled Network & Jitter Simulation
===================================================================
Tests the full citizen journey (OTP login -> Family -> Members -> Eligibility -> Guidance -> Tracking)
with synthetic latency (simulating patchy rural 2G/3G connections in Tamil Nadu).
"""

import os
import time
import pytest
import httpx
from fastapi.testclient import TestClient

BASE_URL = os.getenv("TEST_BASE_URL", "").rstrip("/")


def simulate_network_throttle(delay_seconds: float = 0.05):
    """Simulate mobile network packet latency."""
    time.sleep(delay_seconds)


def test_throttled_full_citizen_journey(client: TestClient):
    """Executes the full user lifecycle under throttled network conditions."""
    phone = "+919876543210"

    # 1. Phone OTP Request with throttle
    simulate_network_throttle(0.05)
    if BASE_URL:
        resp = httpx.post(f"{BASE_URL}/auth/phone/send-otp", json={"phone": phone}, timeout=15.0)
    else:
        resp = client.post("/auth/phone/send-otp", json={"phone": phone})
    assert resp.status_code == 200

    # 2. Verify OTP
    simulate_network_throttle(0.05)
    if BASE_URL:
        resp = httpx.post(f"{BASE_URL}/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"}, timeout=15.0)
    else:
        resp = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert resp.status_code == 200
    token = resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Create Family
    simulate_network_throttle(0.05)
    fam_payload = {
        "composition_type": "nuclear",
        "district": "Madurai",
        "taluk": "Melur",
        "address": "22, Main Road, Melur",
        "ration_card_type": "phh_aay",
        "total_household_income": 4500.0,
    }
    if BASE_URL:
        resp = httpx.post(f"{BASE_URL}/families", json=fam_payload, headers=headers, timeout=15.0)
    else:
        resp = client.post("/families", json=fam_payload, headers=headers)
    assert resp.status_code == 201
    family_id = resp.json()["id"]

    # 4. Add Person (Elderly Mother, 68)
    simulate_network_throttle(0.05)
    person_payload = {
        "name": "மீனாட்சி அம்மாள் (Meenakshi Ammal)",
        "age": 68,
        "gender": "female",
        "education_level": "none",
        "occupation": "homemaker",
        "marital_status": "widowed",
        "caste_category": "MBC",
        "disability_status": False,
        "special_flags": ["destitute", "widow"],
    }
    if BASE_URL:
        resp = httpx.post(f"{BASE_URL}/families/{family_id}/persons", json=person_payload, headers=headers, timeout=15.0)
    else:
        resp = client.post(f"/families/{family_id}/persons", json=person_payload, headers=headers)
    assert resp.status_code == 201
    person_id = resp.json()["id"]

    # 5. Evaluate Eligibility
    simulate_network_throttle(0.05)
    if BASE_URL:
        resp = httpx.get(f"{BASE_URL}/persons/{person_id}/eligibility", headers=headers, timeout=15.0)
    else:
        resp = client.get(f"/persons/{person_id}/eligibility", headers=headers)
    assert resp.status_code == 200
    elig_data = resp.json()
    assert len(elig_data["eligible_schemes"]) >= 1

    # 6. Retrieve Guidance Action Plan in Tamil
    simulate_network_throttle(0.05)
    if BASE_URL:
        resp = httpx.get(f"{BASE_URL}/persons/{person_id}/guidance", headers=headers, timeout=15.0)
    else:
        resp = client.get(f"/persons/{person_id}/guidance", headers=headers)
    assert resp.status_code == 200
    guide_data = resp.json()
    assert guide_data["eligible_schemes_count"] >= 1
    first_scheme = guide_data["eligible_schemes_guidance"][0]
    assert len(first_scheme["steps_tamil"]) > 0
    assert len(first_scheme["required_documents"]) > 0

    # 7. Start Application Tracking
    simulate_network_throttle(0.05)
    app_payload = {
        "person_id": person_id,
        "scheme_id": first_scheme["scheme_id"],
        "status": "documents_pending",
        "pending_documents": first_scheme["required_documents"],
        "next_action_note": "குடும்ப அட்டை நகல் சமர்ப்பிக்கப்பட வேண்டும்",
    }
    if BASE_URL:
        resp = httpx.post(f"{BASE_URL}/applications", json=app_payload, headers=headers, timeout=15.0)
    else:
        resp = client.post("/applications", json=app_payload, headers=headers)
    assert resp.status_code == 201
    app_data = resp.json()
    assert app_data["status"] == "documents_pending"
