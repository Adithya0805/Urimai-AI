from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.person import Person
from app.models.family import Family
from app.schemas.person import PersonUpdate, PersonResponse
from app.core.auth import get_optional_user, AuthUser
from app.api.families import verify_family_access

router = APIRouter(prefix="/persons", tags=["Persons"])


@router.get("/{person_id}", response_model=PersonResponse)
def get_person(
    person_id: UUID,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Fetch an individual person by ID with family access verification."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id '{person_id}' not found",
        )

    if person.family:
        verify_family_access(person.family, current_user)

    return person


@router.patch("/{person_id}", response_model=PersonResponse)
def update_person(
    person_id: UUID,
    payload: PersonUpdate,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Partially update an individual person's details with authorization verification."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id '{person_id}' not found",
        )

    if person.family:
        verify_family_access(person.family, current_user)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(person, field, value)

    db.commit()
    db.refresh(person)
    return person
