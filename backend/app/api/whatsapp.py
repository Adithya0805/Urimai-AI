from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Request, Response, Form, Query, status
from fastapi.responses import PlainTextResponse, Response as FastAPIResponse
from sqlalchemy.orm import Session
import xml.etree.ElementTree as ET

from app.database import get_db
from app.models.whatsapp import WhatsAppSession, WhatsAppMessageLog
from app.schemas.whatsapp import (
    WhatsAppInboundMessage,
    WhatsAppWebhookResponse,
    WhatsAppConsentRequest,
    WhatsAppSessionResponse,
)
from app.services.whatsapp_service import (
    process_inbound_whatsapp_message,
    send_proactive_whatsapp_reminder,
    get_or_create_whatsapp_session,
)
from app.services.whatsapp_adapter import normalize_phone_number, is_within_24h_window
from app.core.rate_limiter import rate_limit
from app.core.sanitizer import sanitize_phone

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp Channel (Tamil Nadu Citizens)"])


@router.get("/webhook", summary="Meta WhatsApp Webhook Verification")
def verify_meta_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
):
    """Meta WhatsApp Cloud API webhook challenge verification."""
    VERIFY_TOKEN = "urimai_webhook_verify_2026"
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return PlainTextResponse(hub_challenge or "")
    if hub_challenge:
        return PlainTextResponse(hub_challenge)
    return {"status": "verified"}


@router.post(
    "/webhook",
    response_model=WhatsAppWebhookResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Inbound WhatsApp Webhook (Twilio / Meta / Simulator)",
    description="Processes incoming WhatsApp messages from citizens, manages multi-day sessions, and returns Tamil replies.",
)
async def handle_whatsapp_webhook(
    request: Request,
    db: Session = Depends(get_db),
    From: Optional[str] = Form(None),
    Body: Optional[str] = Form(None),
    MessageSid: Optional[str] = Form(None),
    ProfileName: Optional[str] = Form(None),
):
    """Universal webhook supporting both Twilio form-encoded and Meta/Simulator JSON payloads."""
    content_type = request.headers.get("content-type", "")

    if "application/json" in content_type:
        try:
            json_body = await request.json()
        except Exception:
            json_body = {}

        # 1. Direct simulation schema: {"from_number": "+91...", "body": "..."}
        if "from_number" in json_body and "body" in json_body:
            inbound = WhatsAppInboundMessage(**json_body)
        # 2. Meta Cloud API schema: {"entry": [{"changes": [{"value": {"messages": [...]}}]}]}
        elif "entry" in json_body and json_body["entry"]:
            try:
                msg_entry = json_body["entry"][0]["changes"][0]["value"]["messages"][0]
                from_num = msg_entry.get("from", "")
                text_body = msg_entry.get("text", {}).get("body", "")
                inbound = WhatsAppInboundMessage(from_number=from_num, body=text_body)
            except Exception:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Meta payload structure")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unrecognized JSON payload format")

    else:
        # Twilio Form payload
        if not From or not Body:
            # Try parsing json fallback if form params were empty
            try:
                json_body = await request.json()
                inbound = WhatsAppInboundMessage(
                    from_number=json_body.get("from_number", json_body.get("From", "")),
                    body=json_body.get("body", json_body.get("Body", "")),
                )
            except Exception:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing 'From' or 'Body' form fields")
        else:
            inbound = WhatsAppInboundMessage(
                from_number=From,
                body=Body,
                message_id=MessageSid,
                profile_name=ProfileName,
            )

    result = process_inbound_whatsapp_message(db, inbound)

    # If requested by Twilio (accept header or form content), can return TwiML
    accept_header = request.headers.get("accept", "")
    if "application/xml" in accept_header or "text/xml" in accept_header:
        root = ET.Element("Response")
        for reply in result.reply_messages:
            msg_el = ET.SubElement(root, "Message")
            msg_el.text = reply
        xml_str = ET.tostring(root, encoding="utf-8", method="xml")
        return FastAPIResponse(content=xml_str, media_type="application/xml")

    return result


@router.post(
    "/consent",
    summary="Update Citizen WhatsApp Opt-In Consent",
    description="Records explicit citizen consent to receive proactive scheme reminders and application updates.",
)
def update_whatsapp_consent(payload: WhatsAppConsentRequest, db: Session = Depends(get_db)):
    clean_phone = sanitize_phone(payload.phone_number)
    session = get_or_create_whatsapp_session(db, clean_phone)
    session.whatsapp_consent = payload.consent
    from datetime import datetime, timezone
    session.consent_at = datetime.now(timezone.utc) if payload.consent else None
    db.commit()
    return {
        "status": "success",
        "phone_number": clean_phone,
        "whatsapp_consent": session.whatsapp_consent,
    }


@router.get(
    "/sessions/{phone_number}",
    response_model=WhatsAppSessionResponse,
    summary="Get WhatsApp Session Details",
)
def get_session_details(phone_number: str, db: Session = Depends(get_db)):
    clean_phone = sanitize_phone(phone_number)
    session = (
        db.query(WhatsAppSession)
        .filter(WhatsAppSession.phone_number == clean_phone)
        .order_by(WhatsAppSession.updated_at.desc())
        .first()
    )
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No active WhatsApp session found for phone {clean_phone}",
        )

    msg_count = db.query(WhatsAppMessageLog).filter(WhatsAppMessageLog.phone_number == clean_phone).count()

    return WhatsAppSessionResponse(
        id=str(session.id),
        phone_number=session.phone_number,
        user_id=str(session.user_id) if session.user_id else None,
        family_id=str(session.family_id) if session.family_id else None,
        current_step=session.current_step,
        status=session.status,
        whatsapp_consent=session.whatsapp_consent,
        last_user_message_at=session.last_user_message_at,
        is_within_24h_window=is_within_24h_window(session.last_user_message_at),
        message_count=msg_count,
    )
