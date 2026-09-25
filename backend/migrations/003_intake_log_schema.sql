-- ==============================================================================
-- Urimai AI — Phase 4: Intake Extraction Logs Schema
-- Target: Supabase / PostgreSQL
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
