import datetime
from typing import List, Optional, Any, Dict
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import RuleOperator, RuleAppliesTo


class DashboardStatsResponse(BaseModel):
    total_families: int
    total_persons: int
    total_applications: int
    active_schemes_count: int
    stale_schemes_count: int
    stuck_applications_count: int
    schemes_zero_matches: List[Dict[str, Any]] = []
    total_extractions_logged: int
    recent_errors_count: int


class AdminAuditLogResponse(BaseModel):
    id: UUID
    admin_user_id: UUID
    admin_email: str
    action: str
    entity_type: str
    entity_id: str
    before_value: Optional[Dict[str, Any]] = None
    after_value: Optional[Dict[str, Any]] = None
    ip_address: Optional[str] = None
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class StuckApplicationItem(BaseModel):
    id: UUID
    person_id: UUID
    person_name: str
    family_id: UUID
    district: str
    scheme_id: UUID
    scheme_code: str
    scheme_name_tamil: str
    scheme_name_english: str
    department: str
    status: str
    days_stuck: int
    last_updated: datetime.date
    pending_documents: List[str]
    next_action_note: Optional[str] = None


class ErrorLogItem(BaseModel):
    id: UUID
    log_type: str  # "extraction_failure", "llm_error", "system_error"
    session_id: Optional[str] = None
    raw_input: Optional[str] = None
    target_field: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime.datetime


class RuleUpdateRequest(BaseModel):
    field_name: Optional[str] = None
    operator: Optional[RuleOperator] = None
    value: Optional[str] = None
    applies_to: Optional[RuleAppliesTo] = None
    admin_notes: str = Field(..., description="Mandatory rationale for why this rule is being updated")


class RuleCreateRequest(BaseModel):
    field_name: str
    operator: RuleOperator
    value: str
    applies_to: RuleAppliesTo
    admin_notes: str = Field(..., description="Mandatory rationale for why this rule is being created")
