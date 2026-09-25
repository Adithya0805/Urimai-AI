import uuid
import datetime
from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
    JSON,
    Enum as SQLEnum,
    func,
)
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.family import GUID
from app.models.enums import ApplicationTrackingStatus


class ApplicationStatus(Base):
    __tablename__ = "application_statuses"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    person_id = Column(
        GUID(),
        ForeignKey("persons.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    scheme_id = Column(
        GUID(),
        ForeignKey("schemes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    status = Column(
        SQLEnum(
            ApplicationTrackingStatus,
            name="application_tracking_status_enum",
            native_enum=False,
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
        default=ApplicationTrackingStatus.NOT_STARTED,
        index=True,
    )
    last_updated = Column(Date, nullable=False, default=datetime.date.today)
    next_action_note = Column(Text, nullable=True)
    pending_documents = Column(JSON, default=list, nullable=False)
    renewal_due_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    person = relationship("Person", lazy="selectin")
    scheme = relationship("Scheme", lazy="selectin")
    notifications = relationship(
        "NotificationLog",
        back_populates="application",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    application_id = Column(
        GUID(),
        ForeignKey("application_statuses.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    person_id = Column(
        GUID(),
        ForeignKey("persons.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    notification_type = Column(String(100), nullable=False)  # documents_pending_reminder, renewal_due_reminder
    channel = Column(String(50), nullable=False, default="log")  # log, whatsapp, sms
    message_tamil = Column(Text, nullable=False)
    sent_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    application = relationship("ApplicationStatus", back_populates="notifications")
    person = relationship("Person", lazy="selectin")


class SchemeReviewQueue(Base):
    __tablename__ = "scheme_review_queue"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    scheme_id = Column(
        GUID(),
        ForeignKey("schemes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    flagged_reason = Column(Text, nullable=False)
    source_url = Column(String(500), nullable=False)
    status = Column(String(50), nullable=False, default="pending_human_review", index=True)
    reviewer_notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    reviewed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    scheme = relationship("Scheme", lazy="selectin")
