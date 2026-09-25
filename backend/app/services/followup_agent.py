import datetime
from typing import List, Tuple
from sqlalchemy.orm import Session
from app.models.enums import ApplicationTrackingStatus
from app.models.application_status import ApplicationStatus, NotificationLog
from app.schemas.application_status import FollowupScanResult

DEFAULT_DOCUMENTS_PENDING_DAYS = 7
DEFAULT_RENEWAL_ALERT_WINDOW_DAYS = 30


def generate_documents_pending_tamil_message(app: ApplicationStatus) -> str:
    """Generates structured Tamil follow-up reminder for pending documents."""
    person_name = app.person.name if app.person else "பயனாளர்"
    scheme_name = app.scheme.name_tamil if app.scheme else "நலத்திட்டம்"
    office = app.scheme.application_office if app.scheme else "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்"
    portal = (
        app.scheme.online_application_url
        if (app.scheme and app.scheme.online_application_url)
        else "அருகிலுள்ள இ-சேவை மையம் (e-Sevai)"
    )

    # Determine missing docs
    missing_docs = app.pending_documents
    if not missing_docs and app.scheme and app.scheme.required_documents:
        missing_docs = app.scheme.required_documents

    docs_list_tamil = (
        "\n".join([f"  • {doc}" for doc in missing_docs])
        if missing_docs
        else "  • தேவையான அசல் சான்றிதழ்கள்"
    )

    days_pending = (datetime.date.today() - app.last_updated).days

    return (
        f"வணக்கம் {person_name}!\n\n"
        f"தங்களின் '{scheme_name}' விண்ணப்பத்திற்கு ஆவணங்கள் சமர்ப்பிக்கப்பட்டு {days_pending} நாட்களாக நிலுவையில் உள்ளன.\n"
        f"இன்னும் சமர்ப்பிக்கப்பட வேண்டிய ஆவணங்கள்:\n"
        f"{docs_list_tamil}\n\n"
        f"விண்ணப்பத்தை விரைவாக பரிசீலிக்க இவ்வாவணங்களை {office} அல்லது {portal} வாயிலாக சமர்ப்பிக்கவும்."
    )


def generate_renewal_due_tamil_message(app: ApplicationStatus) -> str:
    """Generates structured Tamil follow-up reminder for renewal due schemes."""
    person_name = app.person.name if app.person else "பயனாளர்"
    scheme_name = app.scheme.name_tamil if app.scheme else "நலத்திட்டம்"
    office = app.scheme.application_office if app.scheme else "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்"
    due_date_str = (
        app.renewal_due_date.strftime("%d-%m-%Y")
        if app.renewal_due_date
        else "உடனடியாக"
    )

    return (
        f"வணக்கம் {person_name}!\n\n"
        f"தங்களின் '{scheme_name}' திட்ட பலன்களை தொடர்ந்து பெற வருடாந்திர புதுப்பித்தல் (Renewal) செய்ய வேண்டும்.\n"
        f"கடைசி நாள் / தவணை: {due_date_str}.\n\n"
        f"வாழ்வுரிமைச் சான்றிதழ் அல்லது வருமானச் சான்றிதழுடன் {office} அணுகி புதுப்பிக்குமாறு அன்புடன் கேட்டுக்கொள்கிறோம்."
    )


