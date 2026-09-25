-- ==============================================================================
-- Urimai AI — Phase 5: Scheme Guidance Fields Schema
-- Target: Supabase / PostgreSQL
-- ==============================================================================

DO $$ BEGIN
    CREATE TYPE application_mode_enum AS ENUM ('online', 'offline', 'both');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

ALTER TABLE schemes
    ADD COLUMN IF NOT EXISTS required_documents JSONB NOT NULL DEFAULT '[]'::jsonb,
    ADD COLUMN IF NOT EXISTS application_office VARCHAR(255) NOT NULL DEFAULT 'வட்டாட்சியர் அலுவலகம் / இ-சேவை மையம்',
    ADD COLUMN IF NOT EXISTS application_mode VARCHAR(50) NOT NULL DEFAULT 'both',
    ADD COLUMN IF NOT EXISTS online_application_url VARCHAR(500),
    ADD COLUMN IF NOT EXISTS processing_time_estimate VARCHAR(100) NOT NULL DEFAULT '15 முதல் 30 நாட்கள்';
