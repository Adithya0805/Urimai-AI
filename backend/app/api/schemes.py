from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.scheme import Scheme, SchemeTermGlossary
from app.schemas.scheme import (
    SchemeSummaryResponse,
    SchemeDetailResponse,
    GlossaryTermResponse,
)

router = APIRouter(tags=["Schemes & Glossary"])


@router.get("/schemes", response_model=List[SchemeSummaryResponse])
def list_schemes(
    department: Optional[str] = Query(None, description="Filter by department"),
    category: Optional[str] = Query(None, description="Filter by scheme category"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    db: Session = Depends(get_db),
):
    """List all available government schemes, with optional filtering by department and category."""
    query = db.query(Scheme)
    if department:
        query = query.filter(Scheme.department.ilike(f"%{department}%"))
    if category:
        query = query.filter(Scheme.category.ilike(f"%{category}%"))
    if is_active is not None:
        query = query.filter(Scheme.is_active == is_active)

    schemes = query.order_by(Scheme.scheme_code).all()
    return schemes


@router.get("/schemes/{scheme_id_or_code}", response_model=SchemeDetailResponse)
def get_scheme(scheme_id_or_code: str, db: Session = Depends(get_db)):
    """Fetch complete details of a scheme, including all associated eligibility rules.
    Supports either UUID id or unique scheme_code (e.g. 'TN-SW-OAP').
    """
    # Check if UUID
    scheme = None
    try:
        val_uuid = UUID(scheme_id_or_code)
        scheme = db.query(Scheme).filter(Scheme.id == val_uuid).first()
    except ValueError:
        pass

    if not scheme:
        # Fallback to scheme_code match
        scheme = db.query(Scheme).filter(Scheme.scheme_code == scheme_id_or_code).first()

    if not scheme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Scheme '{scheme_id_or_code}' not found",
        )

    return scheme


@router.get("/glossary", response_model=List[GlossaryTermResponse])
def list_glossary_terms(
    search: Optional[str] = Query(None, description="Search term in Tamil or English"),
    db: Session = Depends(get_db),
):
    """List bilingual scheme terms, caste categorizations, and welfare vocabulary."""
    query = db.query(SchemeTermGlossary)
    if search:
        query = query.filter(
            (SchemeTermGlossary.tamil_term.ilike(f"%{search}%"))
            | (SchemeTermGlossary.english_equivalent.ilike(f"%{search}%"))
        )
    return query.order_by(SchemeTermGlossary.tamil_term).all()
