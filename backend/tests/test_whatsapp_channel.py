"""Urimai AI — WhatsApp Channel Test Suite
===========================================
Verifies WhatsApp Business API integration, numbered quick-replies, multi-day resume detection,
cross-channel data parity, guidance chunking, opt-in consent, and proactive follow-up reminders.
"""

import uuid
from datetime import datetime, timezone, timedelta
from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy.orm import Session

from app.models.family import Family
from app.models.person import Person
from app.models.whatsapp import WhatsAppSession, WhatsAppMessageLog
from app.models.application_status import ApplicationStatus
from app.models.enums import ApplicationTrackingStatus
from app.services.followup_agent import run_followup_cycle


def test_whatsapp_full_intake_and_chunked_guidance_journey(client: TestClient, db_session: Session):
    """Scenario 1: Full WhatsApp intake flow using numbered quick-replies,
    persisting to Family/Person tables, chunking guidance, and recording consent.
    """
    phone = "+919444199999"

    def send_msg(text: str):
        res = client.post("/whatsapp/webhook", json={"from_number": phone, "body": text})
        assert res.status_code == status.HTTP_200_OK
        return res.json()

    # 1. First Message: Greeting
    r1 = send_msg("வணக்கம்")
    assert len(r1["reply_messages"]) >= 1
    assert "குடும்ப அமைப்பை" in r1["reply_messages"][0]

    # 2. Composition: 3 (Nuclear)
    r2 = send_msg("3")
    assert "மாவட்டம்" in r2["reply_messages"][0]

    # 3. District: Thanjavur
    r3 = send_msg("தஞ்சாவூர்")
    assert "வட்டம்" in r3["reply_messages"][0]

    # 4. Taluk: Papanasam
    r4 = send_msg("பாபநாசம்")
    assert "முகவரி" in r4["reply_messages"][0]

    # 5. Address
    r5 = send_msg("12, வடக்கு தெரு, பாபநாசம்")
    assert "குடும்ப அட்டை" in r5["reply_messages"][0]

    # 6. Ration Card: 1 (Green / Rice)
    r6 = send_msg("1")
    assert "வருமானம்" in r6["reply_messages"][0]

    # 7. Monthly Income: 8000
    r7 = send_msg("8000")
    assert "நபர்களின்" in r7["reply_messages"][0]

    # 8. Total members to register: 1
    r8 = send_msg("1")
    assert "பெயர்" in r8["reply_messages"][0]

    # 9. Person Name: கந்தசாமி
    r9 = send_msg("கந்தசாமி")
    assert "வயது" in r9["reply_messages"][0]

    # 10. Age: 65
    r10 = send_msg("65")
    assert "பாலினம்" in r10["reply_messages"][0]

    # 11. Gender: 2 (Male)
    r11 = send_msg("2")
    assert "கல்வி" in r11["reply_messages"][0]

    # 12. Education: 2 (Primary)
    r12 = send_msg("2")
    assert "தொழில்" in r12["reply_messages"][0]

    # 13. Occupation: 1 (Farmer) -> Adaptive Agriculture flow triggered
    r13 = send_msg("1")
    assert "நிலத்தின் அளவு" in r13["reply_messages"][0]

    # 14. Land holding acres: 1.5
    r14 = send_msg("1.5")
    assert "பயிர்" in r14["reply_messages"][0]

    # 15. Crop type: 1 (Paddy)
    r15 = send_msg("1")
    assert "திருமண நிலை" in r15["reply_messages"][0]

    # 16. Marital status: 1 (Married)
    r16 = send_msg("1")
    assert "சமூகப் பிரிவு" in r16["reply_messages"][0]

    # 17. Caste category: 1 (BC)
    r17 = send_msg("1")
    assert "மாற்றுத்திறனாளியா" in r17["reply_messages"][0]

    # 18. Disability: 2 (No)
    r18 = send_msg("2")
    assert "சிறப்பு" in r18["reply_messages"][0]

    # 19. Special flags: 4 (None) -> Summary prompt
    r19 = send_msg("4")
    assert "சரியானவையா" in r19["reply_messages"][0]

    # 20. Confirm summary: 1 (Yes, Confirm)
    r20 = send_msg("1")
    assert r20["is_completed"] is True
    # Verify guidance was split into sequential chunked messages (Summary + Schemes + Opt-In)
    assert len(r20["reply_messages"]) >= 2
    assert any("நலத்திட்டங்கள் கண்டறியப்பட்டன" in m for m in r20["reply_messages"])
    assert any("WhatsApp நினைவூட்டல் சேவை" in m for m in r20["reply_messages"])

    # 21. Opt-In Consent: 1 (Yes)
    r21 = send_msg("1")
    assert "நினைவூட்டல் சேவை இயக்கப்பட்டது" in r21["reply_messages"][0]
    assert r21["opted_in_consent"] is True

    # 22. Database Parity Verification
    db_session.expire_all()
    session_record = db_session.query(WhatsAppSession).filter(WhatsAppSession.phone_number == phone).first()
    assert session_record is not None
    assert session_record.whatsapp_consent is True
    assert session_record.family_id is not None

    family = db_session.query(Family).filter(Family.id == session_record.family_id).first()
    assert family is not None
    assert family.district == "தஞ்சாவூர்"
    assert family.taluk == "பாபநாசம்"
    assert len(family.persons) == 1
    assert family.persons[0].name == "கந்தசாமி"
    assert family.persons[0].occupation.value == "farmer"


