import uuid
from sqlalchemy import Column, String, Text, Float, Boolean, DateTime, func
from app.database import Base
from app.models.family import GUID


class LlmCallLog(Base):
    """Audit log for every LLM call made by Urimai AI.

    Covers two call types:
    - "nlu_extraction"  : Gemini called to parse Tamil free text → enum value
    - "guidance_generation" : Gemini called to write Tamil guidance text grounded
                              in Pinecone-retrieved scheme passages.

    This table is the audit trail if a user later disputes a piece of guidance
    or an extracted field value.
    """
    __tablename__ = "llm_call_logs"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)

    # Who triggered this call
    call_type = Column(String(50), nullable=False, index=True)
    # "nlu_extraction" or "guidance_generation"

    session_id = Column(String(100), nullable=True, index=True)
    # Populated for intake NLU calls; links to intake_extraction_logs.session_id

    person_id = Column(String(36), nullable=True, index=True)
    # Populated for guidance calls

    scheme_code = Column(String(100), nullable=True, index=True)
    # Populated for guidance calls; identifies which scheme's guidance was generated

    # ── What went in ─────────────────────────────────────────────────────────
    prompt_text = Column(Text, nullable=False)
    # Full prompt sent to Gemini

    retrieved_context = Column(Text, nullable=True)
    # Pinecone passages concatenated, if RAG was used; NULL for NLU calls

    retrieval_score = Column(Float, nullable=True)
    # Highest cosine similarity score from Pinecone; NULL if RAG not used

    used_rag = Column(Boolean, nullable=False, default=False)
    # True = Pinecone context was above threshold and sent to Gemini

    # ── What came out ────────────────────────────────────────────────────────
    llm_output = Column(Text, nullable=False)
    # Raw text response from Gemini

    # ── Metadata ─────────────────────────────────────────────────────────────
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
