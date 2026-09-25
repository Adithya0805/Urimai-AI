-- ==============================================================================
-- Urimai AI — Migration 010: WhatsApp Channel & Multi-Day Session Schema
-- Target: Supabase / PostgreSQL
-- ==============================================================================

-- 1. Create WHATSAPP_SESSIONS Table
CREATE TABLE IF NOT EXISTS whatsapp_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(50) NOT NULL,
    user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    family_id UUID REFERENCES families(id) ON DELETE SET NULL,
    current_step VARCHAR(50) NOT NULL DEFAULT 'greet',
    state_data JSONB NOT NULL DEFAULT '{}'::jsonb,
    status VARCHAR(50) NOT NULL DEFAULT 'active', -- 'active', 'completed', 'awaiting_resume_choice'
    whatsapp_consent BOOLEAN NOT NULL DEFAULT FALSE,
    consent_at TIMESTAMPTZ,
    last_user_message_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_phone ON whatsapp_sessions(phone_number);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_user_id ON whatsapp_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_status ON whatsapp_sessions(status);
CREATE INDEX IF NOT EXISTS idx_whatsapp_sessions_last_msg ON whatsapp_sessions(last_user_message_at);

-- 2. Create WHATSAPP_MESSAGE_LOGS Table
CREATE TABLE IF NOT EXISTS whatsapp_message_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone_number VARCHAR(50) NOT NULL,
    direction VARCHAR(20) NOT NULL, -- 'inbound', 'outbound'
    message_type VARCHAR(50) NOT NULL DEFAULT 'session', -- 'session', 'template', 'quick_reply'
    template_name VARCHAR(100),
    body TEXT NOT NULL,
    is_within_24h BOOLEAN NOT NULL DEFAULT TRUE,
    status VARCHAR(50) NOT NULL DEFAULT 'sent', -- 'received', 'sent', 'failed'
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_whatsapp_logs_phone ON whatsapp_message_logs(phone_number);
CREATE INDEX IF NOT EXISTS idx_whatsapp_logs_created_at ON whatsapp_message_logs(created_at DESC);

-- 3. Enable Row-Level Security
ALTER TABLE whatsapp_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE whatsapp_message_logs ENABLE ROW LEVEL SECURITY;

-- 4. RLS Policies: Service role and Admins have full access
DROP POLICY IF EXISTS "Service role has full access to whatsapp_sessions" ON whatsapp_sessions;
CREATE POLICY "Service role has full access to whatsapp_sessions"
    ON whatsapp_sessions
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );

DROP POLICY IF EXISTS "Service role has full access to whatsapp_message_logs" ON whatsapp_message_logs;
CREATE POLICY "Service role has full access to whatsapp_message_logs"
    ON whatsapp_message_logs
    FOR ALL
    USING (
        (auth.jwt() ->> 'role') = 'service_role'
        OR (auth.jwt() ->> 'role') = 'admin'
        OR (auth.jwt() -> 'user_metadata' ->> 'role') = 'admin'
    );
