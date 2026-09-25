-- ==============================================================================
-- Urimai AI — Phase 1: Foundational Data Layer Schema
-- Target: Supabase / PostgreSQL
-- ==============================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Clean up if exists (for clean re-runs)
-- DROP TABLE IF EXISTS persons CASCADE;
-- DROP TABLE IF EXISTS families CASCADE;

-- 1. Create Enums
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

-- 2. Create FAMILIES Table
CREATE TABLE IF NOT EXISTS families (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    composition_type VARCHAR(50) NOT NULL,
    district TEXT NOT NULL,
    taluk TEXT NOT NULL,
    address TEXT NOT NULL,
    ration_card_type VARCHAR(50) NOT NULL,
    total_household_income NUMERIC(12, 2) NOT NULL CHECK (total_household_income >= 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 3. Create PERSONS Table
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
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 4. Create Indexes
CREATE INDEX IF NOT EXISTS idx_persons_family_id ON persons(family_id);
CREATE INDEX IF NOT EXISTS idx_families_district_taluk ON families(district, taluk);

-- 5. Trigger for updated_at timestamps
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
