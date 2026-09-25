# Urimai AI (உரிமை AI) — Production Infrastructure & Deployment Guide

This document details the complete production infrastructure deployment, database migrations, security verification, cloud hosting setup (Railway & Vercel), backup/restore testing, and continuous uptime monitoring for Urimai AI.

---

## 1. Migration Numbering & Sequence Resolution

All migration numbering collisions (005/006 duplicates) have been resolved into a strictly sequential, dependency-ordered chain:

| Sequence | Migration File | Target Tables / Schema Changes |
|---|---|---|
| **001** | [`migrations/001_initial_schema.sql`](file:///d:/Urimai%20AI/backend/migrations/001_initial_schema.sql) | Enums, `families`, `persons`, timestamp triggers |
| **002** | [`migrations/002_schemes_schema.sql`](file:///d:/Urimai%20AI/backend/migrations/002_schemes_schema.sql) | `schemes`, `eligibility_rules`, `scheme_term_glossary` |
| **003** | [`migrations/003_intake_log_schema.sql`](file:///d:/Urimai%20AI/backend/migrations/003_intake_log_schema.sql) | `intake_extraction_logs` |
| **004** | [`migrations/004_scheme_guidance_fields.sql`](file:///d:/Urimai%20AI/backend/migrations/004_scheme_guidance_fields.sql) | Guidance fields: `application_office`, `application_mode`, `required_documents`, `processing_time_estimate` |
| **005** | [`migrations/005_add_agriculture_fields.sql`](file:///d:/Urimai%20AI/backend/migrations/005_add_agriculture_fields.sql) | Agriculture extensions: `land_holding_acres`, `crop_type` |
| **006** | [`migrations/006_application_tracking_and_freshness.sql`](file:///d:/Urimai%20AI/backend/migrations/006_application_tracking_and_freshness.sql) | `application_statuses`, `notification_logs`, `scheme_review_queue` |
| **007** | [`migrations/007_add_llm_call_logs.sql`](file:///d:/Urimai%20AI/backend/migrations/007_add_llm_call_logs.sql) | `llm_call_logs` telemetry and latency audit table |
| **008** | [`migrations/008_auth_and_rls.sql`](file:///d:/Urimai%20AI/backend/migrations/008_auth_and_rls.sql) | `user_id`/`created_by` foreign keys, table-level RLS enablement, citizen & volunteer isolation policies |
| **009** | [`migrations/009_admin_dashboard_and_audit.sql`](file:///d:/Urimai%20AI/backend/migrations/009_admin_dashboard_and_audit.sql) | `admin_audit_logs`, Admin role RLS policies with cross-family review and write access |

---

## 2. Production Database Setup & Security Verification

### Step 2.1: Run Migrations against Production Supabase
```bash
python backend/scripts/migrate_production.py postgresql://postgres:[PROD_PASSWORD]@db.[PROD_PROJECT_REF].supabase.co:5432/postgres
```

### Step 2.2: Audit Row Level Security BEFORE Seeding Data
```bash
python backend/scripts/verify_production_security.py postgresql://postgres:[PROD_PASSWORD]@db.[PROD_PROJECT_REF].supabase.co:5432/postgres
```
*Guarantees that all 11 tables have RLS enabled and active tenant isolation policies before any live records are populated.*

### Step 2.3: Seed Scheme Knowledge Base Across All 4 Departments
```bash
python backend/scripts/seed_production.py postgresql://postgres:[PROD_PASSWORD]@db.[PROD_PROJECT_REF].supabase.co:5432/postgres
```
*Populates verified schemes for Social Welfare, Higher & School Education, Agriculture & Farmer Welfare, and Labour & Employment.*

---

## 3. Backend Deployment (Railway / Render)

### Environment Variables for Railway/Render Dashboard:
```ini
ENVIRONMENT=production
DATABASE_URL=postgresql://postgres:[PROD_PASSWORD]@db.[PROD_PROJECT_REF].supabase.co:5432/postgres
SUPABASE_URL=https://[PROD_PROJECT_REF].supabase.co
SUPABASE_KEY=[PROD_SUPABASE_SERVICE_ROLE_KEY]
GOOGLE_API_KEY=[PROD_GEMINI_API_KEY]
PINECONE_API_KEY=[PROD_PINECONE_API_KEY]
PINECONE_INDEX_NAME=urimai-schemes
JWT_SECRET=[CRYPTO_RANDOM_256_BIT_SECRET]
ALLOWED_ORIGINS=https://urimai-ai.vercel.app,https://admin.urimai.tn.gov.in
RATE_LIMIT_ENABLED=true
```

### Deploy via Railway CLI:
```bash
railway login
railway init --name urimai-backend
railway up
```

---

## 4. Frontend Deployment (Vercel)

### Environment Variables for Vercel Project Dashboard:
```ini
NEXT_PUBLIC_API_URL=https://urimai-backend.up.railway.app
NEXT_PUBLIC_SUPABASE_URL=https://[PROD_PROJECT_REF].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=[PROD_SUPABASE_ANON_KEY]
```

### Deploy via Vercel CLI:
```bash
vercel login
cd frontend
vercel --prod
```

---

## 5. End-to-End Throttled Network Testing

To verify resilience on patchy 2G/3G mobile networks across Tamil Nadu:
```bash
# Run throttled network journey against live deployment
TEST_BASE_URL=https://urimai-backend.up.railway.app pytest backend/tests/test_live_e2e_throttled.py -v
```

---

## 6. Backup & Disaster Recovery Verification

1. **Automated Snapshots**: Daily Supabase backups retained for 7 to 30 days.
2. **Point-In-Time Recovery (PITR)**: Continuous transaction log archiving.
3. **Test Restore Procedure**:
   ```bash
   # Export test backup
   pg_dump --dbname="postgresql://postgres:[PROD_PW]@db.[PROD_REF].supabase.co:5432/postgres" \
           --format=custom --file="urimai_backup_test.dump"

   # Restore into throwaway test project
   pg_restore --dbname="postgresql://postgres:[TEST_PW]@db.[THROWAWAY_REF].supabase.co:5432/postgres" \
              --clean --if-exists urimai_backup_test.dump

   # Verify security on restored database
   python backend/scripts/verify_production_security.py postgresql://postgres:[TEST_PW]@db.[THROWAWAY_REF].supabase.co:5432/postgres
   ```

---

## 7. Continuous Uptime & Latency Monitoring

Run the background uptime healthcheck monitor:
```bash
python backend/scripts/uptime_monitor.py --target-url https://urimai-backend.up.railway.app --interval 30
```
- **Healthcheck endpoint**: `/health` (verifies API and PostgreSQL connection health)
- **Degradation alert**: Flags when latency exceeds 2,500ms or HTTP status $\neq$ 200.
