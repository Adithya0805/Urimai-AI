-- ==============================================================================
-- Urimai AI — Phase 2: Scheme Knowledge Base Schema
-- Target: Supabase / PostgreSQL
-- ==============================================================================

-- 1. Create Enums for Rules
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

-- 2. Create SCHEMES Table
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
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 3. Create ELIGIBILITY_RULES Table
CREATE TABLE IF NOT EXISTS eligibility_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scheme_id UUID NOT NULL REFERENCES schemes(id) ON DELETE CASCADE,
    field_name VARCHAR(100) NOT NULL,
    operator VARCHAR(50) NOT NULL,
    value VARCHAR(255) NOT NULL,
    applies_to VARCHAR(50) NOT NULL
);

-- 4. Create SCHEME_TERM_GLOSSARY Table
CREATE TABLE IF NOT EXISTS scheme_term_glossary (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tamil_term VARCHAR(255) NOT NULL,
    english_equivalent VARCHAR(255) NOT NULL,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 5. Indexes
CREATE INDEX IF NOT EXISTS idx_schemes_dept_cat ON schemes(department, category);
CREATE INDEX IF NOT EXISTS idx_schemes_code ON schemes(scheme_code);
CREATE INDEX IF NOT EXISTS idx_eligibility_rules_scheme_id ON eligibility_rules(scheme_id);
CREATE INDEX IF NOT EXISTS idx_glossary_tamil_term ON scheme_term_glossary(tamil_term);

-- 6. Trigger for updated_at on schemes
DROP TRIGGER IF EXISTS trg_update_schemes_timestamp ON schemes;
CREATE TRIGGER trg_update_schemes_timestamp
    BEFORE UPDATE ON schemes
    FOR EACH ROW
    EXECUTE FUNCTION update_timestamp_column();
