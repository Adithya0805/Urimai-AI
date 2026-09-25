from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.family import Family
from app.models.person import Person
from app.schemas.family import (
    FamilyCreate,
    FamilyUpdate,
    FamilyResponse,
    FamilyDetailResponse,
)
from app.schemas.person import PersonCreate, PersonResponse
from app.core.auth import get_current_user, get_optional_user, AuthUser

router = APIRouter(prefix="/families", tags=["Families"])


def verify_family_access(family: Family, user: Optional[AuthUser]) -> None:
    """Enforces per-family ownership and volunteer delegation isolation."""
    # If family is linked to a user account, enforce security
    if family.user_id:
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required to access this family record.",
            )
        is_owner = (family.user_id == user.id)
        is_creator = (family.created_by == user.id)
        is_volunteer = user.is_volunteer
        if not (is_owner or is_creator or is_volunteer):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. You do not have permission to view or manage another citizen's family record.",
            )


@router.post("", response_model=FamilyResponse, status_code=status.HTTP_201_CREATED)
def create_family(
    payload: FamilyCreate,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Create a new household / family record, linked to authenticated user."""
    target_user_id = payload.user_id or (current_user.id if current_user else None)
    created_by_id = payload.created_by or (current_user.id if current_user else None)

    family = Family(
        composition_type=payload.composition_type,
        district=payload.district,
        taluk=payload.taluk,
        address=payload.address,
        ration_card_type=payload.ration_card_type,
        total_household_income=payload.total_household_income,
        user_id=target_user_id,
        created_by=created_by_id,
    )
    db.add(family)
    db.commit()
    db.refresh(family)
    return family


@router.get("", response_model=List[FamilyResponse])
def list_my_families(
    current_user: AuthUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all families owned by current user or created by community volunteer."""
    if current_user.is_volunteer:
        families = db.query(Family).filter(
            (Family.user_id == current_user.id) | (Family.created_by == current_user.id)
        ).all()
    else:
        families = db.query(Family).filter(Family.user_id == current_user.id).all()
    return families


@router.get("/{family_id}", response_model=FamilyDetailResponse)
def get_family(
    family_id: UUID,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Fetch family by ID along with member list. Enforces ownership isolation."""
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Family with id '{family_id}' not found",
        )
    verify_family_access(family, current_user)
    return family


@router.patch("/{family_id}", response_model=FamilyResponse)
def update_family(
    family_id: UUID,
    payload: FamilyUpdate,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Partially update family information with authorization verification."""
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Family with id '{family_id}' not found",
        )
    verify_family_access(family, current_user)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(family, field, value)

    db.commit()
    db.refresh(family)
    return family


@router.post(
    "/{family_id}/persons",
    response_model=PersonResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_person_to_family(
    family_id: UUID,
    payload: PersonCreate,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Add a new member to an existing family with ownership verification."""
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot add person. Family with id '{family_id}' does not exist",
        )
    verify_family_access(family, current_user)

    person = Person(
        family_id=family_id,
        name=payload.name,
        age=payload.age,
        gender=payload.gender,
        education_level=payload.education_level,
        occupation=payload.occupation,
        occupation_detail=payload.occupation_detail,
        marital_status=payload.marital_status,
        caste_category=payload.caste_category,
        disability_status=payload.disability_status,
        disability_type=payload.disability_type,
        special_flags=payload.special_flags,
        land_holding_acres=payload.land_holding_acres,
        crop_type=payload.crop_type,
    )
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@router.get("/{family_id}/persons", response_model=List[PersonResponse])
def list_family_persons(
    family_id: UUID,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """List all persons belonging to a specific family with access verification."""
    family = db.query(Family).filter(Family.id == family_id).first()
    if not family:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Family with id '{family_id}' not found",
        )
    verify_family_access(family, current_user)

    persons = db.query(Person).filter(Person.family_id == family_id).all()
    return persons
