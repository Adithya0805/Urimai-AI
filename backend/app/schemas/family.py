from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import CompositionType, RationCardType
from app.schemas.person import PersonResponse


class FamilyBase(BaseModel):
    composition_type: CompositionType
    district: str = Field(..., min_length=1, description="District in Tamil Nadu")
    taluk: str = Field(..., min_length=1, description="Taluk within the district")
    address: str = Field(..., min_length=1, description="Residential address")
    ration_card_type: RationCardType
    total_household_income: Decimal = Field(..., ge=0, description="Monthly household income")


class FamilyCreate(FamilyBase):
    user_id: Optional[UUID] = None
    created_by: Optional[UUID] = None


class FamilyUpdate(BaseModel):
    composition_type: Optional[CompositionType] = None
    district: Optional[str] = Field(None, min_length=1)
    taluk: Optional[str] = Field(None, min_length=1)
    address: Optional[str] = Field(None, min_length=1)
    ration_card_type: Optional[RationCardType] = None
    total_household_income: Optional[Decimal] = Field(None, ge=0)
    user_id: Optional[UUID] = None


class FamilyResponse(FamilyBase):
    id: UUID
    user_id: Optional[UUID] = None
    created_by: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FamilyDetailResponse(FamilyResponse):
    persons: List[PersonResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)

