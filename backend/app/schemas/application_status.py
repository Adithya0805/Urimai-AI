import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import ApplicationTrackingStatus


class ApplicationStatusBase(BaseModel):
    person_id: UUID
    scheme_id: UUID
    status: ApplicationTrackingStatus = ApplicationTrackingStatus.NOT_STARTED
    next_action_note: Optional[str] = None
    pending_documents: List[str] = Field(default_factory=list)
    renewal_due_date: Optional[datetime.date] = None


class ApplicationStatusCreate(ApplicationStatusBase):
    pass


class ApplicationStatusUpdate(BaseModel):
    status: Optional[ApplicationTrackingStatus] = None
    next_action_note: Optional[str] = None
    pending_documents: Optional[List[str]] = None
    renewal_due_date: Optional[datetime.date] = None
    last_updated: Optional[datetime.date] = None


class ApplicationStatusResponse(ApplicationStatusBase):
    id: UUID
    last_updated: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
    person_name: Optional[str] = None
    scheme_code: Optional[str] = None
    scheme_name_tamil: Optional[str] = None
    scheme_name_english: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class NotificationLogResponse(BaseModel):
    id: UUID
    application_id: Optional[UUID] = None
    person_id: UUID
    notification_type: str
    channel: str
    message_tamil: str
    sent_at: datetime.datetime
    person_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class SchemeReviewQueueResponse(BaseModel):
    id: UUID
    scheme_id: UUID
    scheme_code: str
    scheme_name_tamil: str
    scheme_name_english: str
    department: str
    source_url: str
    last_verified_date: Optional[datetime.date] = None
    flagged_reason: str
    status: str
    reviewer_notes: Optional[str] = None
    created_at: datetime.datetime
    reviewed_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)


class FreshnessScanResult(BaseModel):
    total_schemes_checked: int
    stale_schemes_flagged: int
    review_queue_count: int
    message: str


class FollowupScanResult(BaseModel):
    total_applications_checked: int
    documents_pending_reminders_generated: int
    renewal_reminders_generated: int
    notifications_created: int
    message: str
