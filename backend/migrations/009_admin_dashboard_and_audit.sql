-- Migration: 009_admin_dashboard_and_audit.sql
-- Description: Creates admin_audit_logs table and configures Admin Role RLS policies

-- 1. Create ADMIN_AUDIT_LOGS Table
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

-- 2. Enable RLS on admin_audit_logs, scheme_review_queue, and llm_call_logs
ALTER TABLE admin_audit_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE scheme_review_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE llm_call_logs ENABLE ROW LEVEL SECURITY;

-- 3. Policy: Only Administrators can view and insert audit logs
DROP POLICY IF EXISTS "Admins can view and create audit logs" ON admin_audit_logs;
CREATE POLICY "Admins can view and create audit logs"
    ON admin_audit_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 4. Cross-Family Read/Manage Policies for Admin Role on Application Status, Families & Persons
DROP POLICY IF EXISTS "Admins have cross-family access to application statuses" ON application_statuses;
CREATE POLICY "Admins have cross-family access to application statuses"
    ON application_statuses
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Admins have cross-family access to families" ON families;
CREATE POLICY "Admins have cross-family access to families"
    ON families
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Admins have cross-family access to persons" ON persons;
CREATE POLICY "Admins have cross-family access to persons"
    ON persons
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 5. Admin Full Access to Scheme Review Queue
DROP POLICY IF EXISTS "Admins have full access to scheme review queue" ON scheme_review_queue;
CREATE POLICY "Admins have full access to scheme review queue"
    ON scheme_review_queue
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 6. Admin Write Access to Schemes, Eligibility Rules, and Glossary
DROP POLICY IF EXISTS "Admins have write access to schemes" ON schemes;
CREATE POLICY "Admins have write access to schemes"
    ON schemes
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Admins have write access to eligibility rules" ON eligibility_rules;
CREATE POLICY "Admins have write access to eligibility rules"
    ON eligibility_rules
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Admins have write access to glossary" ON scheme_term_glossary;
CREATE POLICY "Admins have write access to glossary"
    ON scheme_term_glossary
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

-- 7. LLM Call Logs Access Policy
DROP POLICY IF EXISTS "LLM logs access for admin and service role" ON llm_call_logs;
CREATE POLICY "LLM logs access for admin and service role"
    ON llm_call_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    )
    WITH CHECK (
        (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
        OR (auth.jwt() ->> 'role') = 'service_role'
    );
