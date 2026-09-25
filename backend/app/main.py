import time
import uuid
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy import text

from app.config import get_settings
from app.database import engine, Base, SessionLocal
from app.core.logging_config import setup_logging, logger
from app.core.sentry import init_sentry
from app.core.error_handlers import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)

# API Routers
from app.api.auth import router as auth_router
from app.api.families import router as families_router
from app.api.persons import router as persons_router
from app.api.schemes import router as schemes_router
from app.api.eligibility import router as eligibility_router
from app.api.intake import router as intake_router
from app.api.guidance import router as guidance_router
from app.api.applications import router as applications_router
from app.api.admin import router as admin_router
from app.api.whatsapp import router as whatsapp_router
from app.seed_data import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup structured logging & Sentry
    settings = get_settings()
    setup_logging(
        log_level=settings.LOG_LEVEL,
        json_format=settings.is_production,
    )
    init_sentry()
    logger.info(f"Starting Urimai AI backend in [{settings.ENVIRONMENT.upper()}] environment...")

    # Ensure tables are created when running in development/local
    Base.metadata.create_all(bind=engine)

    # Seed knowledge base if not present
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()

    yield

    logger.info("Urimai AI backend shutdown complete.")


settings = get_settings()

app = FastAPI(
    title="Urimai AI — API",
    description="Guidance Agent, Conversational Intake (Tamil), Eligibility Engine & Knowledge Base for Tamil Nadu Welfare Schemes.",
    version="6.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# ── Register Global Exception Handlers ──────────────────────────────────────────
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# ── Configure CORS ─────────────────────────────────────────────────────────────
allowed_origins_list = [orig.strip() for orig in settings.ALLOWED_ORIGINS.split(",") if orig.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins_list if allowed_origins_list else ["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


# ── Request Tracing & Structured Access Logging Middleware ─────────────────────
@app.middleware("http")
async def request_tracing_middleware(request: Request, call_next):
    request_id = request.headers.get("x-request-id") or f"req_{uuid.uuid4().hex[:12]}"
    request.state.request_id = request_id

    start_time = time.time()
    response = await call_next(request)
    duration_ms = round((time.time() - start_time) * 1000, 2)

    # Attach tracing header to response
    response.headers["x-request-id"] = request_id

    # Log request (ignore health check noise in info level)
    if request.url.path not in ["/health", "/"]:
        logger.info(
            f"{request.method} {request.url.path} -> {response.status_code} ({duration_ms}ms) [{request_id}]"
        )

    return response


# ── Include Routers ────────────────────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(families_router)
app.include_router(persons_router)
app.include_router(schemes_router)
app.include_router(eligibility_router)
app.include_router(intake_router)
app.include_router(guidance_router)
app.include_router(applications_router)
app.include_router(admin_router)
app.include_router(whatsapp_router)


# ── Health & Diagnostics ───────────────────────────────────────────────────────
@app.get("/health", tags=["Health & Diagnostics"])
def health_check():
    """Comprehensive health check verifying database connectivity, rate limiter, and service flags."""
    db_status = "healthy"
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception as e:
        logger.error(f"Health check database ping failed: {e}")
        db_status = f"unhealthy: {str(e)}"

    return {
        "status": "healthy" if db_status == "healthy" else "degraded",
        "service": "urimai-ai-backend",
        "environment": settings.ENVIRONMENT,
        "database": db_status,
        "rate_limiting": "enabled" if settings.RATE_LIMIT_ENABLED else "disabled",
        "llm_layer": "available" if settings.llm_available else "fallback_deterministic",
        "rag_vector_store": "available" if settings.rag_available else "database_direct",
    }


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "Urimai AI",
        "description": "Tamil Nadu Government Scheme Eligibility Platform",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "openapi_url": "/openapi.json",
        "version": "6.0.0",
    }
