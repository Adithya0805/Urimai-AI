import datetime
from typing import List, Optional, Dict, Any
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.enums import ApplicationTrackingStatus, RuleOperator, RuleAppliesTo
from app.models.family import Family
from app.models.person import Person
from app.models.scheme import Scheme, EligibilityRule
from app.models.application_status import (
    ApplicationStatus,
    NotificationLog,
    SchemeReviewQueue,
)
from app.models.intake_log import IntakeExtractionLog
from app.models.admin_audit_log import AdminAuditLog
from app.core.auth import require_admin_user, AuthUser
from app.core.sanitizer import sanitize_text

from app.schemas.application_status import (
    SchemeReviewQueueResponse,
    FreshnessScanResult,
    FollowupScanResult,
    ApplicationStatusResponse,
    NotificationLogResponse,
)
from app.schemas.admin import (
    DashboardStatsResponse,
    AdminAuditLogResponse,
    StuckApplicationItem,
    ErrorLogItem,
    RuleUpdateRequest,
    RuleCreateRequest,
)
from app.schemas.scheme import EligibilityRuleResponse
from app.services.freshness_pipeline import (
    run_freshness_check,
    get_freshness_review_queue,
    verify_and_resolve_scheme_review,
)
from app.services.followup_agent import run_followup_cycle
from app.api.applications import serialize_application_response

router = APIRouter(
    prefix="/admin",
    tags=["Admin Dashboard & Operations"],
    dependencies=[Depends(require_admin_user)],
)


class ReviewResolutionRequest(BaseModel):
    reviewer_notes: str = "Verified against official gazette / portal"
    update_verified_date: bool = True


# ── 1. Overview & Stats ────────────────────────────────────────────────────────
@router.get("/dashboard/stats", response_model=DashboardStatsResponse)
def get_dashboard_stats(db: Session = Depends(get_db)):
    """Provides consolidated high-level system usage and health statistics for administrators."""
    today = datetime.date.today()
    six_months_ago = today - datetime.timedelta(days=180)

    total_families = db.query(func.count(Family.id)).scalar() or 0
    total_persons = db.query(func.count(Person.id)).scalar() or 0
    total_applications = db.query(func.count(ApplicationStatus.id)).scalar() or 0
    active_schemes_count = db.query(func.count(Scheme.id)).filter(Scheme.is_active == True).scalar() or 0

    stale_schemes_count = (
        db.query(func.count(Scheme.id))
        .filter(Scheme.is_active == True)
        .filter((Scheme.last_verified_date == None) | (Scheme.last_verified_date < six_months_ago))
        .scalar()
        or 0
    )

    stuck_applications_count = (
        db.query(func.count(ApplicationStatus.id))
        .filter(
            ApplicationStatus.status.in_([
                ApplicationTrackingStatus.DOCUMENTS_PENDING,
                ApplicationTrackingStatus.RENEWAL_DUE,
            ])
        )
        .scalar()
        or 0
    )

    # Detect schemes with zero tracked applications (signal of potential over-constraining rules)
    all_schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    schemes_zero_matches = []
    for s in all_schemes:
        app_count = db.query(func.count(ApplicationStatus.id)).filter(ApplicationStatus.scheme_id == s.id).scalar() or 0
        if app_count == 0:
            schemes_zero_matches.append({
                "scheme_id": str(s.id),
                "scheme_code": s.scheme_code,
                "name_tamil": s.name_tamil,
                "name_english": s.name_english,
                "department": s.department,
                "rules_count": len(s.rules),
            })

    total_extractions = db.query(func.count(IntakeExtractionLog.id)).scalar() or 0
    recent_errors = db.query(func.count(IntakeExtractionLog.id)).filter(IntakeExtractionLog.is_valid == False).scalar() or 0

    return DashboardStatsResponse(
        total_families=total_families,
        total_persons=total_persons,
        total_applications=total_applications,
        active_schemes_count=active_schemes_count,
        stale_schemes_count=stale_schemes_count,
        stuck_applications_count=stuck_applications_count,
        schemes_zero_matches=schemes_zero_matches[:10],
        total_extractions_logged=total_extractions,
        recent_errors_count=recent_errors,
    )


