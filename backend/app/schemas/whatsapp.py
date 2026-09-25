from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class WhatsAppInboundMessage(BaseModel):
    """Normalized inbound message from Twilio, Meta, or direct simulator."""
    from_number: str = Field(..., description="Sender WhatsApp phone number in E.164 (e.g. +919876543210)")
    body: str = Field(..., description="Message text content")
    message_id: Optional[str] = Field(None, description="Provider message SID / ID")
    profile_name: Optional[str] = Field(None, description="Sender WhatsApp display name")
    timestamp: Optional[datetime] = None


class WhatsAppOutboundMessage(BaseModel):
    to_number: str
    body: str
    message_type: str = "session"  # session, template, quick_reply
    template_name: Optional[str] = None
    media_url: Optional[str] = None


class WhatsAppWebhookResponse(BaseModel):
    status: str = "success"
    reply_messages: List[str] = []
    session_id: Optional[str] = None
    current_step: Optional[str] = None
    is_completed: bool = False
    opted_in_consent: Optional[bool] = None


class WhatsAppConsentRequest(BaseModel):
    phone_number: str
    consent: bool = True


class WhatsAppSessionResponse(BaseModel):
    id: str
    phone_number: str
    user_id: Optional[str] = None
    family_id: Optional[str] = None
    current_step: str
    status: str
    whatsapp_consent: bool
    last_user_message_at: datetime
    is_within_24h_window: bool
    message_count: int = 0
