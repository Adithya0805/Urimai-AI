import uuid
from sqlalchemy import Column, String, Numeric, DateTime, Enum as SQLEnum, func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.enums import CompositionType, RationCardType


class GUID(TypeDecorator):
    """Platform-independent GUID type.
    Uses PostgreSQL's UUID type, otherwise uses CHAR(36), storing as stringified hex values.
    """
    impl = CHAR
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(PG_UUID(as_uuid=True))
        else:
            return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            if isinstance(value, uuid.UUID):
                return str(value)
            else:
                return str(uuid.UUID(str(value)))

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                return uuid.UUID(str(value))
            return value


class Family(Base):
    __tablename__ = "families"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    composition_type = Column(
        SQLEnum(CompositionType, name="composition_type_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    district = Column(String, nullable=False, index=True)
    taluk = Column(String, nullable=False, index=True)
    address = Column(String, nullable=False)
    ration_card_type = Column(
        SQLEnum(RationCardType, name="ration_card_type_enum", native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
    )
    total_household_income = Column(Numeric(12, 2), nullable=False)
    user_id = Column(GUID(), nullable=True, index=True)
    created_by = Column(GUID(), nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    persons = relationship("Person", back_populates="family", cascade="all, delete-orphan", lazy="selectin")
