"""Unit tests for SQL migration sequence ordering, integrity, and dependencies.
"""
import glob
from pathlib import Path

MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"


def test_migration_files_numbering_and_no_duplicates():
    migration_files = sorted(glob.glob(str(MIGRATIONS_DIR / "[0-9][0-9][0-9]_*.sql")))
    assert len(migration_files) == 10, f"Expected exactly 10 migration files, found {len(migration_files)}"

    basenames = [Path(p).name for p in migration_files]
    prefixes = [b.split("_")[0] for b in basenames]

    # Verify strictly 001 to 010
    expected_prefixes = [f"{i:03d}" for i in range(1, 11)]
    assert prefixes == expected_prefixes, f"Migration prefixes {prefixes} do not match {expected_prefixes}"

    expected_files = [
        "001_initial_schema.sql",
        "002_schemes_schema.sql",
        "003_intake_log_schema.sql",
        "004_scheme_guidance_fields.sql",
        "005_add_agriculture_fields.sql",
        "006_application_tracking_and_freshness.sql",
        "007_add_llm_call_logs.sql",
        "008_auth_and_rls.sql",
        "009_admin_dashboard_and_audit.sql",
        "010_whatsapp_channel.sql",
    ]
    assert basenames == expected_files


def test_migration_dependency_ordering():
    """Verify that tables are created before they are referenced or altered."""
    migration_files = sorted(glob.glob(str(MIGRATIONS_DIR / "[0-9][0-9][0-9]_*.sql")))
    sql_texts = {}
    for p in migration_files:
        with open(p, "r", encoding="utf-8") as f:
            sql_texts[Path(p).name] = f.read().lower()

    # 1. families & persons created in 001
    assert "create table if not exists families" in sql_texts["001_initial_schema.sql"]
    assert "create table if not exists persons" in sql_texts["001_initial_schema.sql"]

    # 2. schemes & rules created in 002
    assert "create table if not exists schemes" in sql_texts["002_schemes_schema.sql"]
    assert "create table if not exists eligibility_rules" in sql_texts["002_schemes_schema.sql"]

    # 3. intake logs in 003
    assert "create table if not exists intake_extraction_logs" in sql_texts["003_intake_log_schema.sql"]

    # 4. scheme guidance fields in 004 alters schemes
    assert "alter table schemes" in sql_texts["004_scheme_guidance_fields.sql"]

    # 5. agriculture fields in 005 alters persons
    assert "alter table persons" in sql_texts["005_add_agriculture_fields.sql"]

    # 6. application tracking & freshness in 006
    assert "create table if not exists application_statuses" in sql_texts["006_application_tracking_and_freshness.sql"]
    assert "create table if not exists notification_logs" in sql_texts["006_application_tracking_and_freshness.sql"]
    assert "create table if not exists scheme_review_queue" in sql_texts["006_application_tracking_and_freshness.sql"]

    # 7. llm call logs in 007
    assert "create table if not exists llm_call_logs" in sql_texts["007_add_llm_call_logs.sql"]

    # 8. auth and rls in 008
    assert "alter table families enable row level security" in sql_texts["008_auth_and_rls.sql"]
    assert "alter table persons enable row level security" in sql_texts["008_auth_and_rls.sql"]

    # 9. admin dashboard and audit in 009
    assert "create table if not exists admin_audit_logs" in sql_texts["009_admin_dashboard_and_audit.sql"]
    assert "alter table admin_audit_logs enable row level security" in sql_texts["009_admin_dashboard_and_audit.sql"]

    # 10. whatsapp channel in 010
    assert "create table if not exists whatsapp_sessions" in sql_texts["010_whatsapp_channel.sql"]
    assert "create table if not exists whatsapp_message_logs" in sql_texts["010_whatsapp_channel.sql"]
    assert "alter table whatsapp_sessions enable row level security" in sql_texts["010_whatsapp_channel.sql"]
