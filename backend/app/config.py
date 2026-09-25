import os
from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ── Database ──────────────────────────────────────────────────────────────
    DATABASE_URL: Optional[str] = None
    SUPABASE_URL: Optional[str] = None
    SUPABASE_KEY: Optional[str] = None

    # ── Google Gemini (LLM + Embeddings) ─────────────────────────────────────
    GOOGLE_API_KEY: Optional[str] = None

    # ── Pinecone (Vector Store for RAG) ──────────────────────────────────────
    PINECONE_API_KEY: Optional[str] = None
    PINECONE_INDEX_NAME: str = "urimai-schemes"
    PINECONE_ENVIRONMENT: str = "us-east-1-aws"

    # ── RAG / LLM Feature Flags ───────────────────────────────────────────────
    # Set LLM_ENABLED=false to disable LLM layer (pure deterministic mode, no API calls)
    LLM_ENABLED: bool = True
    # Minimum Pinecone similarity score to use RAG context (else fallback to DB)
    RAG_SIMILARITY_THRESHOLD: float = 0.70

    # ── Security & Authentication ─────────────────────────────────────────────
    JWT_SECRET: str = "urimai-ai-super-secure-secret-key-2026"
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000,http://localhost:8000,http://127.0.0.1:8000"

    # ── OTP Security & Throttling ─────────────────────────────────────────────
    OTP_EXPIRY_SECONDS: int = 300
    OTP_MAX_FAILED_ATTEMPTS: int = 5
    OTP_LOCKOUT_SECONDS: int = 600

    # ── Rate Limiting ─────────────────────────────────────────────────────────
    RATE_LIMIT_ENABLED: bool = True

    # ── Error Monitoring & Sentry ─────────────────────────────────────────────
    SENTRY_DSN: Optional[str] = None

    # ── General ───────────────────────────────────────────────────────────────
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() == "production"

    @property
    def is_staging(self) -> bool:
        return self.ENVIRONMENT.lower() == "staging"

    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT.lower() == "development"

    @property
    def llm_available(self) -> bool:
        """True only when required Google API key is present and LLM is enabled."""
        return (
            self.LLM_ENABLED
            and bool(self.GOOGLE_API_KEY)
        )

    @property
    def rag_available(self) -> bool:
        """True only when both Pinecone and Google API keys are present."""
        return (
            self.LLM_ENABLED
            and bool(self.GOOGLE_API_KEY)
            and bool(self.PINECONE_API_KEY)
        )

    def __repr__(self) -> str:
        """Safe string representation that never exposes sensitive credentials."""
        return (
            f"<Settings env={self.ENVIRONMENT} "
            f"db_configured={bool(self.DATABASE_URL or self.SUPABASE_URL)} "
            f"llm_enabled={self.LLM_ENABLED} "
            f"rag_available={self.rag_available}>"
        )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
