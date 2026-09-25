-- ==============================================================================
-- Urimai AI — Complete Production Schema Migration (001 - 010 Consolidated)
-- Target: Supabase / PostgreSQL
-- Project: vabchcklkasdxjjdxomw (or any Supabase instance)
-- ==============================================================================

-- 0. Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ==============================================================================
-- Migration 001: Foundational Schema (Families & Persons)
-- ==============================================================================

DO $$ BEGIN
    CREATE TYPE composition_type_enum AS ENUM ('single', 'couple', 'nuclear', 'joint');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE ration_card_type_enum AS ENUM ('none', 'green', 'white', 'khaki', 'phh_aay', 'orange', 'yellow', 'other');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE gender_enum AS ENUM ('male', 'female', 'transgender', 'other');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE education_level_enum AS ENUM ('none', 'primary', 'secondary', 'higher_secondary', 'graduate', 'postgraduate', 'dropout');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE occupation_enum AS ENUM ('farmer', 'daily_wage', 'self_employed', 'govt_employee', 'private_employee', 'unemployed', 'student', 'homemaker', 'retired', 'other');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE marital_status_enum AS ENUM ('single', 'married', 'widowed', 'divorced');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE caste_category_enum AS ENUM ('SC', 'ST', 'BC', 'MBC', 'DNC', 'General');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS families (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    composition_type VARCHAR(50) NOT NULL,
    district TEXT NOT NULL,
    taluk TEXT NOT NULL,
    address TEXT NOT NULL,
    ration_card_type VARCHAR(50) NOT NULL,
    total_household_income NUMERIC(12, 2) NOT NULL CHECK (total_household_income >= 0),
    user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS persons (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL REFERENCES families(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL,
    education_level VARCHAR(50) NOT NULL,
    occupation VARCHAR(50) NOT NULL,
    occupation_detail TEXT,
    marital_status VARCHAR(50) NOT NULL,
    caste_category VARCHAR(50) NOT NULL,
    disability_status BOOLEAN NOT NULL DEFAULT FALSE,
    disability_type TEXT,
    special_flags JSONB NOT NULL DEFAULT '[]'::jsonb,
    land_holding_acres NUMERIC(6, 2) DEFAULT 0.0,
    crop_type VARCHAR(100) DEFAULT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_persons_family_id ON persons(family_id);
CREATE INDEX IF NOT EXISTS idx_families_district_taluk ON families(district, taluk);
CREATE INDEX IF NOT EXISTS idx_families_user_id ON families(user_id);
CREATE INDEX IF NOT EXISTS idx_families_created_by ON families(created_by);

CREATE OR REPLACE FUNCTION update_timestamp_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_update_families_timestamp ON families;
CREATE TRIGGER trg_update_families_timestamp
    BEFORE UPDATE ON families
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp_column();

DROP TRIGGER IF EXISTS trg_update_persons_timestamp ON persons;
CREATE TRIGGER trg_update_persons_timestamp
    BEFORE UPDATE ON persons
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp_column();

-- ==============================================================================
-- Migration 002 & 004: Schemes, Eligibility Rules, Glossary & Guidance Fields
-- ==============================================================================

DO $$ BEGIN
    CREATE TYPE rule_operator_enum AS ENUM (
        'equals', 'not_equals', 'greater_than', 'less_than', 
        'greater_or_equal', 'less_or_equal', 'in_list'
    );
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE rule_applies_to_enum AS ENUM ('person', 'family');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE application_mode_enum AS ENUM ('online', 'offline', 'both');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS schemes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scheme_code VARCHAR(100) UNIQUE NOT NULL,
    name_english VARCHAR(255) NOT NULL,
    name_tamil VARCHAR(255) NOT NULL,
    name_transliteration VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    description_english TEXT NOT NULL,
    description_tamil TEXT NOT NULL,
    benefit_amount VARCHAR(255) NOT NULL,
    source_url VARCHAR(500) NOT NULL,
    last_verified_date DATE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    required_documents JSONB NOT NULL DEFAULT '[]'::jsonb,
    application_office VARCHAR(255) NOT NULL DEFAULT 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்',
    application_mode VARCHAR(50) NOT NULL DEFAULT 'both',
    online_application_url VARCHAR(500),
    processing_time_estimate VARCHAR(100) NOT NULL DEFAULT '15 முதல் 30 நாட்கள்',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS eligibility_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scheme_id UUID NOT NULL REFERENCES schemes(id) ON DELETE CASCADE,
    field_name VARCHAR(100) NOT NULL,
    operator VARCHAR(50) NOT NULL,
    value VARCHAR(255) NOT NULL,
    applies_to VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS scheme_term_glossary (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tamil_term VARCHAR(255) NOT NULL,
    english_equivalent VARCHAR(255) NOT NULL,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_schemes_dept_cat ON schemes(department, category);
CREATE INDEX IF NOT EXISTS idx_schemes_code ON schemes(scheme_code);
CREATE INDEX IF NOT EXISTS idx_eligibility_rules_scheme_id ON eligibility_rules(scheme_id);
CREATE INDEX IF NOT EXISTS idx_glossary_tamil_term ON scheme_term_glossary(tamil_term);

DROP TRIGGER IF EXISTS trg_update_schemes_timestamp ON schemes;
CREATE TRIGGER trg_update_schemes_timestamp
    BEFORE UPDATE ON schemes
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp_column();

-- ==============================================================================
-- Migration 003: Intake Extraction Logs
-- ==============================================================================

CREATE TABLE IF NOT EXISTS intake_extraction_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id VARCHAR(100) NOT NULL,
    raw_tamil_input TEXT NOT NULL,
    target_field VARCHAR(100) NOT NULL,
    extracted_value TEXT NOT NULL,
    confirmed_value TEXT,
    is_valid BOOLEAN NOT NULL DEFAULT TRUE,
    error_message TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_intake_logs_session_id ON intake_extraction_logs(session_id);
CREATE INDEX IF NOT EXISTS idx_intake_logs_field ON intake_extraction_logs(target_field);

-- ==============================================================================
-- Migration 006: Application Tracking & Freshness Review Queue
-- ==============================================================================

DO $$ BEGIN
    CREATE TYPE application_tracking_status_enum AS ENUM (
        'not_started',
        'documents_pending',
        'submitted',
        'under_review',
        'approved',
        'rejected',
        'renewal_due'
    );
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS application_statuses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    person_id UUID NOT NULL REFERENCES persons(id) ON DELETE CASCADE,
    scheme_id UUID NOT NULL REFERENCES schemes(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL DEFAULT 'not_started',
    last_updated DATE NOT NULL DEFAULT CURRENT_DATE,
    next_action_note TEXT,
    pending_documents JSONB NOT NULL DEFAULT '[]'::jsonb,
    renewal_due_date DATE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS notification_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID REFERENCES application_statuses(id) ON DELETE CASCADE,
    person_id UUID NOT NULL REFERENCES persons(id) ON DELETE CASCADE,
    notification_type VARCHAR(100) NOT NULL,
    channel VARCHAR(50) NOT NULL DEFAULT 'log',
    message_tamil TEXT NOT NULL,
    sent_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS scheme_review_queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scheme_id UUID NOT NULL REFERENCES schemes(id) ON DELETE CASCADE,
    flagged_reason TEXT NOT NULL,
    source_url VARCHAR(500) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending_human_review',
    reviewer_notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    reviewed_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_application_statuses_person_id ON application_statuses(person_id);
CREATE INDEX IF NOT EXISTS idx_application_statuses_scheme_id ON application_statuses(scheme_id);
CREATE INDEX IF NOT EXISTS idx_application_statuses_status ON application_statuses(status);
CREATE INDEX IF NOT EXISTS idx_notification_logs_person_id ON notification_logs(person_id);
CREATE INDEX IF NOT EXISTS idx_scheme_review_queue_status ON scheme_review_queue(status);

-- ==============================================================================
-- Migration 007: LLM Call Logs Audit Trail
-- ==============================================================================

CREATE TABLE IF NOT EXISTS llm_call_logs (
    id          CHAR(36) PRIMARY KEY,
    call_type   VARCHAR(50)  NOT NULL,
    session_id  VARCHAR(100) NULL,
    person_id   VARCHAR(36)  NULL,
    scheme_code VARCHAR(100) NULL,
    prompt_text TEXT         NOT NULL,
    retrieved_context TEXT   NULL,
    retrieval_score   FLOAT  NULL,
    used_rag    BOOLEAN      NOT NULL DEFAULT FALSE,
    llm_output  TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_llm_call_logs_call_type   ON llm_call_logs(call_type);
CREATE INDEX IF NOT EXISTS ix_llm_call_logs_session_id  ON llm_call_logs(session_id);
CREATE INDEX IF NOT EXISTS ix_llm_call_logs_person_id   ON llm_call_logs(person_id);
CREATE INDEX IF NOT EXISTS ix_llm_call_logs_scheme_code ON llm_call_logs(scheme_code);

-- ==============================================================================
-- Migration 009: Admin Audit Logs
-- ==============================================================================

CREATE TABLE IF NOT EXISTS admin_audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    admin_user_id UUID NOT NULL,
    admin_email VARCHAR(255) NOT NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(100) NOT NULL,
    entity_id VARCHAR(100) NOT NULL,
    before_value JSONB,
    after_value JSONB,
    ip_address VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_admin_audit_logs_action ON admin_audit_logs(action);
CREATE INDEX IF NOT EXISTS idx_admin_audit_logs_entity ON admin_audit_logs(entity_type, entity_id);
CREATE INDEX IF NOT EXISTS idx_admin_audit_logs_created_at ON admin_audit_logs(created_at DESC);

-- ==============================================================================
-- Migration 010: WhatsApp Channel Sessions & Message Logs
-- ==============================================================================

CREATE TABLE IF NOT EXISTS whatsapp_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(50) NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    family_id UUID REFERENCES families(id) ON DELETE SET NULL,
    current_step VARCHAR(50) NOT NULL DEFAULT 'greet',
    state_data JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(50) NOT NULL DEFAULT 'active',
    whatsapp_consent BOOLEAN NOT NULL DEFAULT FALSE,
    consent_at TIMESTAMPTZ,
    last_user_message_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS whatsapp_message_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(50) NOT NULL,
    direction VARCHAR(20) NOT NULL,
    message_type VARCHAR(50) NOT NULL DEFAULT 'session',
    template_name VARCHAR(100),
    body TEXT NOT NULL,
    is_within_24h BOOLEAN NOT NULL DEFAULT TRUE,
    status VARCHAR(50) NOT NULL DEFAULT 'sent',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_phone ON whatsapp_sessions(phone_number);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_user_id ON whatsapp_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_status ON whatsapp_sessions(status);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_last_msg ON whatsapp_sessions(last_user_message_at);
CREATE INDEX IF NOT EXISTS idx_whatsapp_logs_phone ON whatsapp_message_logs(phone_number);
CREATE INDEX IF NOT EXISTS idx_whatsapp_logs_created_at ON whatsapp_message_logs(created_at DESC);

-- ==============================================================================
-- Migration 008 & 009: Row-Level Security (RLS) & Policies
-- ==============================================================================

-- Enable RLS across all tables
ALTER TABLE families ENABLE ROW LEVEL SECURITY;
ALTER TABLE persons ENABLE ROW LEVEL SECURITY;
ALTER TABLE application_statuses ENABLE ROW LEVEL SECURITY;
ALTER TABLE notification_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE intake_extraction_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE schemes ENABLE ROW LEVEL SECURITY;
ALTER TABLE eligibility_rules ENABLE ROW LEVEL SECURITY;
ALTER TABLE scheme_term_glossary ENABLE ROW LEVEL SECURITY;
ALTER TABLE admin_audit_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE scheme_review_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE llm_call_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE whatsapp_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE whatsapp_message_logs ENABLE ROW LEVEL SECURITY;

-- 1. Schemes & Glossary (Public Read)
DROP POLICY IF EXISTS schemes_public_read ON schemes;
CREATE POLICY schemes_public_read ON schemes FOR SELECT USING (is_active = true);

DROP POLICY IF EXISTS rules_public_read ON eligibility_rules;
CREATE POLICY rules_public_read ON eligibility_rules FOR SELECT USING (true);

DROP POLICY IF EXISTS glossary_public_read ON scheme_term_glossary;
CREATE POLICY glossary_public_read ON scheme_term_glossary FOR SELECT USING (true);

-- 2. Families (Owner, Volunteer, Admin)
DROP POLICY IF EXISTS families_user_isolation_select ON families;
CREATE POLICY families_user_isolation_select ON families
    FOR SELECT
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS families_user_isolation_insert ON families;
CREATE POLICY families_user_isolation_insert ON families
    FOR INSERT
    WITH CHECK (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS families_user_isolation_update ON families;
CREATE POLICY families_user_isolation_update ON families
    FOR UPDATE
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS families_user_isolation_delete ON families;
CREATE POLICY families_user_isolation_delete ON families
    FOR DELETE
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 3. Persons (Inherited Family Isolation)
DROP POLICY IF EXISTS persons_family_isolation_select ON persons;
CREATE POLICY persons_family_isolation_select ON persons
    FOR SELECT
    USING (
        EXISTS (
            SELECT 1 FROM families 
            WHERE families.id = persons.family_id 
            AND (
                families.user_id = auth.uid() 
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'volunteer'
                OR (auth.jwt() ->> 'role') = 'admin'
                OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
            )
        )
    );

DROP POLICY IF EXISTS persons_family_isolation_insert ON persons;
CREATE POLICY persons_family_isolation_insert ON persons
    FOR INSERT
    WITH CHECK (
        EXISTS (
            SELECT 1 FROM families 
            WHERE families.id = persons.family_id 
            AND (
                families.user_id = auth.uid() 
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'volunteer'
                OR (auth.jwt() ->> 'role') = 'admin'
                OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
            )
        )
    );

DROP POLICY IF EXISTS persons_family_isolation_update ON persons;
CREATE POLICY persons_family_isolation_update ON persons
    FOR UPDATE
    USING (
        EXISTS (
            SELECT 1 FROM families 
            WHERE families.id = persons.family_id 
            AND (
                families.user_id = auth.uid() 
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'volunteer'
                OR (auth.jwt() ->> 'role') = 'admin'
                OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
            )
        )
    );

DROP POLICY IF EXISTS persons_family_isolation_delete ON persons;
CREATE POLICY persons_family_isolation_delete ON persons
    FOR DELETE
    USING (
        EXISTS (
            SELECT 1 FROM families 
            WHERE families.id = persons.family_id 
            AND (
                families.user_id = auth.uid() 
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'admin'
                OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
            )
        )
    );

-- 4. Application Status & Notification Logs
DROP POLICY IF EXISTS application_statuses_isolation ON application_statuses;
CREATE POLICY application_statuses_isolation ON application_statuses
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR EXISTS (
            SELECT 1 FROM persons
            JOIN families ON families.id = persons.family_id
            WHERE persons.id = application_statuses.person_id
            AND (
                families.user_id = auth.uid()
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'volunteer'
            )
        )
    );

DROP POLICY IF EXISTS notification_logs_isolation ON notification_logs;
CREATE POLICY notification_logs_isolation ON notification_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR EXISTS (
            SELECT 1 FROM persons
            JOIN families ON families.id = persons.family_id
            WHERE persons.id = notification_logs.person_id
            AND (
                families.user_id = auth.uid()
                OR families.created_by = auth.uid()
                OR (auth.jwt() ->> 'role') = 'service_role'
                OR (auth.jwt() ->> 'role') = 'volunteer'
            )
        )
    );

-- 5. Admin & Service Role Policies for Audit, Review Queue & LLM Logs
DROP POLICY IF EXISTS "Admins can view and create audit logs" ON admin_audit_logs;
CREATE POLICY "Admins can view and create audit logs"
    ON admin_audit_logs FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS "Admins have full access to scheme review queue" ON scheme_review_queue;
CREATE POLICY "Admins have full access to scheme review queue"
    ON scheme_review_queue FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS "Admins have write access to schemes" ON schemes;
CREATE POLICY "Admins have write access to schemes"
    ON schemes FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS "Admins have write access to eligibility rules" ON eligibility_rules;
CREATE POLICY "Admins have write access to eligibility rules"
    ON eligibility_rules FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS "Admins have write access to glossary" ON scheme_term_glossary;
CREATE POLICY "Admins have write access to glossary"
    ON scheme_term_glossary FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS "LLM logs access for admin and service role" ON llm_call_logs;
CREATE POLICY "LLM logs access for admin and service role"
    ON llm_call_logs FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

DROP POLICY IF EXISTS intake_logs_access ON intake_extraction_logs;
CREATE POLICY intake_logs_access ON intake_extraction_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'authenticated'
        OR (auth.jwt() ->> 'role') = 'anon'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 6. WhatsApp Sessions & Message Logs
DROP POLICY IF EXISTS "Service role has full access to whatsapp_sessions" ON whatsapp_sessions;
CREATE POLICY "Service role has full access to whatsapp_sessions"
    ON whatsapp_sessions FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Service role has full access to whatsapp_message_logs" ON whatsapp_message_logs;
CREATE POLICY "Service role has full access to whatsapp_message_logs"
    ON whatsapp_message_logs FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );
