"""Urimai AI — Production Scheme & Knowledge Base Seeder
=========================================================
Seeds all verified Tamil Nadu government welfare schemes, deterministic rules,
guidance checklists, and bilingual glossary terms into the target database.

Usage:
    python scripts/seed_production.py [--database-url <url>]
"""

import os
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.seed_data import seed_database

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-7s | %(message)s")
logger = logging.getLogger("urimai.seed")


def seed_production(database_url: str):
    logger.info("Connecting to database for scheme seeding...")
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        logger.info("Starting verified scheme data seeding...")
        seed_database(db)
        logger.info("✓ Production database successfully populated with all verified government schemes, rules, and glossaries.")
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    db_url = sys.argv[1] if len(sys.argv) > 1 else (os.getenv("PROD_DATABASE_URL") or os.getenv("DATABASE_URL"))
    if not db_url:
        logger.error("DATABASE_URL or PROD_DATABASE_URL environment variable is required.")
        sys.exit(1)
    seed_production(db_url)