# ── 2. Scheme Review Queue (Freshness) ──────────────────────────────────────────
@router.get("/freshness/review-queue", response_model=List[SchemeReviewQueueResponse])
def list_review_queue(
    status: Optional[str] = Query("pending_human_review", description="Filter by status"),
    db: Session = Depends(get_db),
):
    """Lists all schemes flagged for manual human re-verification by official administrators."""
    items = get_freshness_review_queue(db, status_filter=status)
    result = []
    for item in items:
        scheme = item.scheme
        result.append(
            SchemeReviewQueueResponse(
                id=item.id,
                scheme_id=item.scheme_id,
                scheme_code=scheme.scheme_code if scheme else "N/A",
                scheme_name_tamil=scheme.name_tamil if scheme else "N/A",
                scheme_name_english=scheme.name_english if scheme else "N/A",
                department=scheme.department if scheme else "N/A",
                source_url=item.source_url,
                last_verified_date=scheme.last_verified_date if scheme else None,
                flagged_reason=item.flagged_reason,
                status=item.status,
                reviewer_notes=item.reviewer_notes,
                created_at=item.created_at,
                reviewed_at=item.reviewed_at,
            )
        )
    return result


@router.post("/freshness/verify/{review_id}", response_model=SchemeReviewQueueResponse)
def resolve_scheme_review(
    review_id: UUID,
    payload: ReviewResolutionRequest,
    request: Request,
    admin: AuthUser = Depends(require_admin_user),
    db: Session = Depends(get_db),
):
    """Admin sign-off on a scheme's re-verification, updating last_verified_date and creating an audit record."""
    try:
        item = verify_and_resolve_scheme_review(
            db,
            review_id=review_id,
            reviewer_notes=payload.reviewer_notes,
            update_verified_date=payload.update_verified_date,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    scheme = item.scheme

    # Record Admin Audit Log
    audit = AdminAuditLog(
        admin_user_id=admin.id,
        admin_email=admin.email or "admin@urimai.tn.gov.in",
        action="SCHEME_REVIEWED",
        entity_type="scheme",
        entity_id=str(scheme.id) if scheme else str(review_id),
        before_value={"status": "pending_human_review"},
        after_value={
            "status": "resolved",
            "reviewer_notes": payload.reviewer_notes,
            "last_verified_date": str(scheme.last_verified_date) if scheme else None,
        },
        ip_address=request.client.host if request.client else None,
    )
    db.add(audit)
    db.commit()

    return SchemeReviewQueueResponse(
        id=item.id,
        scheme_id=item.scheme_id,
        scheme_code=scheme.scheme_code if scheme else "N/A",
        scheme_name_tamil=scheme.name_tamil if scheme else "N/A",
        scheme_name_english=scheme.name_english if scheme else "N/A",
        department=scheme.department if scheme else "N/A",
        source_url=item.source_url,
        last_verified_date=scheme.last_verified_date if scheme else None,
        flagged_reason=item.flagged_reason,
        status=item.status,
        reviewer_notes=item.reviewer_notes,
        created_at=item.created_at,
        reviewed_at=item.reviewed_at,
    )


# ── 3. Stuck Applications Dashboard ───────────────────────────────────────────
@router.get("/applications/stuck", response_model=List[StuckApplicationItem])
def list_stuck_applications(
    days_threshold: int = Query(7, description="Days pending threshold"),
    db: Session = Depends(get_db),
):
    """Returns detailed records of citizen applications stalled in 'documents_pending' or 'renewal_due'."""
    today = datetime.date.today()
    apps = (
        db.query(ApplicationStatus)
        .filter(
            ApplicationStatus.status.in_([
                ApplicationTrackingStatus.DOCUMENTS_PENDING,
                ApplicationTrackingStatus.RENEWAL_DUE,
            ])
        )
        .all()
    )

    stuck_items = []
    for app in apps:
        days_stuck = (today - app.last_updated).days
        if days_stuck >= days_threshold or app.status == ApplicationTrackingStatus.RENEWAL_DUE:
            person = app.person
            family = person.family if person else None
            scheme = app.scheme

            stuck_items.append(
                StuckApplicationItem(
                    id=app.id,
                    person_id=app.person_id,
                    person_name=person.name if person else "N/A",
                    family_id=family.id if family else app.person_id,
                    district=family.district if family else "N/A",
                    scheme_id=app.scheme_id,
                    scheme_code=scheme.scheme_code if scheme else "N/A",
                    scheme_name_tamil=scheme.name_tamil if scheme else "N/A",
                    scheme_name_english=scheme.name_english if scheme else "N/A",
                    department=scheme.department if scheme else "N/A",
                    status=app.status.value,
                    days_stuck=days_stuck,
                    last_updated=app.last_updated,
                    pending_documents=app.pending_documents or [],
                    next_action_note=app.next_action_note,
                )
            )

    return stuck_items


@router.get("/applications/pending-followups", response_model=List[ApplicationStatusResponse])
def list_pending_followup_applications(
    days_pending: int = Query(7, description="Days pending threshold"),
    db: Session = Depends(get_db),
):
    """Admin endpoint: List all applications currently stuck in 'documents_pending' or 'renewal_due'."""
    today = datetime.date.today()
    apps = (
        db.query(ApplicationStatus)
        .filter(
            ApplicationStatus.status.in_([
                ApplicationTrackingStatus.DOCUMENTS_PENDING,
                ApplicationTrackingStatus.RENEWAL_DUE,
            ])
        )
        .all()
    )
    result = []
    for app in apps:
        if app.status == ApplicationTrackingStatus.DOCUMENTS_PENDING:
            if (today - app.last_updated).days >= days_pending:
                result.append(serialize_application_response(app))
        elif app.status == ApplicationTrackingStatus.RENEWAL_DUE:
            result.append(serialize_application_response(app))
    return result


# ── 4. Error Logs & Failure Visibility ────────────────────────────────────────
@router.get("/logs/errors", response_model=List[ErrorLogItem])
def list_error_logs(
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """Retrieves conversational extraction failures and system errors for debugging."""
    failed_extractions = (
        db.query(IntakeExtractionLog)
        .filter(IntakeExtractionLog.is_valid == False)
        .order_by(IntakeExtractionLog.created_at.desc())
        .limit(limit)
        .all()
    )

    return [
        ErrorLogItem(
            id=log.id,
            log_type="extraction_failure",
            session_id=log.session_id,
            raw_input=log.raw_tamil_input,
            target_field=log.target_field,
            error_message=log.error_message,
            created_at=log.created_at,
        )
        for log in failed_extractions
    ]


# ── 5. Admin Audit Trail ──────────────────────────────────────────────────────
@router.get("/audit-logs", response_model=List[AdminAuditLogResponse])
def list_admin_audit_logs(
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """Retrieves the full chronological audit trail of administrative modifications."""
    logs = (
        db.query(AdminAuditLog)
        .order_by(AdminAuditLog.created_at.desc())
        .limit(limit)
        .all()
    )
    return logs


# ── 6. Eligibility Rule Management with Strict Engine Validation & Audit ───────
@router.patch("/schemes/{scheme_id}/rules/{rule_id}", response_model=EligibilityRuleResponse)
def update_eligibility_rule(
    scheme_id: UUID,
    rule_id: UUID,
    payload: RuleUpdateRequest,
    request: Request,
    admin: AuthUser = Depends(require_admin_user),
    db: Session = Depends(get_db),
):
    """Admin edit of an eligibility rule. Enforces strict schema field validation and writes before/after audit log."""
    rule = db.query(EligibilityRule).filter(EligibilityRule.id == rule_id, EligibilityRule.scheme_id == scheme_id).first()
    if not rule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error_code": "RULE_NOT_FOUND",
                "message": f"Eligibility rule with id '{rule_id}' not found for scheme '{scheme_id}'.",
                "message_ta": "விதி விவரங்கள் கிடைக்கவில்லை.",
            },
        )

    # Capture BEFORE state
    before_state = {
        "field_name": rule.field_name,
        "operator": rule.operator.value,
        "value": rule.value,
        "applies_to": rule.applies_to.value,
    }

    # Validate target field existence on models
    target_field = payload.field_name or rule.field_name
    applies_to = payload.applies_to or rule.applies_to

    if applies_to == RuleAppliesTo.PERSON:
        valid_fields = {c.name for c in Person.__table__.columns}
    else:
        valid_fields = {c.name for c in Family.__table__.columns}

    if target_field not in valid_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "error_code": "INVALID_RULE_FIELD",
                "message": f"Field '{target_field}' does not exist on {applies_to.value.capitalize()} model. Valid fields: {sorted(list(valid_fields))}",
                "message_ta": f"'{target_field}' என்ற புலம் தரவுத்தளத்தில் இல்லை.",
            },
        )

    # Apply updates
    if payload.field_name is not None:
        rule.field_name = payload.field_name
    if payload.operator is not None:
        rule.operator = payload.operator
    if payload.value is not None:
        rule.value = payload.value
    if payload.applies_to is not None:
        rule.applies_to = payload.applies_to

    # Capture AFTER state
    after_state = {
        "field_name": rule.field_name,
        "operator": rule.operator.value,
        "value": rule.value,
        "applies_to": rule.applies_to.value,
        "admin_notes": payload.admin_notes,
    }

    # Save Audit Log
    audit = AdminAuditLog(
        admin_user_id=admin.id,
        admin_email=admin.email or "admin@urimai.tn.gov.in",
        action="RULE_UPDATED",
        entity_type="eligibility_rule",
        entity_id=str(rule.id),
        before_value=before_state,
        after_value=after_state,
        ip_address=request.client.host if request.client else None,
    )
    db.add(audit)
    db.commit()
    db.refresh(rule)

    return rule


