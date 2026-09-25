from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.family import Family
from app.core.auth import (
    send_phone_otp,
    verify_phone_otp,
    authenticate_admin,
    get_current_user,
    AuthUser,
)
from app.core.rate_limiter import rate_limit
from app.core.sanitizer import sanitize_phone

router = APIRouter(prefix="/auth", tags=["Authentication & Session"])


class SendOtpRequest(BaseModel):
    phone: str = Field(..., json_schema_extra={"example": "+919444123456"}, description="10-digit mobile number with country code")


class VerifyOtpRequest(BaseModel):
    phone: str = Field(..., json_schema_extra={"example": "+919444123456"})
    otp: str = Field(..., json_schema_extra={"example": "123456"}, description="6-digit one-time password")


class AdminLoginRequest(BaseModel):
    email: str = Field(..., json_schema_extra={"example": "admin@urimai.tn.gov.in"}, description="Administrator email address")
    password: str = Field(..., json_schema_extra={"example": "Admin@Urimai2026!"}, description="Administrator secret password")


class UserMeResponse(BaseModel):
    id: str
    phone: str = ""
    email: Optional[str] = None
    role: str
    is_volunteer: bool
    family_ids: List[str] = []


@router.post(
    "/admin/login",
    dependencies=[Depends(rate_limit(max_requests=10, window_seconds=60))],
    summary="Administrator Login",
    description="Authenticates official welfare department administrators via secure email/password credentials, separate from citizen OTP.",
)
def login_admin(payload: AdminLoginRequest, response: Response):
    """Admin login with email and password."""
    result = authenticate_admin(payload.email, payload.password)
    token = result["access_token"]

    # Set secure httpOnly cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=7 * 24 * 3600,
        samesite="lax",
        secure=False,
    )

    return result


@router.post(
    "/phone/send-otp",
    dependencies=[Depends(rate_limit(max_requests=10, window_seconds=60))],
    summary="Request Phone OTP",
    description="Generates and sends a 6-digit OTP to the specified mobile phone number. Subject to throttling.",
)
def request_otp(payload: SendOtpRequest):
    """Request a 6-digit OTP to mobile phone number."""
    cleaned_phone = sanitize_phone(payload.phone)
    if not cleaned_phone or len(cleaned_phone.replace("+91", "").replace("+", "")) < 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error_code": "INVALID_PHONE_NUMBER",
                "message": "Please provide a valid 10-digit mobile number.",
                "message_ta": "சரியான 10 இலக்க தொலைபேசி எண்ணை உள்ளிடவும்.",
            },
        )
    return send_phone_otp(cleaned_phone)


@router.post(
    "/phone/verify-otp",
    dependencies=[Depends(rate_limit(max_requests=15, window_seconds=60))],
    summary="Verify OTP & Authenticate",
    description="Validates OTP, issues JWT session token, and sets httpOnly secure cookie. Protected against brute force.",
)
def login_with_otp(payload: VerifyOtpRequest, response: Response):
    """Verify phone OTP, generate session token, and set secure httpOnly cookie."""
    cleaned_phone = sanitize_phone(payload.phone)
    result = verify_phone_otp(cleaned_phone, payload.otp)
    token = result["access_token"]

    # Set secure httpOnly cookie for web browser session persistence
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=7 * 24 * 3600,  # 7 days
        samesite="lax",
        secure=False,  # Set to True in production HTTPS
    )

    return result


@router.get(
    "/me",
    response_model=UserMeResponse,
    summary="Get Authenticated User Profile",
    description="Returns authenticated citizen/volunteer profile and list of owned/managed family IDs.",
)
def get_me(
    current_user: AuthUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return authenticated user profile and list of managed family IDs."""
    # Find all families owned by this user or created by this volunteer
    families = (
        db.query(Family)
        .filter((Family.user_id == current_user.id) | (Family.created_by == current_user.id))
        .all()
    )
    family_ids = [str(f.id) for f in families]

    return UserMeResponse(
        id=str(current_user.id),
        phone=current_user.phone,
        role=current_user.role,
        is_volunteer=current_user.is_volunteer,
        family_ids=family_ids,
    )


@router.post(
    "/logout",
    summary="Logout Citizen Session",
    description="Clears httpOnly authentication cookie and ends user session.",
)
def logout(response: Response):
    """Clear session cookie and log out."""
    response.delete_cookie("access_token")
    return {"status": "success", "message": "Logged out successfully"}
