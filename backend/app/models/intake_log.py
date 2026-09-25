import uuid
from sqlalchemy import Column, String, Text, Boolean, DateTime, func
from app.database import Base
from app.models.family import GUID


class IntakeExtractionLog(Base):
    __tablename__ = "intake_extraction_logs"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    session_id = Column(String(100), nullable=False, index=True)
    raw_tamil_input = Column(Text, nullable=False)
    target_field = Column(String(100), nullable=False)
    extracted_value = Column(Text, nullable=False)
    confirmed_value = Column(Text, nullable=True)
    is_valid = Column(Boolean, default=True, nullable=False)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
