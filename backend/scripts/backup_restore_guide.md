# Urimai AI — Production Supabase Backup & Disaster Recovery Guide

This guide establishes backup policies, automated retention schedules, and disaster recovery procedures for the production Supabase PostgreSQL instance.

---

## 1. Backup Strategy Overview

| Tier | Mechanism | Schedule | Retention | Recovery Objective (RTO/RPO) |
|---|---|---|---|---|
| **Tier 1: Daily Automated Backups** | Supabase Managed Snapshots | Daily at 00:00 UTC | 7 to 30 days (Pro plan) | RTO < 15 mins, RPO < 24 hrs |
| **Tier 2: Point-In-Time Recovery (PITR)** | WAL Streaming (Supabase PITR) | Continuous (every second) | Up to 7 days | RTO < 10 mins, RPO < 1 min |
| **Tier 3: Offline Logical Dumps** | `pg_dump` Encrypted Backups | Weekly automated script | 90 days off-site (S3 / GCS) | Cold Disaster Recovery |

---

## 2. Enabling Automatic Backups in Supabase

1. Open the [Supabase Dashboard](https://supabase.com/dashboard/project/_/database/backups/scheduled).
2. Navigate to **Project Settings** $\rightarrow$ **Database** $\rightarrow$ **Backups**.
3. Confirm that **Scheduled Backups** is enabled.
4. For high-availability production workloads, enable **Point in Time Recovery (PITR)** under the Add-ons tab to enable continuous transaction log archiving.

---

## 3. Manual Backup Procedure (`pg_dump`)

To take an immediate point-in-time snapshot before running major schema changes or data migrations:

```bash
# 1. Export database snapshot (Schema + Data)
pg_dump \
  --dbname="postgresql://postgres:[PROD_PASSWORD]@db.[PROD_PROJECT_REF].supabase.co:5432/postgres" \
  --format=custom \
  --no-owner \
  --no-privileges \
  --file="urimai_prod_backup_$(date +%Y%m%d_%H%M%S).dump"

# 2. Verify dump integrity
pg_restore --list urimai_prod_backup_*.dump > /dev/null && echo "✓ Backup verified successfully."
```

---

## 4. Disaster Recovery & Restore Procedure

In the event of accidental data corruption or disaster recovery:

### Method A: One-Click Restore via Supabase Dashboard
1. Go to **Database** $\rightarrow$ **Backups** $\rightarrow$ **Scheduled Backups** (or **Point in Time**).
2. Select the target snapshot or exact timestamp.
3. Click **Restore to New Project** (Recommended to prevent overwrite) or **Restore to Current Project**.

### Method B: Command-Line Restore (`pg_restore`)
To restore from a logical dump file into a clean target database:

```bash
# 1. Run migrations first to establish extensions and enums
python scripts/migrate_production.py postgresql://postgres:[PASSWORD]@db.[TARGET_REF].supabase.co:5432/postgres

# 2. Restore tables and verified data
pg_restore \
  --dbname="postgresql://postgres:[PASSWORD]@db.[TARGET_REF].supabase.co:5432/postgres" \
  --clean \
  --if-exists \
  --no-owner \
  --no-privileges \
  --data-only \
  urimai_prod_backup_20260924.dump

# 3. Verify Row-Level Security and data integrity
python scripts/verify_production_security.py postgresql://postgres:[PASSWORD]@db.[TARGET_REF].supabase.co:5432/postgres
```

---

## 5. Verification Checklist Post-Restore

After restoring a database instance, run the following commands to confirm full operational readiness:

1. `python scripts/verify_production_security.py` — Confirm RLS policies are active on all 8 tables.
2. `pytest tests/test_end_to_end_system_integration.py -v` — Run full citizen journey.
3. `curl http://127.0.0.1:8000/health` — Verify DB connection status returns `healthy`.
