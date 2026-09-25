"""Urimai AI — Production Database Migration Runner
==================================================
Applies all foundational, scheme, guidance, tracking, auth, and admin RLS migrations
sequentially against the production Supabase/PostgreSQL instance.

Usage:
    python scripts/migrate_production.py [--database-url <url>]
"""

import os
import sys
import glob
import logging
from pathlib import Path
from sqlalchemy import create_engine, text

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-7s | %(message)s")
logger = logging.getLogger("urimai.migration")

MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"


def get_production_database_url() -> str:
    url = os.getenv("PROD_DATABASE_URL") or os.getenv("DATABASE_URL")
    if not url:
        logger.error("DATABASE_URL or PROD_DATABASE_URL environment variable is required.")
        sys.exit(1)
    return url


def run_migrations(database_url: str):
    logger.info(f"Connecting to database target...")
    engine = create_engine(database_url, isolation_level="AUTOCOMMIT")

    migration_files = sorted(glob.glob(str(MIGRATIONS_DIR / "*.sql")))
    if not migration_files:
        logger.error(f"No SQL migration files found in {MIGRATIONS_DIR}")
        sys.exit(1)

    logger.info(f"Found {len(migration_files)} migration files to execute.")

    with engine.connect() as conn:
        for filepath in migration_files:
            filename = os.path.basename(filepath)
            logger.info(f"Applying migration: {filename}...")

            with open(filepath, "r", encoding="utf-8") as f:
                sql_content = f.read()

            try:
                # Execute migration SQL script
                conn.execute(text(sql_content))
                logger.info(f"✓ Migration {filename} applied successfully.")
            except Exception as e:
                logger.error(f"✗ Error applying {filename}: {e}")
                # Provide guidance on already applied or enum duplicate cases
                if "already exists" in str(e).lower() or "duplicate" in str(e).lower():
                    logger.warning("Object already exists; continuing...")
                else:
                    raise e

    logger.info("==================================================")
    logger.info("All production migrations executed successfully.")
    logger.info("==================================================")


if __name__ == "__main__":
    db_url = sys.argv[1] if len(sys.argv) > 1 else get_production_database_url()
    run_migrations(db_url)