@router.post("/schemes/{scheme_id}/rules", response_model=EligibilityRuleResponse, status_code=status.HTTP_201_CREATED)
def create_eligibility_rule(
    scheme_id: UUID,
    payload: RuleCreateRequest,
    request: Request,
    admin: AuthUser = Depends(require_admin_user),
    db: Session = Depends(get_db),
):
    """Admin addition of a new eligibility rule with model field validation and audit trail."""
    scheme = db.query(Scheme).filter(Scheme.id == scheme_id).first()
    if not scheme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error_code": "SCHEME_NOT_FOUND", "message": f"Scheme '{scheme_id}' not found."},
        )

    # Validate target field existence
    if payload.applies_to == RuleAppliesTo.PERSON:
        valid_fields = {c.name for c in Person.__table__.columns}
    else:
        valid_fields = {c.name for c in Family.__table__.columns}

    if payload.field_name not in valid_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "error_code": "INVALID_RULE_FIELD",
                "message": f"Field '{payload.field_name}' does not exist on {payload.applies_to.value.capitalize()} model.",
            },
        )

    new_rule = EligibilityRule(
        scheme_id=scheme_id,
        field_name=payload.field_name,
        operator=payload.operator,
        value=payload.value,
        applies_to=payload.applies_to,
    )
    db.add(new_rule)
    db.flush()

    # Record Audit Log
    audit = AdminAuditLog(
        admin_user_id=admin.id,
        admin_email=admin.email or "admin@urimai.tn.gov.in",
        action="RULE_CREATED",
        entity_type="eligibility_rule",
        entity_id=str(new_rule.id),
        before_value=None,
        after_value={
            "scheme_id": str(scheme_id),
            "scheme_code": scheme.scheme_code,
            "field_name": payload.field_name,
            "operator": payload.operator.value,
            "value": payload.value,
            "applies_to": payload.applies_to.value,
            "admin_notes": payload.admin_notes,
        },
        ip_address=request.client.host if request.client else None,
    )
    db.add(audit)
    db.commit()
    db.refresh(new_rule)

    return new_rule


