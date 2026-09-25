-- Migration 007: Add llm_call_logs table
-- Audit trail for every Gemini LLM call (NLU extraction + guidance generation)

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