def run_followup_cycle(
    db: Session,
    pending_days_threshold: int = DEFAULT_DOCUMENTS_PENDING_DAYS,
    renewal_window_days: int = DEFAULT_RENEWAL_ALERT_WINDOW_DAYS,
    channel: str = "log",
) -> FollowupScanResult:
    """Follow-up agent worker:
    1. Scans all applications in DOCUMENTS_PENDING status older than pending_days_threshold.
    2. Scans all applications in RENEWAL_DUE status or approaching renewal_due_date.
    3. Emits Tamil reminders and logs them into notification_logs (ready for WhatsApp / SMS adapter).
    """
    all_apps = db.query(ApplicationStatus).all()
    today = datetime.date.today()

    doc_reminders = 0
    renewal_reminders = 0
    notifications_created = 0

    for app in all_apps:
        # 1. Documents pending check
        if app.status == ApplicationTrackingStatus.DOCUMENTS_PENDING:
            days_old = (today - app.last_updated).days
            if days_old >= pending_days_threshold:
                message = generate_documents_pending_tamil_message(app)
                
                # Check WhatsApp dispatch
                if channel == "whatsapp":
                    from app.models.whatsapp import WhatsAppSession
                    from app.services.whatsapp_service import send_proactive_whatsapp_reminder
                    # Find session by person's family
                    fam = app.person.family if app.person else None
                    sess = db.query(WhatsAppSession).filter(WhatsAppSession.family_id == fam.id).first() if fam else None
                    if sess and sess.whatsapp_consent:
                        p_name = app.person.name if app.person else "பயனாளர்"
                        s_name = app.scheme.name_tamil if app.scheme else "நலத்திட்டம்"
                        send_proactive_whatsapp_reminder(
                            db=db,
                            phone_number=sess.phone_number,
                            person_name=p_name,
                            scheme_name=s_name,
                            details_tamil=f"தேவையான ஆவணங்கள் நிலுவையில் உள்ளன ({days_old} நாட்கள்).",
                            notification_type="documents_pending_reminder",
                        )

                notif = NotificationLog(
                    application_id=app.id,
                    person_id=app.person_id,
                    notification_type="documents_pending_reminder",
                    channel=channel,
                    message_tamil=message,
                )
                db.add(notif)
                doc_reminders += 1
                notifications_created += 1

        # 2. Renewal due check
        elif app.status == ApplicationTrackingStatus.RENEWAL_DUE:
            message = generate_renewal_due_tamil_message(app)

            # Check WhatsApp dispatch
            if channel == "whatsapp":
                from app.models.whatsapp import WhatsAppSession
                from app.services.whatsapp_service import send_proactive_whatsapp_reminder
                fam = app.person.family if app.person else None
                sess = db.query(WhatsAppSession).filter(WhatsAppSession.family_id == fam.id).first() if fam else None
                if sess and sess.whatsapp_consent:
                    p_name = app.person.name if app.person else "பயனாளர்"
                    s_name = app.scheme.name_tamil if app.scheme else "நலத்திட்டம்"
                    send_proactive_whatsapp_reminder(
                        db=db,
                        phone_number=sess.phone_number,
                        person_name=p_name,
                        scheme_name=s_name,
                        details_tamil="வருடாந்திர புதுப்பித்தல் செய்ய வேண்டும்.",
                        notification_type="renewal_due_reminder",
                    )

            notif = NotificationLog(
                application_id=app.id,
                person_id=app.person_id,
                notification_type="renewal_due_reminder",
                channel=channel,
                message_tamil=message,
            )
            db.add(notif)
            renewal_reminders += 1
            notifications_created += 1

        elif app.renewal_due_date:
            days_until_renewal = (app.renewal_due_date - today).days
            if 0 <= days_until_renewal <= renewal_window_days:
                # Update status to renewal_due
                app.status = ApplicationTrackingStatus.RENEWAL_DUE
                message = generate_renewal_due_tamil_message(app)

                if channel == "whatsapp":
                    from app.models.whatsapp import WhatsAppSession
                    from app.services.whatsapp_service import send_proactive_whatsapp_reminder
                    fam = app.person.family if app.person else None
                    sess = db.query(WhatsAppSession).filter(WhatsAppSession.family_id == fam.id).first() if fam else None
                    if sess and sess.whatsapp_consent:
                        p_name = app.person.name if app.person else "பயனாளர்"
                        s_name = app.scheme.name_tamil if app.scheme else "நலத்திட்டம்"
                        send_proactive_whatsapp_reminder(
                            db=db,
                            phone_number=sess.phone_number,
                            person_name=p_name,
                            scheme_name=s_name,
                            details_tamil=f"புதுப்பித்தல் கடைசி நாள்: {app.renewal_due_date}",
                            notification_type="renewal_due_reminder",
                        )

                notif = NotificationLog(
                    application_id=app.id,
                    person_id=app.person_id,
                    notification_type="renewal_due_reminder",
                    channel=channel,
                    message_tamil=message,
                )
                db.add(notif)
                renewal_reminders += 1
                notifications_created += 1

    db.commit()

    return FollowupScanResult(
        total_applications_checked=len(all_apps),
        documents_pending_reminders_generated=doc_reminders,
        renewal_reminders_generated=renewal_reminders,
        notifications_created=notifications_created,
        message=(
            f"Follow-up cycle completed. Processed {len(all_apps)} applications. "
            f"Generated {doc_reminders} pending document reminders and {renewal_reminders} renewal reminders."
        ),
    )
