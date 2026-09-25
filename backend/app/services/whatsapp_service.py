"""Urimai AI — WhatsApp Channel Service
=========================================
Handles webhook processing, session persistence, multi-day resume detection,
cross-channel family mapping, guidance chunking, and consent-gated proactive reminders.
"""

import uuid
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified
from uuid import UUID

from app.database import SessionLocal
from app.models.family import Family
from app.models.person import Person
from app.models.whatsapp import WhatsAppSession, WhatsAppMessageLog
from app.schemas.whatsapp import WhatsAppInboundMessage, WhatsAppWebhookResponse
from app.services.intake_state import IntakeState, create_initial_state
from app.services.intake_graph import process_user_turn
from app.services.matching_engine import evaluate_person_eligibility, evaluate_family_eligibility
from app.services.guidance_service import generate_person_guidance
from app.models.scheme import Scheme
from app.services.whatsapp_adapter import (
    normalize_phone_number,
    is_within_24h_window,
    format_whatsapp_intake_question,
    parse_numbered_input,
    split_guidance_into_whatsapp_messages,
    format_proactive_whatsapp_reminder,
)
from app.core.auth import USER_REGISTRY
from app.core.sanitizer import sanitize_text

logger = logging.getLogger("urimai.whatsapp")


def get_or_create_auth_user_id_for_phone(phone: str) -> str:
    """Ensures consistent auth user ID between WhatsApp and Web App."""
    clean_phone = normalize_phone_number(phone)
    if clean_phone in USER_REGISTRY:
        return USER_REGISTRY[clean_phone]["id"]
    new_id = str(uuid.uuid4())
    USER_REGISTRY[clean_phone] = {
        "id": new_id,
        "phone": clean_phone,
        "role": "citizen",
    }
    return new_id