# ── 7. Freshness Pipeline Scans & Followup Triggers ────────────────────────────
@router.post("/freshness/run-check", response_model=FreshnessScanResult)
def trigger_freshness_check(
    threshold_days: int = Query(180, description="Staleness threshold in days"),
    db: Session = Depends(get_db),
):
    """Run scheduled / on-demand freshness inspection across all active schemes."""
    return run_freshness_check(db, threshold_days=threshold_days)


@router.post("/applications/trigger-followups", response_model=FollowupScanResult)
def trigger_followup_agent(
    pending_days_threshold: int = Query(7, description="Days pending threshold for reminders"),
    renewal_window_days: int = Query(30, description="Renewal window in days"),
    channel: str = Query("log", description="Notification channel (log, whatsapp, sms)"),
    db: Session = Depends(get_db),
):
    """Triggers the Follow-up Agent cycle to formulate Tamil reminders."""
    return run_followup_cycle(
        db,
        pending_days_threshold=pending_days_threshold,
        renewal_window_days=renewal_window_days,
        channel=channel,
    )


@router.get("/notifications", response_model=List[NotificationLogResponse])
def list_notifications(
    limit: int = Query(50, description="Limit count"),
    db: Session = Depends(get_db),
):
    """List all follow-up notifications generated for citizens."""
    notifs = (
        db.query(NotificationLog)
        .order_by(NotificationLog.sent_at.desc())
        .limit(limit)
        .all()
    )
    return [
        NotificationLogResponse(
            id=n.id,
            application_id=n.application_id,
            person_id=n.person_id,
            notification_type=n.notification_type,
            channel=n.channel,
            message_tamil=n.message_tamil,
            sent_at=n.sent_at,
            person_name=n.person.name if n.person else None,
        )
        for n in notifs
    ]


@router.get("/security/audit", summary="Audit Database RLS & Security Policies")
def get_security_audit(db: Session = Depends(get_db)):
    """Inspects PostgreSQL Row Level Security (RLS) tables and active security policies."""
    from app.core.security_audit import audit_database_security_policies
    return audit_database_security_policies(db)
