import uuid
import datetime
from fastapi.testclient import TestClient
from fastapi import status
from app.models.enums import ApplicationTrackingStatus
from app.models.scheme import Scheme, EligibilityRule
from app.models.application_status import ApplicationStatus, SchemeReviewQueue, NotificationLog
from app.services.freshness_pipeline import run_freshness_check, get_freshness_review_queue


def get_admin_headers(client: TestClient) -> dict:
    res = client.post(
        "/auth/admin/login",
        json={"email": "admin@urimai.tn.gov.in", "password": "Admin@Urimai2026!"},
    )
    assert res.status_code == status.HTTP_200_OK
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def create_family_and_person(client: TestClient):
    fam_res = client.post(
        "/families",
        json={
            "composition_type": "nuclear",
            "district": "Madurai",
            "taluk": "Madurai North",
            "address": "12, Sellur Road",
            "ration_card_type": "green",
            "total_household_income": 8000.0,
        },
    )
    assert fam_res.status_code == status.HTTP_201_CREATED
    family_id = fam_res.json()["id"]

    person_res = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "மீனாட்சி",
            "age": 62,
            "gender": "female",
            "education_level": "none",
            "occupation": "unemployed",
            "marital_status": "widowed",
            "caste_category": "BC",
            "disability_status": False,
            "special_flags": ["destitute"],
        },
    )
    assert person_res.status_code == status.HTTP_201_CREATED
    person_id = person_res.json()["id"]
    return family_id, person_id


def get_sample_scheme(client: TestClient):
    schemes_res = client.get("/schemes?category=pension")
    assert schemes_res.status_code == status.HTTP_200_OK
    schemes = schemes_res.json()
    assert len(schemes) > 0
    return schemes[0]


def test_create_and_update_application_tracking(client: TestClient):
    """Test creating an application tracking record and updating its status lifecycle."""
    _, person_id = create_family_and_person(client)
    scheme = get_sample_scheme(client)
    scheme_id = scheme["id"]

    # 1. Create tracking record in DOCUMENTS_PENDING status
    payload = {
        "person_id": person_id,
        "scheme_id": scheme_id,
        "status": "documents_pending",
        "pending_documents": ["வருமானச் சான்றிதழ்", "ஆதார் அட்டை நகல்"],
        "next_action_note": "Submit income proof at Taluk office",
    }
    create_res = client.post("/applications", json=payload)
    assert create_res.status_code == status.HTTP_201_CREATED
    app_data = create_res.json()
    app_id = app_data["id"]

    assert app_data["status"] == "documents_pending"
    assert app_data["person_id"] == person_id
    assert app_data["scheme_id"] == scheme_id
    assert len(app_data["pending_documents"]) == 2
    assert app_data["person_name"] == "மீனாட்சி"

    # 2. Fetch by ID
    get_res = client.get(f"/applications/{app_id}")
    assert get_res.status_code == status.HTTP_200_OK
    assert get_res.json()["id"] == app_id

    # 3. Update status to SUBMITTED
    patch_res = client.patch(
        f"/applications/{app_id}",
        json={
            "status": "submitted",
            "pending_documents": [],
            "next_action_note": "Application submitted at e-Sevai centre, acknowledgement received.",
        },
    )
    assert patch_res.status_code == status.HTTP_200_OK
    updated_data = patch_res.json()
    assert updated_data["status"] == "submitted"
    assert updated_data["pending_documents"] == []

    # 4. List all applications for the person
    list_res = client.get(f"/persons/{person_id}/applications")
    assert list_res.status_code == status.HTTP_200_OK
    apps_list = list_res.json()
    assert len(apps_list) >= 1
    assert apps_list[0]["id"] == app_id


def test_freshness_pipeline_flags_stale_schemes_without_rule_tampering(client: TestClient, db_session):
    """Test that schemes with last_verified_date older than threshold are flagged into the
    SchemeReviewQueue, while strictly guaranteeing NO automated modifications to eligibility rules.
    """
    # 1. Artificially make a scheme stale (verified 250 days ago)
    stale_date = datetime.date.today() - datetime.timedelta(days=250)
    scheme = db_session.query(Scheme).filter(Scheme.scheme_code == "TN-SW-OAP").first()
    assert scheme is not None
    scheme.last_verified_date = stale_date
    db_session.commit()

    # Record rule count before check
    rule_count_before = db_session.query(EligibilityRule).filter(EligibilityRule.scheme_id == scheme.id).count()
    rules_before = [
        (r.field_name, r.operator.value if hasattr(r.operator, 'value') else r.operator, r.value)
        for r in db_session.query(EligibilityRule).filter(EligibilityRule.scheme_id == scheme.id).all()
    ]

    # 2. Trigger Freshness Scan via Admin API (threshold = 180 days)
    admin_headers = get_admin_headers(client)
    scan_res = client.post("/admin/freshness/run-check?threshold_days=180", headers=admin_headers)
    assert scan_res.status_code == status.HTTP_200_OK
    scan_data = scan_res.json()
    assert scan_data["stale_schemes_flagged"] >= 1

    # 3. Verify Scheme is in Review Queue
    queue_res = client.get("/admin/freshness/review-queue", headers=admin_headers)
    assert queue_res.status_code == status.HTTP_200_OK
    queue_items = queue_res.json()
    assert any(item["scheme_code"] == "TN-SW-OAP" for item in queue_items)

    oap_item = next(item for item in queue_items if item["scheme_code"] == "TN-SW-OAP")
    assert "250 நாட்களுக்கு முன்பு" in oap_item["flagged_reason"] or "180" in oap_item["flagged_reason"]
    assert oap_item["status"] == "pending_human_review"

    # 4. CRITICAL FIREWALL CHECK: Verify NO automated rule changes occurred
    rule_count_after = db_session.query(EligibilityRule).filter(EligibilityRule.scheme_id == scheme.id).count()
    rules_after = [
        (r.field_name, r.operator.value if hasattr(r.operator, 'value') else r.operator, r.value)
        for r in db_session.query(EligibilityRule).filter(EligibilityRule.scheme_id == scheme.id).all()
    ]
    assert rule_count_before == rule_count_after, "Rule count must not be altered by automated checks!"
    assert rules_before == rules_after, "Rule criteria must remain identical without human admin sign-off!"

    # 5. Admin signs off and verifies the scheme
    review_id = oap_item["id"]
    verify_res = client.post(
        f"/admin/freshness/verify/{review_id}",
        json={
            "reviewer_notes": "Official gazette confirmed G.O. Ms. No. 45 criteria unchanged for 2026.",
            "update_verified_date": True,
        },
        headers=admin_headers,
    )
    assert verify_res.status_code == status.HTTP_200_OK
    verified_data = verify_res.json()
    assert verified_data["status"] == "reviewed_verified"
    assert verified_data["reviewer_notes"] == "Official gazette confirmed G.O. Ms. No. 45 criteria unchanged for 2026."

    # Verify scheme.last_verified_date is now today
    db_session.refresh(scheme)
    assert scheme.last_verified_date == datetime.date.today()


