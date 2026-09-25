import uuid
from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
    func,
)
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.family import GUID
from app.models.enums import RuleOperator, RuleAppliesTo, ApplicationMode
from sqlalchemy import JSON


class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    scheme_code = Column(String(100), unique=True, nullable=False, index=True)
    name_english = Column(String(255), nullable=False)
    name_tamil = Column(String(255), nullable=False)
    name_transliteration = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False, index=True)
    category = Column(String(100), nullable=False, index=True)
    description_english = Column(Text, nullable=False)
    description_tamil = Column(Text, nullable=False)
    benefit_amount = Column(String(255), nullable=False)
    source_url = Column(String(500), nullable=False)
    last_verified_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Phase 5 Guidance Fields
    required_documents = Column(JSON, default=list, nullable=False)
    application_office = Column(String(255), nullable=False, default="வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்")
    application_mode = Column(
        SQLEnum(
            ApplicationMode,
            name="application_mode_enum",
            native_enum=False,
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
        default=ApplicationMode.BOTH,
    )
    online_application_url = Column(String(500), nullable=True)
    processing_time_estimate = Column(String(100), nullable=False, default="15 முதல் 30 நாட்கள்")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


    # Relationships
    rules = relationship(
        "EligibilityRule",
        back_populates="scheme",
        cascade="all, delete-orphan",
        lazy="selectin",
        order_by="EligibilityRule.id",
    )


class EligibilityRule(Base):
    __tablename__ = "eligibility_rules"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    scheme_id = Column(
        GUID(),
        ForeignKey("schemes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    field_name = Column(String(100), nullable=False)
    operator = Column(
        SQLEnum(
            RuleOperator,
            name="rule_operator_enum",
            native_enum=False,
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
    )
    value = Column(String(255), nullable=False)
    applies_to = Column(
        SQLEnum(
            RuleAppliesTo,
            name="rule_applies_to_enum",
            native_enum=False,
            values_callable=lambda obj: [e.value for e in obj],
        ),
        nullable=False,
    )

    # Relationships
    scheme = relationship("Scheme", back_populates="rules")


class SchemeTermGlossary(Base):
    __tablename__ = "scheme_term_glossary"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    tamil_term = Column(String(255), nullable=False, index=True)
    english_equivalent = Column(String(255), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
