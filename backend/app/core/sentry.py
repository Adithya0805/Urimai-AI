import logging
from typing import Optional
from app.config import get_settings

logger = logging.getLogger("urimai.sentry")


def init_sentry():
    """Initializes Sentry error monitoring if SENTRY_DSN is configured.
    Fails safely and gracefully without blocking application startup if unconfigured or missing.
    """
    settings = get_settings()
    if not settings.SENTRY_DSN:
        logger.debug("Sentry error tracking is disabled (SENTRY_DSN not set).")
        return

    try:
        import sentry_sdk
        from sentry_sdk.integrations.fastapi import FastApiIntegration
        from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            environment=settings.ENVIRONMENT,
            integrations=[
                FastApiIntegration(transaction_style="endpoint"),
                SqlalchemyIntegration(),
            ],
            traces_sample_rate=0.2 if settings.is_production else 1.0,
            profiles_sample_rate=0.1 if settings.is_production else 0.0,
            send_default_pii=False,
        )
        logger.info(f"Sentry initialized successfully for environment: {settings.ENVIRONMENT}")
    except ImportError:
        logger.warning("sentry-sdk is not installed. Error tracking disabled.")
    except Exception as e:
        logger.error(f"Failed to initialize Sentry: {e}")


def capture_exception(exc: Exception, context: Optional[dict] = None):
    """Safely captures an exception to Sentry if available."""
    try:
        import sentry_sdk
        if sentry_sdk.is_initialized():
            if context:
                with sentry_sdk.push_scope() as scope:
                    for key, val in context.items():
                        scope.set_extra(key, val)
                    sentry_sdk.capture_exception(exc)
            else:
                sentry_sdk.capture_exception(exc)
    except Exception:
        pass
