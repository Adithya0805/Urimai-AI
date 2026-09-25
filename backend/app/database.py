import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from app.config import get_settings

settings = get_settings()

raw_db_url = settings.DATABASE_URL or "sqlite:///./urimai_local.db"

# Handle Heroku / Supabase style postgres:// url to postgresql:// for SQLAlchemy
if raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)

connect_args = {}
if raw_db_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(raw_db_url, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
