from datetime import datetime, timezone
from typing import Any, List, Optional
from pydantic import BaseModel, Field


class StandardErrorResponse(BaseModel):
    """Unified error response contract across all Urimai AI backend endpoints."""

    error_code: str = Field(
        ...,
        description="Standardized machine-readable error identifier (e.g. NOT_FOUND, VALIDATION_ERROR, RATE_LIMITED)",
        example="NOT_FOUND",
    )
    message: str = Field(
        ...,
        description="Human-readable English description of the error",
        example="Family record not found",
    )
    message_ta: str = Field(
        ...,
        description="Safe, plain-Tamil explanation suitable for direct presentation to citizens",
        example="குடும்ப விவரங்கள் கிடைக்கவில்லை.",
    )
    request_id: str = Field(
        ...,
        description="Unique request tracing ID for support and error tracking",
        example="req_01h8abc123",
    )
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
        description="ISO 8601 UTC timestamp of the error event",
    )
    details: Optional[Any] = Field(
        default=None,
        description="Optional field-level validation errors or non-sensitive debug context",
    )
