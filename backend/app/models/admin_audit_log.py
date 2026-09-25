import uuid
from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    JSON,
    func,
)
from app.database import Base
from app.models.family import GUID


class AdminAuditLog(Base):
    __tablename__ = "admin_audit_logs"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    admin_user_id = Column(GUID(), nullable=False, index=True)
    admin_email = Column(String(255), nullable=False)
    action = Column(String(100), nullable=False, index=True)  # e.g. SCHEME_REVIEWED, RULE_UPDATED, RULE_CREATED
    entity_type = Column(String(100), nullable=False, index=True)  # e.g. scheme, eligibility_rule
    entity_id = Column(String(100), nullable=False, index=True)
    before_value = Column(JSON, nullable=True)
    after_value = Column(JSON, nullable=True)
    ip_address = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
