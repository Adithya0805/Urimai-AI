import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Text, Boolean, DateTime, JSON, ForeignKey, func
from app.database import Base
from app.models.family import GUID


class WhatsAppSession(Base):
    __tablename__ = "whatsapp_sessions"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    phone_number = Column(String(50), nullable=False, index=True)
    user_id = Column(GUID(), nullable=True, index=True)
    family_id = Column(GUID(), ForeignKey("families.id", ondelete="SET NULL"), nullable=True)
    current_step = Column(String(50), nullable=False, default="greet")
    state_data = Column(JSON, nullable=False, default=dict)
    status = Column(String(50), nullable=False, default="active")  # active, completed, awaiting_resume_choice
    whatsapp_consent = Column(Boolean, nullable=False, default=False)
    consent_at = Column(DateTime(timezone=True), nullable=True)
    last_user_message_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class WhatsAppMessageLog(Base):
    __tablename__ = "whatsapp_message_logs"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    phone_number = Column(String(50), nullable=False, index=True)
    direction = Column(String(20), nullable=False)  # inbound, outbound
    message_type = Column(String(50), nullable=False, default="session")  # session, template, quick_reply
    template_name = Column(String(100), nullable=True)
    body = Column(Text, nullable=False)
    is_within_24h = Column(Boolean, nullable=False, default=True)
    status = Column(String(50), nullable=False, default="sent")  # received, sent, failed
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False,
    )
