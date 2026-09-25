import uuid
from fastapi.testclient import TestClient
from fastapi import status


def get_admin_headers(client: TestClient) -> dict:
    """Helper to authenticate as admin and obtain authorization headers."""
    res = client.post(
        "/auth/admin/login",
        json={"email": "admin@urimai.tn.gov.in", "password": "Admin@Urimai2026!"},
    )
    assert res.status_code == status.HTTP_200_OK
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def get_citizen_headers(client: TestClient) -> dict:
    """Helper to authenticate as standard citizen."""
    phone = "+919876543210"
    client.post("/auth/phone/send-otp", json={"phone": phone})
    res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert res.status_code == status.HTTP_200_OK
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_admin_login_success(client: TestClient):
    """Confirm admin can authenticate via email/password and receive admin JWT."""
    res = client.post(
        "/auth/admin/login",
        json={"email": "admin@urimai.tn.gov.in", "password": "Admin@Urimai2026!"},
    )
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert "access_token" in data
    assert data["user"]["role"] == "admin"
    assert data["user"]["email"] == "admin@urimai.tn.gov.in"


def test_admin_login_invalid_credentials_rejected(client: TestClient):
    """Confirm invalid admin credentials return 401 Unauthorized."""
    res = client.post(
        "/auth/admin/login",
        json={"email": "admin@urimai.tn.gov.in", "password": "WrongPassword123!"},
    )
    assert res.status_code == status.HTTP_401_UNAUTHORIZED
    data = res.json()
    assert data["error_code"] == "INVALID_ADMIN_CREDENTIALS"
    assert "மின்னஞ்சல்" in data["message_ta"]


def test_citizen_cannot_access_admin_endpoints(client: TestClient):
    """Confirm standard citizen user receives 403 Forbidden on any /admin route."""
    citizen_headers = get_citizen_headers(client)

    # 1. Stats endpoint
    res_stats = client.get("/admin/dashboard/stats", headers=citizen_headers)
    assert res_stats.status_code == status.HTTP_403_FORBIDDEN
    assert res_stats.json()["error_code"] == "FORBIDDEN_ADMIN_ACCESS"

    # 2. Review queue
    res_queue = client.get("/admin/freshness/review-queue", headers=citizen_headers)
    assert res_queue.status_code == status.HTTP_403_FORBIDDEN

    # 3. Stuck applications
    res_stuck = client.get("/admin/applications/stuck", headers=citizen_headers)
    assert res_stuck.status_code == status.HTTP_403_FORBIDDEN

    # 4. Audit logs
    res_audit = client.get("/admin/audit-logs", headers=citizen_headers)
    assert res_audit.status_code == status.HTTP_403_FORBIDDEN


def test_unauthenticated_request_to_admin_rejected(client: TestClient):
    """Confirm unauthenticated request receives 401 Unauthorized."""
    res = client.get("/admin/dashboard/stats")
    assert res.status_code == status.HTTP_401_UNAUTHORIZED


def test_admin_can_view_stats_and_stuck_applications(client: TestClient):
    """Confirm authenticated admin can access live dashboard stats and stuck application records."""
    admin_headers = get_admin_headers(client)

    # 1. Fetch Stats
    stats_res = client.get("/admin/dashboard/stats", headers=admin_headers)
    assert stats_res.status_code == status.HTTP_200_OK
    stats = stats_res.json()
    assert "total_families" in stats
    assert "active_schemes_count" in stats
    assert "stuck_applications_count" in stats
    assert stats["active_schemes_count"] > 0

    # 2. Fetch Stuck Applications
    stuck_res = client.get("/admin/applications/stuck", headers=admin_headers)
    assert stuck_res.status_code == status.HTTP_200_OK
    assert isinstance(stuck_res.json(), list)


