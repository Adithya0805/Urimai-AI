-- ==============================================================================
-- Urimai AI — Phase 7: Application Tracking & Freshness Review Schema
-- Target: Supabase / PostgreSQL
-- ==============================================================================

-- 1. Create Application Tracking Status Enum
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

-- 2. Create APPLICATION_STATUSES Table
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

-- 3. Create NOTIFICATION_LOGS Table
CREATE TABLE IF NOT EXISTS notification_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    application_id UUID REFERENCES application_statuses(id) ON DELETE CASCADE,
    person_id UUID NOT NULL REFERENCES persons(id) ON DELETE CASCADE,
    notification_type VARCHAR(100) NOT NULL,
    channel VARCHAR(50) NOT NULL DEFAULT 'log',
    message_tamil TEXT NOT NULL,
    sent_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 4. Create SCHEME_REVIEW_QUEUE Table
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

-- 5. Indexes for fast lookup
CREATE INDEX IF NOT EXISTS idx_application_statuses_person_id ON application_statuses(person_id);
CREATE INDEX IF NOT EXISTS idx_application_statuses_scheme_id ON application_statuses(scheme_id);
CREATE INDEX IF NOT EXISTS idx_application_statuses_status ON application_statuses(status);
CREATE INDEX IF NOT EXISTS idx_notification_logs_person_id ON notification_logs(person_id);
CREATE INDEX IF NOT EXISTS idx_scheme_review_queue_status ON scheme_review_queue(status);
