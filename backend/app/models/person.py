import uuid
from sqlalchemy import (
    Column,
    String,
    Integer,
    Numeric,
    Boolean,
    DateTime,
    ForeignKey,
    JSON,
    Enum as SQLEnum,
    func,
)
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.family import GUID
from app.models.enums import (
    Gender,
    EducationLevel,
    Occupation,
    MaritalStatus,
    CasteCategory,
)


class Person(Base):
    __tablename__ = "persons"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    family_id = Column(
        GUID(),
        ForeignKey("families.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(
        SQLEnum(Gender, name="gender_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    education_level = Column(
        SQLEnum(EducationLevel, name="education_level_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    occupation = Column(
        SQLEnum(Occupation, name="occupation_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    occupation_detail = Column(String, nullable=True)
    marital_status = Column(
        SQLEnum(MaritalStatus, name="marital_status_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    caste_category = Column(
        SQLEnum(CasteCategory, name="caste_category_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    disability_status = Column(Boolean, default=False, nullable=False)
    disability_type = Column(String, nullable=True)
    special_flags = Column(JSON, default=list, nullable=False)
    land_holding_acres = Column(Numeric(6, 2), nullable=True, default=0.0)
    crop_type = Column(String(100), nullable=True, default=None)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    family = relationship("Family", back_populates="persons")