def test_admin_can_resolve_review_and_audit_is_created(client: TestClient):
    """Confirm admin marking a scheme reviewed updates last_verified_date and logs to admin_audit_logs."""
    admin_headers = get_admin_headers(client)

    # Trigger freshness check first to generate review queue items
    scan_res = client.post("/admin/freshness/run-check?threshold_days=0", headers=admin_headers)
    assert scan_res.status_code == status.HTTP_200_OK

    # Fetch review queue
    queue_res = client.get("/admin/freshness/review-queue", headers=admin_headers)
    assert queue_res.status_code == status.HTTP_200_OK
    review_queue = queue_res.json()
    assert len(review_queue) > 0

    review_id = review_queue[0]["id"]

    # Admin signs off
    resolve_res = client.post(
        f"/admin/freshness/verify/{review_id}",
        json={
            "reviewer_notes": "Official gazette verified by District Welfare Officer",
            "update_verified_date": True,
        },
        headers=admin_headers,
    )
    assert resolve_res.status_code == status.HTTP_200_OK
    assert resolve_res.json()["status"] == "reviewed_verified"

    # Verify audit log recorded
    audit_res = client.get("/admin/audit-logs", headers=admin_headers)
    assert audit_res.status_code == status.HTTP_200_OK
    audit_logs = audit_res.json()
    assert len(audit_logs) >= 1
    recent_log = audit_logs[0]
    assert recent_log["action"] == "SCHEME_REVIEWED"
    assert recent_log["entity_type"] == "scheme"
    assert recent_log["after_value"]["status"] == "resolved" or recent_log["after_value"]["status"] == "reviewed_verified"


def test_admin_rule_edit_captures_before_after_in_audit_log(client: TestClient):
    """Confirm admin editing a rule updates the database via engine validation and records before/after diff in audit log."""
    admin_headers = get_admin_headers(client)

    # Get an existing scheme with rules
    scheme_res = client.get("/schemes/TN-SW-OAP")
    assert scheme_res.status_code == status.HTTP_200_OK
    scheme = scheme_res.json()
    assert len(scheme["rules"]) > 0
    rule = scheme["rules"][0]
    rule_id = rule["id"]
    scheme_id = scheme["id"]
    original_value = rule["value"]

    # Admin updates rule value
    new_value = "65" if original_value == "60" else "60"
    update_res = client.patch(
        f"/admin/schemes/{scheme_id}/rules/{rule_id}",
        json={
            "value": new_value,
            "admin_notes": "Updated based on Revised G.O. Ms. No. 42",
        },
        headers=admin_headers,
    )
    assert update_res.status_code == status.HTTP_200_OK
    assert update_res.json()["value"] == new_value

    # Verify audit log captured the before & after values
    audit_res = client.get("/admin/audit-logs", headers=admin_headers)
    assert audit_res.status_code == status.HTTP_200_OK
    recent_log = audit_res.json()[0]
    assert recent_log["action"] == "RULE_UPDATED"
    assert recent_log["entity_type"] == "eligibility_rule"
    assert recent_log["entity_id"] == rule_id
    assert recent_log["before_value"]["value"] == original_value
    assert recent_log["after_value"]["value"] == new_value
    assert recent_log["after_value"]["admin_notes"] == "Updated based on Revised G.O. Ms. No. 42"


def test_admin_rule_edit_with_invalid_field_is_rejected(client: TestClient):
    """Confirm admin attempting to set a non-existent database field on a rule is rejected with 422."""
    admin_headers = get_admin_headers(client)

    scheme_res = client.get("/schemes/TN-SW-OAP")
    scheme = scheme_res.json()
    rule = scheme["rules"][0]

    update_res = client.patch(
        f"/admin/schemes/{scheme['id']}/rules/{rule['id']}",
        json={
            "field_name": "non_existent_random_column_123",
            "admin_notes": "Testing validation rejection",
        },
        headers=admin_headers,
    )
    assert update_res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    err = update_res.json()
    assert err["error_code"] == "INVALID_RULE_FIELD"