def test_cross_channel_parity_whatsapp_and_web_app(client: TestClient, db_session: Session):
    """Scenario 2: A citizen completes intake on WhatsApp, then logs into the Web App via OTP.
    The web app must retrieve the EXACT same family and member records.
    """
    phone = "+919876500001"

    def send_msg(text: str):
        res = client.post("/whatsapp/webhook", json={"from_number": phone, "body": text})
        assert res.status_code == status.HTTP_200_OK
        return res.json()

    # Complete quick intake on WhatsApp
    send_msg("வணக்கம்")
    send_msg("3") # Nuclear
    send_msg("மதுரை") # Madurai
    send_msg("மேலூர்") # Melur
    send_msg("10, மெயின் ரோடு")
    send_msg("1") # Green card
    send_msg("6000")
    send_msg("1")
    send_msg("முத்துக்கிருஷ்ணன்")
    send_msg("42")
    send_msg("2") # Male
    send_msg("3") # 10th
    send_msg("2") # Daily wage (non-farmer skips agri)
    send_msg("1") # Married
    send_msg("2") # MBC
    send_msg("2") # No disability
    send_msg("4") # No flags
    r_confirm = send_msg("1") # Confirm summary
    assert r_confirm["is_completed"] is True

    # Now simulate citizen logging into the Web App with the same phone number via OTP
    otp_req = client.post("/auth/phone/send-otp", json={"phone": phone})
    assert otp_req.status_code == status.HTTP_200_OK

    verify_res = client.post("/auth/phone/verify-otp", json={"phone": phone, "otp": "123456"})
    assert verify_res.status_code == status.HTTP_200_OK
    auth_data = verify_res.json()
    token = auth_data["access_token"]
    user_id = auth_data["user"]["id"]

    db_session.expire_all()
    # Verify that the created family belongs to this user_id
    wa_session = db_session.query(WhatsAppSession).filter(WhatsAppSession.phone_number == phone).first()
    assert str(wa_session.user_id) == str(user_id)

    family_res = client.get(f"/families/{wa_session.family_id}", headers={"Authorization": f"Bearer {token}"})
    assert family_res.status_code == status.HTTP_200_OK
    fam_json = family_res.json()
    assert fam_json["district"] == "மதுரை"
    assert fam_json["taluk"] == "மேலூர்"
    assert len(fam_json["persons"]) == 1
    assert fam_json["persons"][0]["name"] == "முத்துக்கிருஷ்ணன்"


def test_whatsapp_multi_day_gap_resume_and_restart(client: TestClient, db_session: Session):
    """Scenario 3: User starts intake, pauses for 3 days, and returns.
    System detects uncompleted intake and offers Resume or Restart.
    """
    phone = "+919876500002"

    def send_msg(text: str):
        res = client.post("/whatsapp/webhook", json={"from_number": phone, "body": text})
        assert res.status_code == status.HTTP_200_OK
        return res.json()

    # Start intake
    send_msg("வணக்கம்")
    send_msg("3") # Nuclear
    send_msg("சேலம்") # Salem

    # Simulate 3-day silent gap
    db_session.expire_all()
    sess = db_session.query(WhatsAppSession).filter(WhatsAppSession.phone_number == phone).first()
    sess.last_user_message_at = datetime.now(timezone.utc) - timedelta(days=3)
    db_session.commit()

    # User returns and sends "வணக்கம்"
    resume_offer = send_msg("வணக்கம்")
    assert len(resume_offer["reply_messages"]) == 1
    assert "பாதியில் உள்ளது" in resume_offer["reply_messages"][0]
    assert "விட்ட இடத்திலிருந்து தொடர" in resume_offer["reply_messages"][0]

    # User chooses "1" to Resume
    resumed = send_msg("1")
    assert "விட்ட இடத்திலிருந்து தொடருவோம்" in resumed["reply_messages"][0]
    # Replays the pending question (Taluk/வட்டம்)
    assert "வட்டம்" in resumed["reply_messages"][0]

    # User continues smoothly
    r_next = send_msg("ஆத்தூர்")
    assert "முகவரி" in r_next["reply_messages"][0]


