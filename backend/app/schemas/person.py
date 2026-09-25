from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import (
    Gender,
    EducationLevel,
    Occupation,
    MaritalStatus,
    CasteCategory,
)


class PersonBase(BaseModel):
    name: str = Field(..., min_length=1, description="Full name of the person")
    age: int = Field(..., gt=0, description="Age must be greater than 0")
    gender: Gender
    education_level: EducationLevel
    occupation: Occupation
    occupation_detail: Optional[str] = Field(None, description="Free text detail, especially when occupation is 'other'")
    marital_status: MaritalStatus
    caste_category: CasteCategory
    disability_status: bool = False
    disability_type: Optional[str] = None
    special_flags: List[str] = Field(default_factory=list, description="Special tags e.g. widow, destitute, folk_artist")
    land_holding_acres: Optional[Decimal] = Field(Decimal("0.0"), description="Agricultural land holding in acres")
    crop_type: Optional[str] = Field(None, description="Primary crop cultivated if farmer, e.g. paddy, millets, etc.")


class PersonCreate(PersonBase):
    pass


class PersonUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    age: Optional[int] = Field(None, gt=0)
    gender: Optional[Gender] = None
    education_level: Optional[EducationLevel] = None
    occupation: Optional[Occupation] = None
    occupation_detail: Optional[str] = None
    marital_status: Optional[MaritalStatus] = None
    caste_category: Optional[CasteCategory] = None
    disability_status: Optional[bool] = None
    disability_type: Optional[str] = None
    special_flags: Optional[List[str]] = None
    land_holding_acres: Optional[Decimal] = None
    crop_type: Optional[str] = None



class PersonResponse(PersonBase):
    id: UUID
    family_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
