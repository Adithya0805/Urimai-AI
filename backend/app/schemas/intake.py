from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class IntakeMessageRequest(BaseModel):
    session_id: Optional[str] = Field(None, description="Unique session ID. If not provided, a new one will be generated.")
    message: str = Field(..., description="User's input message in Tamil or English")


class IntakeMessageResponse(BaseModel):
    session_id: str
    reply: str
    current_step: str
    pending_clarification: Optional[str] = None
    is_completed: bool = False
    summary: Optional[str] = None
    saved_family_id: Optional[str] = None
    saved_person_ids: List[str] = Field(default_factory=list)


class IntakeExtractionLogResponse(BaseModel):
    id: UUID
    session_id: str
    raw_tamil_input: str
    target_field: str
    extracted_value: str
    confirmed_value: Optional[str] = None
    is_valid: bool
    error_message: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