def _get_guidance_for_person(person_id: UUID, db: Session):
    """Internal helper to generate guidance for an individual."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        return None
    family = db.query(Family).filter(Family.id == person.family_id).first()
    if not family:
        return None
    active_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    return generate_person_guidance(person, family, active_schemes, db=db)



def get_or_create_whatsapp_session(db: Session, phone: str) -> WhatsAppSession:
    """Fetches existing WhatsApp session or initializes a new one in the database."""
    clean_phone = normalize_phone_number(phone)
    session = (
        db.query(WhatsAppSession)
        .filter(WhatsAppSession.phone_number == clean_phone)
        .order_by(WhatsAppSession.updated_at.desc())
        .first()
    )
    user_id = get_or_create_auth_user_id_for_phone(clean_phone)

    if not session:
        initial_state = create_initial_state(f"wa_{uuid.uuid4().hex[:8]}")
        initial_state["user_id"] = user_id
        session = WhatsAppSession(
            phone_number=clean_phone,
            user_id=UUID(user_id) if user_id else None,
            current_step="greet",
            state_data=initial_state,
            status="active",
            whatsapp_consent=False,
            last_user_message_at=datetime.now(timezone.utc),
        )
        db.add(session)
        db.commit()
        db.refresh(session)

    return session


def log_whatsapp_message(
    db: Session,
    phone: str,
    direction: str,
    body: str,
    message_type: str = "session",
    template_name: Optional[str] = None,
    is_within_24h: bool = True,
    status: str = "sent",
):
    """Logs inbound/outbound WhatsApp message for audit and 24h compliance."""
    clean_phone = normalize_phone_number(phone)
    log_entry = WhatsAppMessageLog(
        phone_number=clean_phone,
        direction=direction,
        message_type=message_type,
        template_name=template_name,
        body=body,
        is_within_24h=is_within_24h,
        status=status,
    )
    db.add(log_entry)
    db.commit()


def process_inbound_whatsapp_message(
    db: Session,
    inbound: WhatsAppInboundMessage,
) -> WhatsAppWebhookResponse:
    """Processes an inbound WhatsApp message, managing multi-day sessions,
    intake dialogue, guidance delivery, and opt-in consent.
    """
    clean_phone = normalize_phone_number(inbound.from_number)
    text = sanitize_text(inbound.body.strip(), max_length=2000)
    now = datetime.now(timezone.utc)

    # 1. Log inbound message
    log_whatsapp_message(
        db,
        phone=clean_phone,
        direction="inbound",
        body=text,
        message_type="session",
        is_within_24h=True,
        status="received",
    )

    # 2. Get or create session
    session = get_or_create_whatsapp_session(db, clean_phone)
    session.last_user_message_at = now
    state: IntakeState = session.state_data or create_initial_state(f"wa_{uuid.uuid4().hex[:8]}")
    user_id = str(session.user_id) if session.user_id else get_or_create_auth_user_id_for_phone(clean_phone)
    state["user_id"] = user_id

    outbound_messages: List[str] = []
    t_lower = text.lower()

    # 3. Check for existing registered Family (Cross-Channel Recognition)
    existing_family = db.query(Family).filter(Family.user_id == UUID(user_id)).first() if user_id else None

    # Handle Awaiting Resume Choice (Multi-day pause resolution)
    if session.status == "awaiting_resume_choice":
        if text in ("1", "1️⃣") or any(w in t_lower for w in ["தொடர", "resume", "continue", "ஆம்", "yes"]):
            session.status = "active"
            # Replay the last step's formatted question
            raw_q = state.get("reply") or state.get("last_question", "")
            question = format_whatsapp_intake_question(state.get("current_step", "family_composition"), raw_q)
            outbound_messages.append(f"👍 *நன்றி! விட்ட இடத்திலிருந்து தொடருவோம்.*\n\n{question}")
            session.state_data = state
            db.commit()
            for msg in outbound_messages:
                log_whatsapp_message(db, clean_phone, "outbound", msg)
            return WhatsAppWebhookResponse(
                reply_messages=outbound_messages,
                session_id=str(session.id),
                current_step=session.current_step,
            )
        elif text in ("2", "2️⃣") or any(w in t_lower for w in ["புதிதாக", "restart", "start over", "reset"]):
            # Reset to start
            session.status = "active"
            session.current_step = "greet"
            state = create_initial_state(f"wa_{uuid.uuid4().hex[:8]}")
            state["user_id"] = user_id
            session.state_data = state
            q = format_whatsapp_intake_question("greet", "")
            outbound_messages.append(q)
            db.commit()
            for msg in outbound_messages:
                log_whatsapp_message(db, clean_phone, "outbound", msg)
            return WhatsAppWebhookResponse(
                reply_messages=outbound_messages,
                session_id=str(session.id),
                current_step="greet",
            )
        else:
            msg = (
                "தயவுசெய்து எண்ணை மட்டும் தேர்வு செய்யவும்:\n"
                "1️⃣ விட்ட இடத்திலிருந்து தொடர (Resume)\n"
                "2️⃣ புதிதாக தொடங்க (Restart)"
            )
            outbound_messages.append(msg)
            for m in outbound_messages:
                log_whatsapp_message(db, clean_phone, "outbound", m)
            return WhatsAppWebhookResponse(reply_messages=outbound_messages, session_id=str(session.id))

    # 4. Handle Consent Opt-in Stage
    if session.status == "awaiting_consent" or session.current_step == "consent_optin":
        if text in ("1", "1️⃣") or any(w in t_lower for w in ["ஆம்", "yes", "சரி", "ok"]):
            session.whatsapp_consent = True
            session.consent_at = now
            session.status = "completed"
            session.current_step = "completed"
            msg = (
                "✅ *நன்றி! WhatsApp நினைவூட்டல் சேவை இயக்கப்பட்டது.*\n\n"
                "தங்கள் நலத்திட்ட விண்ணப்ப நிலவரம் மற்றும் புதுப்பித்தல் குறித்த அறிவிப்புகள் இங்கு அனுப்பப்படும்.\n\n"
                "👉 தங்களின் விவரங்களை Urimai AI இணையதளத்திலும் தங்களின் மொபைல் எண் மூலம் எப்போது வேண்டுமானாலும் பார்க்கலாம்."
            )
            outbound_messages.append(msg)
        else:
            session.whatsapp_consent = False
            session.status = "completed"
            session.current_step = "completed"
            msg = (
                "👍 *புரிந்துகொண்டோம்.*\n\n"
                "தங்களுக்கு எந்த நினைவூட்டல்களும் அனுப்பப்படாது. உதவி தேவைப்படும்போது எப்போது வேண்டுமானாலும் 'வணக்கம்' என அனுப்பலாம்."
            )
            outbound_messages.append(msg)

        db.commit()
        for m in outbound_messages:
            log_whatsapp_message(db, clean_phone, "outbound", m)
        return WhatsAppWebhookResponse(
            reply_messages=outbound_messages,
            session_id=str(session.id),
            current_step="completed",
            is_completed=True,
            opted_in_consent=session.whatsapp_consent,
        )

    # 5. Check if user sends a generic greeting to an existing or incomplete session
    is_greeting = any(w in t_lower for w in ["வணக்கம்", "hi", "hello", "start", "vanakkam", "menu", "ஹலோ", "வண"])
    
    if is_greeting and session.status == "completed" and existing_family:
        # Returning user menu
        first_person = existing_family.persons[0] if existing_family.persons else None
        p_name = first_person.name if first_person else "பயனாளர்"
        menu_msg = (
            f"🏛️ *வணக்கம் {p_name}! உரிமை AI உதவி மையத்திற்கு நல்வரவு.*\n\n"
            f"தங்களின் குடும்பம் ({existing_family.district} மாவட்டம்) ஏற்கனவே பதிவு செய்யப்பட்டுள்ளது.\n\n"
            "எவ்வகையில் உதவலாம்?\n"
            "1️⃣ தகுதியான நலத்திட்டங்கள் & வழிகாட்டி பார்க்க\n"
            "2️⃣ விண்ணப்ப நிலவரம் (Status) அறிய\n"
            "3️⃣ புதிய குடும்ப தகவல்களை பதிவு செய்ய\n\n"
            "👉 _1, 2 அல்லது 3 என அனுப்பவும்._"
        )
        outbound_messages.append(menu_msg)
        session.current_step = "main_menu"
        db.commit()
        for m in outbound_messages:
            log_whatsapp_message(db, clean_phone, "outbound", m)
        return WhatsAppWebhookResponse(reply_messages=outbound_messages, session_id=str(session.id), current_step="main_menu")

    if is_greeting and session.current_step not in ("greet", "completed") and session.status == "active":
        # Mid-conversation pause: offer Resume or Restart
        session.status = "awaiting_resume_choice"
        db.commit()
        resume_prompt = (
            "🏛️ *உரிமை AI — உரையாடல் பதிவு*\n\n"
            "வணக்கம்! தங்களின் முந்தைய பதிவு பாதியில் உள்ளது.\n\n"
            "1️⃣ விட்ட இடத்திலிருந்து தொடர (Resume)\n"
            "2️⃣ புதிதாக தொடங்க (Restart)\n\n"
            "👉 _1 அல்லது 2 என பதிலளிக்கவும்._"
        )
        outbound_messages.append(resume_prompt)
        for m in outbound_messages:
            log_whatsapp_message(db, clean_phone, "outbound", m)
        return WhatsAppWebhookResponse(
            reply_messages=outbound_messages,
            session_id=str(session.id),
            current_step="awaiting_resume_choice",
        )

    # 6. Handle Main Menu choices for registered users
    if session.current_step == "main_menu" and existing_family:
        if text in ("1", "1️⃣") or "திட்டம்" in t_lower:
            first_person = existing_family.persons[0] if existing_family.persons else None
            if first_person:
                guidance = _get_guidance_for_person(first_person.id, db)
                if guidance:
                    chunked = split_guidance_into_whatsapp_messages(
                        first_person.name,
                        [g.model_dump() for g in guidance.eligible_schemes_guidance],
                        [g.model_dump() for g in guidance.partially_eligible_schemes_guidance],
                    )
                    outbound_messages.extend(chunked)
                    session.current_step = "consent_optin"
                else:
                    outbound_messages.append("வழிகாட்டி விவரங்கள் கிடைக்கவில்லை.")
            else:
                outbound_messages.append("குடும்ப உறுப்பினர்கள் விவரங்கள் கிடைக்கவில்லை.")
        elif text in ("2", "2️⃣") or "நிலவரம்" in t_lower or "status" in t_lower:
            outbound_messages.append(
                "📋 *விண்ணப்ப நிலவரம் (Application Status):*\n\n"
                "தங்களின் விண்ணப்பங்கள் பரிசீலனையில் உள்ளன. தேவையான ஆவணங்கள் இருப்பின் உடனடியாக நினைவூட்டல் அனுப்பப்படும்."
            )
        elif text in ("3", "3️⃣") or "புதிய" in t_lower:
            session.current_step = "greet"
            state = create_initial_state(f"wa_{uuid.uuid4().hex[:8]}")
            state["user_id"] = user_id
            session.state_data = state
            q = format_whatsapp_intake_question("greet", "")
            outbound_messages.append(q)
        else:
            outbound_messages.append("தயவுசெய்து 1, 2 அல்லது 3 என தேர்வு செய்யவும்.")

        session.state_data = state
        db.commit()
        for m in outbound_messages:
            log_whatsapp_message(db, clean_phone, "outbound", m)
        return WhatsAppWebhookResponse(reply_messages=outbound_messages, session_id=str(session.id), current_step=session.current_step)

    # 7. Process Intake Turn with Numbered Quick-Reply parsing
    current_step = state.get("current_step", "greet")
    parsed_input = parse_numbered_input(current_step, text)

    updated_state = process_user_turn(state, parsed_input, db)
    session.current_step = updated_state["current_step"]
    session.state_data = dict(updated_state)
    flag_modified(session, "state_data")

    if updated_state.get("is_completed"):
        # Intake finished! Saved to DB
        fam_id = updated_state.get("saved_family_id")
        person_ids = updated_state.get("saved_person_ids", [])
        session.family_id = UUID(fam_id) if fam_id else None
        session.status = "awaiting_consent"
        session.current_step = "consent_optin"

        # Generate guidance and chunk into readable WhatsApp messages
        if person_ids:
            primary_pid = UUID(person_ids[0])
            guidance = _get_guidance_for_person(primary_pid, db)
            p_name = updated_state["persons_data"][0].get("name", "பயனாளர்") if updated_state.get("persons_data") else "பயனாளர்"
            
            if guidance:
                chunked_msgs = split_guidance_into_whatsapp_messages(
                    p_name,
                    [g.model_dump() for g in guidance.eligible_schemes_guidance],
                    [g.model_dump() for g in guidance.partially_eligible_schemes_guidance],
                )
                outbound_messages.extend(chunked_msgs)
            else:
                outbound_messages.append("✅ தங்களின் குடும்ப விவரங்கள் வெற்றிகரமாக பதிவு செய்யப்பட்டன!")
        else:
            outbound_messages.append("✅ தங்களின் குடும்ப விவரங்கள் வெற்றிகரமாக பதிவு செய்யப்பட்டன!")

    else:
        # Format the next question with numbered options
        formatted_question = format_whatsapp_intake_question(
            updated_state["current_step"],
            updated_state["reply"],
        )
        outbound_messages.append(formatted_question)

    db.commit()

    # Log outbound replies
    for m in outbound_messages:
        log_whatsapp_message(db, clean_phone, "outbound", m)

    return WhatsAppWebhookResponse(
        status="success",
        reply_messages=outbound_messages,
        session_id=str(session.id),
        current_step=session.current_step,
        is_completed=updated_state.get("is_completed", False),
    )


def send_proactive_whatsapp_reminder(
    db: Session,
    phone_number: str,
    person_name: str,
    scheme_name: str,
    details_tamil: str,
    notification_type: str = "documents_pending_reminder",
) -> Tuple[bool, str]:
    """Dispatches a proactive WhatsApp reminder, enforcing opt-in consent and 24h template rules."""
    clean_phone = normalize_phone_number(phone_number)
    session = (
        db.query(WhatsAppSession)
        .filter(WhatsAppSession.phone_number == clean_phone)
        .order_by(WhatsAppSession.updated_at.desc())
        .first()
    )

    # 1. Check Opt-In Consent
    if not session or not session.whatsapp_consent:
        logger.info(f"Skipping proactive WhatsApp message to {clean_phone}: user has not opted in.")
        return False, "CONSENT_NOT_GRANTED"

    # 2. Check 24h Customer Service Window
    within_24h = is_within_24h_window(session.last_user_message_at)
    is_template = not within_24h

    # 3. Format message
    msg_body = format_proactive_whatsapp_reminder(
        notification_type=notification_type,
        person_name=person_name,
        scheme_name=scheme_name,
        details=details_tamil,
        is_template=is_template,
    )

    # 4. Log message
    log_whatsapp_message(
        db=db,
        phone=clean_phone,
        direction="outbound",
        body=msg_body,
        message_type="template" if is_template else "session",
        template_name="urimai_scheme_reminder_v1" if is_template else None,
        is_within_24h=within_24h,
        status="sent",
    )

    logger.info(f"Proactive WhatsApp reminder sent to {clean_phone} (is_template={is_template})")
    return True, msg_body
