import datetime
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.scheme import Scheme
from app.models.application_status import SchemeReviewQueue
from app.schemas.application_status import FreshnessScanResult

DEFAULT_STALENESS_THRESHOLD_DAYS = 180  # 6 months


def run_freshness_check(
    db: Session,
    threshold_days: int = DEFAULT_STALENESS_THRESHOLD_DAYS,
) -> FreshnessScanResult:
    """Scans all active schemes in the database.
    If a scheme's last_verified_date is older than threshold_days (e.g. 180 days / 6 months),
    it flags the scheme for manual human review in the SchemeReviewQueue.

    CRITICAL SAFETY GUARDRAIL:
    This pipeline strictly DOES NOT auto-update or mutate eligibility rules from automated
    web scrapes. Any automated change to eligibility criteria could directly harm vulnerable
    citizens seeking essential welfare benefits. It creates an auditable review queue for human
    administrators.
    """
    schemes = db.query(Scheme).filter(Scheme.is_active == True).all()
    today = datetime.date.today()
    stale_flagged = 0

    for scheme in schemes:
        is_stale = False
        reason = ""

        if not scheme.last_verified_date:
            is_stale = True
            reason = "சரிபார்க்கப்பட்ட தேதி குறிப்பிடப்படவில்லை (Last verified date is missing)."
        else:
            days_old = (today - scheme.last_verified_date).days
            if days_old > threshold_days:
                is_stale = True
                reason = (
                    f"கடைசியாக சரிபார்க்கப்பட்ட தேதி {scheme.last_verified_date} "
                    f"({days_old} நாட்களுக்கு முன்பு — {threshold_days} நாட்களுக்கு மேல்). "
                    f"அதிகாரப்பூர்வ தளத்தில் ({scheme.source_url}) புதிய அரசாணைகள் / விதிகளை சரிபார்க்கவும்."
                )

        if is_stale:
            # Check if already in pending review queue
            existing_queue_item = (
                db.query(SchemeReviewQueue)
                .filter(
                    SchemeReviewQueue.scheme_id == scheme.id,
                    SchemeReviewQueue.status == "pending_human_review",
                )
                .first()
            )

            if not existing_queue_item:
                queue_entry = SchemeReviewQueue(
                    scheme_id=scheme.id,
                    flagged_reason=reason,
                    source_url=scheme.source_url,
                    status="pending_human_review",
                )
                db.add(queue_entry)
                stale_flagged += 1

    db.commit()

    total_pending = (
        db.query(SchemeReviewQueue)
        .filter(SchemeReviewQueue.status == "pending_human_review")
        .count()
    )

    return FreshnessScanResult(
        total_schemes_checked=len(schemes),
        stale_schemes_flagged=stale_flagged,
        review_queue_count=total_pending,
        message=f"Freshness check complete. {stale_flagged} new schemes flagged. Total pending review: {total_pending}.",
    )


def get_freshness_review_queue(
    db: Session,
    status_filter: Optional[str] = "pending_human_review",
) -> List[SchemeReviewQueue]:
    """Retrieve schemes in the freshness review queue."""
    query = db.query(SchemeReviewQueue)
    if status_filter:
        query = query.filter(SchemeReviewQueue.status == status_filter)
    return query.order_by(SchemeReviewQueue.created_at.desc()).all()


def verify_and_resolve_scheme_review(
    db: Session,
    review_id: UUID,
    reviewer_notes: str,
    update_verified_date: bool = True,
) -> SchemeReviewQueue:
    """Administrator human review callback.
    Marks review item as verified and updates scheme's last_verified_date.
    """
    queue_item = (
        db.query(SchemeReviewQueue)
        .filter(SchemeReviewQueue.id == review_id)
        .first()
    )
    if not queue_item:
        raise ValueError(f"Review queue item '{review_id}' not found")

    queue_item.status = "reviewed_verified"
    queue_item.reviewer_notes = reviewer_notes
    queue_item.reviewed_at = datetime.datetime.now(datetime.timezone.utc)

    if update_verified_date and queue_item.scheme:
        queue_item.scheme.last_verified_date = datetime.date.today()

    db.commit()
    db.refresh(queue_item)
    return queue_item
