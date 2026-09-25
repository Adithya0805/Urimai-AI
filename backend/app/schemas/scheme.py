from datetime import date, datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import RuleOperator, RuleAppliesTo


class EligibilityRuleBase(BaseModel):
    field_name: str = Field(..., description="Target field in Person or Family model")
    operator: RuleOperator
    value: str = Field(..., description="Comparison value as string")
    applies_to: RuleAppliesTo


class EligibilityRuleCreate(EligibilityRuleBase):
    pass


class EligibilityRuleResponse(EligibilityRuleBase):
    id: UUID
    scheme_id: UUID

    model_config = ConfigDict(from_attributes=True)


from app.models.enums import RuleOperator, RuleAppliesTo, ApplicationMode


class SchemeBase(BaseModel):
    scheme_code: str = Field(..., description="Unique scheme identifier code")
    name_english: str
    name_tamil: str
    name_transliteration: str
    department: str
    category: str
    description_english: str
    description_tamil: str
    benefit_amount: str
    source_url: str
    last_verified_date: date
    is_active: bool = True
    required_documents: List[str] = Field(default_factory=list)
    application_office: str = "வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்"
    application_mode: ApplicationMode = ApplicationMode.BOTH
    online_application_url: Optional[str] = None
    processing_time_estimate: str = "15 முதல் 30 நாட்கள்"


class SchemeCreate(SchemeBase):
    rules: List[EligibilityRuleCreate] = Field(default_factory=list)



class SchemeSummaryResponse(SchemeBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SchemeDetailResponse(SchemeSummaryResponse):
    rules: List[EligibilityRuleResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


class GlossaryTermBase(BaseModel):
    tamil_term: str
    english_equivalent: str
    notes: Optional[str] = None


class GlossaryTermCreate(GlossaryTermBase):
    pass


class GlossaryTermResponse(GlossaryTermBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