def test_whatsapp_proactive_followup_reminder_with_consent(client: TestClient, db_session: Session):
    """Scenario 4: Proactive scheme follow-up reminders sent over WhatsApp.
    Enforces opt-in consent and respects 24h template requirements.
    """
    phone = "+919876500003"

    def send_msg(text: str):
        res = client.post("/whatsapp/webhook", json={"from_number": phone, "body": text})
        assert res.status_code == status.HTTP_200_OK
        return res.json()

    # Setup completed session with opt-in consent
    send_msg("வணக்கம்")
    send_msg("1") # Single
    send_msg("சென்னை")
    send_msg("மயிலாப்பூர்")
    send_msg("5, காமராஜர் சாலை")
    send_msg("1")
    send_msg("5000")
    send_msg("1")
    send_msg("சுப்பிரமணியன்")
    send_msg("70")
    send_msg("2") # Male
    send_msg("1") # None
    send_msg("9") # Retired
    send_msg("3") # Widowed
    send_msg("1") # BC
    send_msg("2") # No disability
    send_msg("4") # None
    send_msg("1") # Confirm

    # Opt in to consent
    r_consent = send_msg("1") # Yes to consent
    assert r_consent["opted_in_consent"] is True

    db_session.expire_all()
    sess = db_session.query(WhatsAppSession).filter(WhatsAppSession.phone_number == phone).first()
    assert sess.whatsapp_consent is True

    # Create an application tracking record with documents_pending
    family = db_session.query(Family).filter(Family.id == sess.family_id).first()
    person = family.persons[0]

    from app.models.scheme import Scheme
    scheme = db_session.query(Scheme).first()

    app_record = ApplicationStatus(
        person_id=person.id,
        scheme_id=scheme.id,
        status=ApplicationTrackingStatus.DOCUMENTS_PENDING,
        last_updated=datetime.now().date() - timedelta(days=10),
        pending_documents=["குடும்ப அட்டை நகல்", "ஆதார் அட்டை"],
    )
    db_session.add(app_record)
    db_session.commit()

    # Case A: User messaged within 24 hours -> Session message sent
    scan_res = run_followup_cycle(db_session, pending_days_threshold=7, channel="whatsapp")
    assert scan_res.documents_pending_reminders_generated >= 1

    db_session.expire_all()
    latest_msg = (
        db_session.query(WhatsAppMessageLog)
        .filter(WhatsAppMessageLog.phone_number == phone, WhatsAppMessageLog.direction == "outbound")
        .order_by(WhatsAppMessageLog.created_at.desc(), WhatsAppMessageLog.id.desc())
        .first()
    )
    assert latest_msg is not None
    assert latest_msg.is_within_24h is True
    assert "நலத்திட்ட நினைவூட்டல்" in latest_msg.body

    # Case B: Simulate > 24 hours elapsed since user last messaged -> Template message sent
    sess.last_user_message_at = datetime.now(timezone.utc) - timedelta(hours=36)
    db_session.commit()

    scan_res_2 = run_followup_cycle(db_session, pending_days_threshold=7, channel="whatsapp")
    assert scan_res_2.documents_pending_reminders_generated >= 1

    db_session.expire_all()
    latest_msg_2 = (
        db_session.query(WhatsAppMessageLog)
        .filter(WhatsAppMessageLog.phone_number == phone, WhatsAppMessageLog.direction == "outbound")
        .order_by(WhatsAppMessageLog.created_at.desc(), WhatsAppMessageLog.id.desc())
        .first()
    )
    assert latest_msg_2.is_within_24h is False
    assert latest_msg_2.message_type == "template"
    assert latest_msg_2.template_name == "urimai_scheme_reminder_v1"


def test_whatsapp_proactive_reminder_skipped_when_consent_not_granted(client: TestClient, db_session: Session):
    """Scenario 5: If citizen rejected consent (whatsapp_consent=False), proactive follow-up
    reminders are strictly skipped and not dispatched to their number.
    """
    phone = "+919876500004"

    # Set up session with consent = False
    client.post("/whatsapp/webhook", json={"from_number": phone, "body": "வணக்கம்"})
    client.post("/whatsapp/consent", json={"phone_number": phone, "consent": False})

    db_session.expire_all()
    sess = db_session.query(WhatsAppSession).filter(WhatsAppSession.phone_number == phone).first()
    assert sess.whatsapp_consent is False

    from app.services.whatsapp_service import send_proactive_whatsapp_reminder
    success, reason = send_proactive_whatsapp_reminder(
        db=db_session,
        phone_number=phone,
        person_name="முனியம்மாள்",
        scheme_name="முதியோர் உதவித்தொகை",
        details_tamil="ஆவணங்கள் சமர்ப்பிக்கவும்",
    )
    assert success is False
    assert reason == "CONSENT_NOT_GRANTED"
