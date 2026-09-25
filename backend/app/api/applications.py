import datetime
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.person import Person
from app.models.scheme import Scheme
from app.models.application_status import ApplicationStatus
from app.schemas.application_status import (
    ApplicationStatusCreate,
    ApplicationStatusUpdate,
    ApplicationStatusResponse,
)

router = APIRouter(tags=["Application Tracking"])


def serialize_application_response(app: ApplicationStatus) -> ApplicationStatusResponse:
    return ApplicationStatusResponse(
        id=app.id,
        person_id=app.person_id,
        scheme_id=app.scheme_id,
        status=app.status,
        last_updated=app.last_updated,
        next_action_note=app.next_action_note,
        pending_documents=app.pending_documents or [],
        renewal_due_date=app.renewal_due_date,
        created_at=app.created_at,
        updated_at=app.updated_at,
        person_name=app.person.name if app.person else None,
        scheme_code=app.scheme.scheme_code if app.scheme else None,
        scheme_name_tamil=app.scheme.name_tamil if app.scheme else None,
        scheme_name_english=app.scheme.name_english if app.scheme else None,
    )


@router.post(
    "/applications",
    response_model=ApplicationStatusResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application_tracking(
    payload: ApplicationStatusCreate,
    db: Session = Depends(get_db),
):
    """Start tracking a government scheme application for a person."""
    person = db.query(Person).filter(Person.id == payload.person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id '{payload.person_id}' not found",
        )

    scheme = db.query(Scheme).filter(Scheme.id == payload.scheme_id).first()
    if not scheme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Scheme with id '{payload.scheme_id}' not found",
        )

    # If pending_documents not explicitly provided, initialize with scheme.required_documents
    pending_docs = payload.pending_documents
    if not pending_docs and scheme.required_documents:
        pending_docs = list(scheme.required_documents)

    app = ApplicationStatus(
        person_id=payload.person_id,
        scheme_id=payload.scheme_id,
        status=payload.status,
        next_action_note=payload.next_action_note,
        pending_documents=pending_docs,
        renewal_due_date=payload.renewal_due_date,
        last_updated=datetime.date.today(),
    )
    db.add(app)
    db.commit()
    db.refresh(app)
    return serialize_application_response(app)


@router.get("/applications/{application_id}", response_model=ApplicationStatusResponse)
def get_application(application_id: UUID, db: Session = Depends(get_db)):
    """Fetch tracked application status by ID."""
    app = db.query(ApplicationStatus).filter(ApplicationStatus.id == application_id).first()
    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with id '{application_id}' not found",
        )
    return serialize_application_response(app)


@router.patch("/applications/{application_id}", response_model=ApplicationStatusResponse)
def update_application(
    application_id: UUID,
    payload: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
):
    """Update application status, submitted documents, or next action note."""
    app = db.query(ApplicationStatus).filter(ApplicationStatus.id == application_id).first()
    if not app:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with id '{application_id}' not found",
        )

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(app, field, value)

    app.last_updated = payload.last_updated or datetime.date.today()
    db.commit()
    db.refresh(app)
    return serialize_application_response(app)


@router.get(
    "/persons/{person_id}/applications",
    response_model=List[ApplicationStatusResponse],
)
def list_person_applications(person_id: UUID, db: Session = Depends(get_db)):
    """List all tracked scheme applications for a specific person."""
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Person with id '{person_id}' not found",
        )

    apps = (
        db.query(ApplicationStatus)
        .filter(ApplicationStatus.person_id == person_id)
        .order_by(ApplicationStatus.created_at.desc())
        .all()
    )
    return [serialize_application_response(a) for a in apps]
