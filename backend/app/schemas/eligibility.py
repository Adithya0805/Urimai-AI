from decimal import Decimal
from typing import List, Optional, Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import RuleOperator, RuleAppliesTo


class FailedRuleDetail(BaseModel):
    field_name: str
    operator: RuleOperator
    expected_value: str
    actual_value: Optional[str] = None
    applies_to: RuleAppliesTo
    reason: str


class EligibleSchemeItem(BaseModel):
    scheme_id: UUID
    scheme_code: str
    name_english: str
    name_tamil: str
    department: str
    category: str
    benefit_amount: str
    source_url: str
    matched_rules_count: int
    total_rules_count: int

    model_config = ConfigDict(from_attributes=True)


class PartiallyEligibleSchemeItem(BaseModel):
    scheme_id: UUID
    scheme_code: str
    name_english: str
    name_tamil: str
    department: str
    category: str
    benefit_amount: str
    source_url: str
    matched_rules_count: int
    total_rules_count: int
    failed_rules: List[FailedRuleDetail]

    model_config = ConfigDict(from_attributes=True)


class PersonEligibilityResponse(BaseModel):
    person_id: UUID
    person_name: str
    family_id: UUID
    eligible_schemes: List[EligibleSchemeItem] = Field(default_factory=list)
    partially_eligible_schemes: List[PartiallyEligibleSchemeItem] = Field(default_factory=list)
    ineligible_schemes_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class FamilyEligibilityResponse(BaseModel):
    family_id: UUID
    district: str
    taluk: str
    total_household_income: Decimal
    total_persons: int
    persons_eligibility: List[PersonEligibilityResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
