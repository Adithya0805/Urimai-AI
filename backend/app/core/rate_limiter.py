import time
import threading
from collections import defaultdict
from typing import Callable, Dict, List, Optional
from fastapi import Request, HTTPException, status
from app.config import get_settings


class SlidingWindowRateLimiter:
    """Thread-safe in-memory sliding window rate limiter."""

    def __init__(self):
        self._lock = threading.Lock()
        # Key: str -> List of timestamps
        self._requests: Dict[str, List[float]] = defaultdict(list)

    def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> bool:
        settings = get_settings()
        if not settings.RATE_LIMIT_ENABLED:
            return True

        now = time.time()
        cutoff = now - window_seconds

        with self._lock:
            # Filter out timestamps older than the sliding window
            self._requests[key] = [t for t in self._requests[key] if t > cutoff]

            if len(self._requests[key]) >= max_requests:
                return False

            self._requests[key].append(now)
            return True

    def reset(self, key: Optional[str] = None):
        """Reset rate limiter state (useful for tests)."""
        with self._lock:
            if key:
                self._requests.pop(key, None)
            else:
                self._requests.clear()


# Global limiter instance
limiter = SlidingWindowRateLimiter()


def get_client_ip(request: Request) -> str:
    """Extract client IP from headers (supporting proxies/load balancers) or client host."""
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown_client"


def rate_limit(
    max_requests: int = 60,
    window_seconds: int = 60,
    key_func: Optional[Callable[[Request], str]] = None,
):
    """FastAPI Dependency for rate limiting endpoints.

    Usage:
        @router.post("/message", dependencies=[Depends(rate_limit(max_requests=30, window_seconds=60))])
    """

    async def dependency(request: Request):
        settings = get_settings()
        if not settings.RATE_LIMIT_ENABLED:
            return

        key = key_func(request) if key_func else f"{get_client_ip(request)}:{request.url.path}"

        if not limiter.is_allowed(key, max_requests, window_seconds):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={
                    "error_code": "RATE_LIMITED",
                    "message": f"Rate limit exceeded. Maximum {max_requests} requests per {window_seconds}s allowed.",
                    "message_ta": "அதிகமான கோரிக்கைகள் அனுப்பப்பட்டுள்ளன. சிறிது நேரம் காத்திருந்து மீண்டும் முயற்சிக்கவும்.",
                },
            )

    return dependency
