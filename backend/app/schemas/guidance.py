from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import ApplicationMode


class EligibleSchemeGuidance(BaseModel):
    scheme_id: UUID
    scheme_code: str
    name_english: str
    name_tamil: str
    benefit_amount: str
    benefit_summary_tamil: str
    required_documents: List[str]
    where_to_apply_tamil: str
    application_mode: ApplicationMode
    online_application_url: Optional[str] = None
    processing_time_estimate: str
    steps_tamil: List[str]
    is_stale: bool = False
    disclaimer_tamil: Optional[str] = None
    used_rag: bool = False
    rag_retrieval_score: Optional[float] = None
    retrieval_source: str = "structured_data_only"

    model_config = ConfigDict(from_attributes=True)


class PartiallyEligibleSchemeGuidance(BaseModel):
    scheme_id: UUID
    scheme_code: str
    name_english: str
    name_tamil: str
    benefit_amount: str
    missing_conditions_tamil: List[str]
    how_to_resolve_tamil: List[str]
    is_stale: bool = False
    disclaimer_tamil: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class PersonGuidanceResponse(BaseModel):
    person_id: UUID
    person_name: str
    family_id: UUID
    eligible_schemes_count: int
    partially_eligible_schemes_count: int
    ineligible_schemes_count: int
    eligible_schemes_guidance: List[EligibleSchemeGuidance] = Field(default_factory=list)
    partially_eligible_schemes_guidance: List[PartiallyEligibleSchemeGuidance] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


class FamilyGuidanceResponse(BaseModel):
    family_id: UUID
    district: str
    taluk: str
    total_household_income: Decimal
    total_persons: int
    persons_guidance: List[PersonGuidanceResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
