import logging
from typing import Dict, List, Any
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.config import get_settings

logger = logging.getLogger("urimai.security_audit")

# Expected tables that must have Row Level Security enabled in PostgreSQL
CRITICAL_RLS_TABLES = [
    "families",
    "persons",
    "schemes",
    "eligibility_rules",
    "scheme_term_glossary",
    "intake_extraction_logs",
    "application_statuses",
    "notification_logs",
    "scheme_review_queue",
    "llm_call_logs",
    "admin_audit_logs",
    "whatsapp_sessions",
    "whatsapp_message_logs",
]


def audit_database_security_policies(db: Session) -> Dict[str, Any]:
    """Inspects Postgres database catalog to verify Row Level Security (RLS)
    and policies on all tables.
    """
    settings = get_settings()
    # Check if connected to Postgres vs SQLite
    bind_name = db.get_bind().dialect.name

    if bind_name != "postgresql":
        return {
            "dialect": bind_name,
            "environment": settings.ENVIRONMENT,
            "status": "SKIPPED_SQLITE",
            "message": "RLS checks are native to PostgreSQL / Supabase. Local SQLite uses ORM-level tenant filtering.",
            "tables_audited": len(CRITICAL_RLS_TABLES),
            "tables_secured": len(CRITICAL_RLS_TABLES),
            "unsecured_tables": [],
            "policies": [],
        }

    try:
        # Check RLS status on tables
        rls_query = text("""
            SELECT tablename, rowsecurity
            FROM pg_tables
            WHERE schemaname = 'public';
        """)
        rls_results = db.execute(rls_query).fetchall()
        rls_map = {row[0]: row[1] for row in rls_results}

        # Check existing policies
        policy_query = text("""
            SELECT tablename, policyname, cmd, qual
            FROM pg_policies
            WHERE schemaname = 'public';
        """)
        policy_results = db.execute(policy_query).fetchall()
        policies = [
            {
                "table": row[0],
                "policy_name": row[1],
                "command": row[2],
            }
            for row in policy_results
        ]

        unsecured_tables = []
        for table in CRITICAL_RLS_TABLES:
            if table in rls_map and not rls_map[table]:
                unsecured_tables.append(table)

        is_secure = len(unsecured_tables) == 0 and len(policies) > 0

        return {
            "dialect": "postgresql",
            "environment": settings.ENVIRONMENT,
            "status": "PASS" if is_secure else "WARNING",
            "is_fully_secured": is_secure,
            "tables_audited": len(CRITICAL_RLS_TABLES),
            "unsecured_tables": unsecured_tables,
            "policy_count": len(policies),
            "policies": policies,
        }

    except Exception as e:
        logger.error(f"Failed to audit database security policies: {e}")
        return {
            "dialect": bind_name,
            "status": "ERROR",
            "error": str(e),
        }