def test_followup_agent_generates_tamil_reminders_for_pending_documents(client: TestClient, db_session):
    """Test that the follow-up agent detects applications stuck in documents_pending
    for >= 7 days and generates structured Tamil reminder notifications listing the exact missing documents.
    """
    _, person_id = create_family_and_person(client)
    scheme = get_sample_scheme(client)
    scheme_id = scheme["id"]
    admin_headers = get_admin_headers(client)

    # Create an application backdated 10 days ago with status = documents_pending
    past_date = datetime.date.today() - datetime.timedelta(days=10)
    app = ApplicationStatus(
        person_id=uuid.UUID(person_id),
        scheme_id=uuid.UUID(scheme_id),
        status=ApplicationTrackingStatus.DOCUMENTS_PENDING,
        last_updated=past_date,
        pending_documents=["ஆதார் அட்டை", "வாழ்வாதார சான்றிதழ்"],
        next_action_note="Pending citizen submission",
    )
    db_session.add(app)
    db_session.commit()
    db_session.refresh(app)

    # 1. Check pending followups admin endpoint
    pending_res = client.get("/admin/applications/pending-followups?days_pending=7", headers=admin_headers)
    assert pending_res.status_code == status.HTTP_200_OK
    pending_apps = pending_res.json()
    assert any(a["id"] == str(app.id) for a in pending_apps)

    # 2. Trigger follow-up agent cycle
    trigger_res = client.post("/admin/applications/trigger-followups?pending_days_threshold=7", headers=admin_headers)
    assert trigger_res.status_code == status.HTTP_200_OK
    scan_result = trigger_res.json()
    assert scan_result["documents_pending_reminders_generated"] >= 1
    assert scan_result["notifications_created"] >= 1

    # 3. Verify notification log contains structured Tamil message
    notifs_res = client.get("/admin/notifications", headers=admin_headers)
    assert notifs_res.status_code == status.HTTP_200_OK
    notifs = notifs_res.json()
    app_notif = next((n for n in notifs if n["application_id"] == str(app.id)), None)

    assert app_notif is not None
    assert app_notif["notification_type"] == "documents_pending_reminder"
    assert "மீனாட்சி" in app_notif["message_tamil"]
    assert "ஆதார் அட்டை" in app_notif["message_tamil"]
    assert "வாழ்வாதார சான்றிதழ்" in app_notif["message_tamil"]
    assert "10 நாட்களாக நிலுவையில்" in app_notif["message_tamil"]


def test_followup_agent_generates_renewal_due_reminders(client: TestClient, db_session):
    """Test that applications approaching renewal_due_date generate Tamil renewal reminders."""
    _, person_id = create_family_and_person(client)
    scheme = get_sample_scheme(client)
    scheme_id = scheme["id"]
    admin_headers = get_admin_headers(client)

    # Create an approved application with renewal due in 15 days
    renewal_date = datetime.date.today() + datetime.timedelta(days=15)
    app = ApplicationStatus(
        person_id=uuid.UUID(person_id),
        scheme_id=uuid.UUID(scheme_id),
        status=ApplicationTrackingStatus.APPROVED,
        last_updated=datetime.date.today(),
        renewal_due_date=renewal_date,
        next_action_note="Annual renewal required",
    )
    db_session.add(app)
    db_session.commit()
    db_session.refresh(app)

    # Trigger follow-up agent with 30-day renewal window
    trigger_res = client.post("/admin/applications/trigger-followups?renewal_window_days=30", headers=admin_headers)
    assert trigger_res.status_code == status.HTTP_200_OK
    scan_result = trigger_res.json()
    assert scan_result["renewal_reminders_generated"] >= 1

    # Verify status changed to renewal_due and notification created
    db_session.refresh(app)
    assert app.status == ApplicationTrackingStatus.RENEWAL_DUE

    notifs_res = client.get("/admin/notifications", headers=admin_headers)
    assert notifs_res.status_code == status.HTTP_200_OK
    renewal_notif = next(
        (n for n in notifs_res.json() if n["application_id"] == str(app.id) and n["notification_type"] == "renewal_due_reminder"),
        None,
    )
    assert renewal_notif is not None
    assert "வருடாந்திர புதுப்பித்தல் (Renewal)" in renewal_notif["message_tamil"]
    assert renewal_date.strftime("%d-%m-%Y") in renewal_notif["message_tamil"]
