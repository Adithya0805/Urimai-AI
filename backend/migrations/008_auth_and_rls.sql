-- ==============================================================================
-- Urimai AI — Phase 8: Supabase Authentication, Session & Row-Level Security (RLS)
-- Target: Supabase / PostgreSQL
-- ==============================================================================

-- 1. Add user_id and created_by to families
ALTER TABLE families 
ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
ADD COLUMN IF NOT EXISTS created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_families_user_id ON families(user_id);
CREATE INDEX IF NOT EXISTS idx_families_created_by ON families(created_by);

-- 2. Enable Row-Level Security on Core Tables
ALTER TABLE families ENABLE ROW LEVEL SECURITY;
ALTER TABLE persons ENABLE ROW LEVEL SECURITY;
ALTER TABLE application_statuses ENABLE ROW LEVEL SECURITY;
ALTER TABLE intake_extraction_logs ENABLE ROW LEVEL SECURITY;

-- Schemes and Glossary remain publicly readable by all authenticated and anonymous citizens
ALTER TABLE schemes ENABLE ROW LEVEL SECURITY;
ALTER TABLE eligibility_rules ENABLE ROW LEVEL SECURITY;
ALTER TABLE scheme_term_glossary ENABLE ROW LEVEL SECURITY;

-- 3. RLS Policies for SCHEMES & GLOSSARY (Public Read)
DROP POLICY IF EXISTS schemes_public_read ON schemes;
CREATE POLICY schemes_public_read ON schemes 
    FOR SELECT USING (is_active = true);

DROP POLICY IF EXISTS rules_public_read ON eligibility_rules;
CREATE POLICY rules_public_read ON eligibility_rules 
    FOR SELECT USING (true);

DROP POLICY IF EXISTS glossary_public_read ON scheme_term_glossary;
CREATE POLICY glossary_public_read ON scheme_term_glossary 
    FOR SELECT USING (true);

-- 4. RLS Policies for FAMILIES (Owner & Volunteer Access)
DROP POLICY IF EXISTS families_user_isolation_select ON families;
CREATE POLICY families_user_isolation_select ON families
    FOR SELECT
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
    );

DROP POLICY IF EXISTS families_user_isolation_insert ON families;
CREATE POLICY families_user_isolation_insert ON families
    FOR INSERT
    WITH CHECK (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
    );

DROP POLICY IF EXISTS families_user_isolation_update ON families;
CREATE POLICY families_user_isolation_update ON families
    FOR UPDATE
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'volunteer'
    );

DROP POLICY IF EXISTS families_user_isolation_delete ON families;
CREATE POLICY families_user_isolation_delete ON families
    FOR DELETE
    USING (
        auth.uid() = user_id 
        OR auth.uid() = created_by
        OR (auth.jwt() ->> 'role') = 'service_role'
    );

-- 5. RLS Policies for PERSONS (Inherited Family Isolation)
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
            )
        )
    );

-- 6. RLS Policies for APPLICATION_STATUSES
DROP POLICY IF EXISTS application_statuses_isolation ON application_statuses;
CREATE POLICY application_statuses_isolation ON application_statuses
    FOR ALL
    USING (
        EXISTS (
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

-- 7. RLS Policies for NOTIFICATION_LOGS
ALTER TABLE notification_logs ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS notification_logs_isolation ON notification_logs;
CREATE POLICY notification_logs_isolation ON notification_logs
    FOR ALL
    USING (
        EXISTS (
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

-- 8. RLS Policies for INTAKE_EXTRACTION_LOGS
DROP POLICY IF EXISTS intake_logs_access ON intake_extraction_logs;
CREATE POLICY intake_logs_access ON intake_extraction_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'authenticated'
        OR (auth.jwt() ->> 'role') = 'anon'
    );

