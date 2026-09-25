import uuid
import logging
from datetime import datetime, timezone
from typing import Union
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.sentry import capture_exception

logger = logging.getLogger("urimai.errors")

# Default citizen-safe Tamil messages by HTTP status code
DEFAULT_TAMIL_MESSAGES = {
    400: "தவறான உள்ளீடு. தயவுசெய்து உங்கள் விவரங்களை சரிபார்க்கவும்.",
    401: "அங்கீகாரம் தேவை. தயவுசெய்து உங்கள் தொலைபேசி எண் மூலம் உள்நுழையவும்.",
    403: "அனுமதி மறுக்கப்பட்டது. இந்த விவரங்களை அணுக உங்களுக்கு அனுமதி இல்லை.",
    404: "கோரப்பட்ட விவரங்கள் கிடைக்கவில்லை.",
    409: "முரண்பாடு ஏற்பட்டது. இந்த பதிவு ஏற்கனவே உள்ளது.",
    422: "உள்ளீடு தரவுகளில் பிழை உள்ளது. தேவையான விவரங்களை சரியாக உள்ளிடவும்.",
    429: "அதிகமான கோரிக்கைகள். சிறிது நேரம் காத்திருந்து மீண்டும் முயற்சிக்கவும்.",
    500: "சேவையகத்தில் தற்காலிக பிழை ஏற்பட்டுள்ளது. சிறிது நேரம் கழித்து முயற்சிக்கவும்.",
    502: "இணைப்பு பிழை. சிறிது நேரம் கழித்து முயற்சிக்கவும்.",
    503: "சேவை தற்காலிகமாக கிடைக்கவில்லை. பின்னர் முயற்சிக்கவும்.",
}

ERROR_CODES = {
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    409: "CONFLICT",
    422: "VALIDATION_ERROR",
    429: "RATE_LIMITED",
    500: "INTERNAL_SERVER_ERROR",
}


def get_request_id(request: Request) -> str:
    """Retrieve or generate request ID."""
    return getattr(request.state, "request_id", None) or f"req_{uuid.uuid4().hex[:12]}"


async def http_exception_handler(request: Request, exc: Union[HTTPException, StarletteHTTPException]) -> JSONResponse:
    """Handler for standard FastAPI/Starlette HTTP exceptions."""
    status_code = exc.status_code
    req_id = get_request_id(request)

    # Extract detail
    if isinstance(exc.detail, dict):
        message = exc.detail.get("message", exc.detail.get("detail", str(exc.detail)))
        message_ta = exc.detail.get("message_ta", DEFAULT_TAMIL_MESSAGES.get(status_code, DEFAULT_TAMIL_MESSAGES[500]))
        error_code = exc.detail.get("error_code", ERROR_CODES.get(status_code, "HTTP_ERROR"))
        details = exc.detail.get("details", None)
    else:
        message = str(exc.detail) if exc.detail else "An error occurred"
        message_ta = DEFAULT_TAMIL_MESSAGES.get(status_code, DEFAULT_TAMIL_MESSAGES[500])
        error_code = ERROR_CODES.get(status_code, f"HTTP_{status_code}")
        details = None

    if status_code >= 500:
        logger.error(
            f"HTTP {status_code} Error on {request.method} {request.url.path} [{req_id}]: {message}",
            exc_info=True,
        )
    else:
        logger.warning(
            f"HTTP {status_code} Warning on {request.method} {request.url.path} [{req_id}]: {message}"
        )

    return JSONResponse(
        status_code=status_code,
        content={
            "error_code": error_code,
            "message": message,
            "detail": message,  # Backward-compatible for standard FastAPI clients
            "message_ta": message_ta,
            "request_id": req_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "details": details,
        },
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Handler for FastAPI Pydantic schema validation errors."""
    req_id = get_request_id(request)
    errors = exc.errors()

    logger.warning(
        f"Validation error on {request.method} {request.url.path} [{req_id}]: {len(errors)} field error(s)"
    )

    clean_errors = []
    for err in errors:
        loc = [str(x) for x in err.get("loc", []) if str(x) != "body"]
        clean_errors.append({
            "field": ".".join(loc),
            "issue": err.get("msg", "Invalid value"),
            "type": err.get("type", "validation_error"),
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error_code": "VALIDATION_ERROR",
            "message": "Input validation failed. Please review the highlighted fields.",
            "detail": "Input validation failed",
            "message_ta": "உள்ளீடு தரவுகளில் பிழை உள்ளது. தயவுசெய்து விவரங்களை சரிபார்க்கவும்.",
            "request_id": req_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "details": clean_errors,
        },
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Fallback handler for unhandled internal server exceptions."""
    req_id = get_request_id(request)

    # Capture in Sentry
    capture_exception(exc, context={"request_id": req_id, "path": request.url.path, "method": request.method})

    logger.error(
        f"Unhandled 500 error on {request.method} {request.url.path} [{req_id}]: {exc}",
        exc_info=True,
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error_code": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected server error occurred. Please try again shortly.",
            "detail": "Internal server error",
            "message_ta": "சேவையகத்தில் தற்காலிக பிழை ஏற்பட்டுள்ளது. சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்.",
            "request_id": req_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "details": None,
        },
    )
