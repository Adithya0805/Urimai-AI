from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme
from app.schemas.guidance import PersonGuidanceResponse, FamilyGuidanceResponse
from app.services.guidance_service import (
    generate_person_guidance,
    generate_family_guidance,
)
from app.core.rate_limiter import rate_limit

router = APIRouter(tags=["Guidance Agent"])


@router.get(
    "/persons/{person_id}/guidance",
    response_model=PersonGuidanceResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Generate Individual Action Plan & Guidance",
    description="Produces Tamil step-by-step instructions, official document checklists, office locations, and gap analyses for an individual.",
)
def get_person_guidance(person_id: UUID, db: Session = Depends(get_db)):
    """Generate a complete step-by-step guidance package in Tamil for an individual.
    Includes:
    - Step-by-step application instructions and official document checklists for eligible schemes
    - Detailed condition gap analysis and resolution guidance for partially eligible schemes
    - Staleness disclaimer if scheme verified > 6 months ago.
    """
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error_code": "PERSON_NOT_FOUND",
                "message": f"Person with id '{person_id}' not found",
                "message_ta": "குறிப்பிட்ட நபர் பற்றிய விவரங்கள் கிடைக்கவில்லை.",
            },
        )

    family = db.query(Family).filter(Family.id == person.family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error_code": "FAMILY_NOT_FOUND",
                "message": f"Family record for person '{person_id}' not found",
                "message_ta": "குடும்ப விவரங்கள் கிடைக்கவில்லை.",
            },
        )

    active_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    return generate_person_guidance(person, family, active_schemes, db=db)


@router.get(
    "/families/{family_id}/guidance",
    response_model=FamilyGuidanceResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Generate Household Guidance Package",
    description="Produces complete step-by-step guidance packages in Tamil for all members of a family.",
)
def get_family_guidance(family_id: UUID, db: Session = Depends(get_db)):
    """Generate complete step-by-step guidance packages in Tamil for all members of a family."""
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error_code": "FAMILY_NOT_FOUND",
                "message": f"Family with id '{family_id}' not found",
                "message_ta": "குடும்ப விவரங்கள் கிடைக்கவில்லை.",
            },
        )

    active_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    return generate_family_guidance(family, active_schemes, db=db)
