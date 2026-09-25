from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme
from app.schemas.eligibility import (
    PersonEligibilityResponse,
    FamilyEligibilityResponse,
)
from app.services.matching_engine import (
    evaluate_person_eligibility,
    evaluate_family_eligibility,
)

from app.core.rate_limiter import rate_limit

router = APIRouter(tags=["Eligibility Matching Engine"])


@router.get(
    "/persons/{person_id}/eligibility",
    response_model=PersonEligibilityResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Evaluate Person Eligibility",
    description="Deterministically evaluates all active TN welfare schemes against an individual's personal and household attributes.",
)
def get_person_eligibility(person_id: UUID, db: Session = Depends(get_db)):
    """Evaluate all active government schemes for a specific person against their family's profile.
    Returns fully eligible schemes, partially eligible schemes with specific missing conditions,
    and count of ineligible schemes.
    """
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id '{person_id}' not found",
        )

    family = db.query(Family).filter(Family.id == person.family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Family record for person '{person_id}' not found",
        )

    active_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    return evaluate_person_eligibility(person, family, active_schemes)


@router.get(
    "/families/{family_id}/eligibility",
    response_model=FamilyEligibilityResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Evaluate Family Household Eligibility",
    description="Evaluates all active TN welfare schemes for all persons within a household family unit.",
)
def get_family_eligibility(family_id: UUID, db: Session = Depends(get_db)):
    """Evaluate all active schemes for all members of a family.
    Returns household-level overview and individual member eligibility results.
    """
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Family with id '{family_id}' not found",
        )

    active_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    return evaluate_family_eligibility(family, active_schemes)
