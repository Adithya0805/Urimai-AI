"""seed_pinecone.py — CLI script to embed all 64 schemes into Pinecone.

Usage (from the backend directory):
    python -m app.seed_pinecone

Requires:
    GOOGLE_API_KEY and PINECONE_API_KEY to be set in .env

What it does:
    1. Loads all 64 schemes from SCHEMES_DATA (app/seed_data.py)
    2. Builds a rich text document per scheme
    3. Embeds each document using Google text-embedding-004
    4. Upserts to Pinecone index "urimai-schemes" (created if not exists)

Run this once after initial setup, and again after adding new schemes.
"""
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    from app.config import get_settings
    settings = get_settings()

    # ── Preflight checks ──────────────────────────────────────────────────────
    errors = []
    if not settings.GOOGLE_API_KEY:
        errors.append("GOOGLE_API_KEY is not set. Get one at https://aistudio.google.com/app/apikey")
    if not settings.PINECONE_API_KEY:
        errors.append("PINECONE_API_KEY is not set. Get one at https://app.pinecone.io")

    if errors:
        logger.error("Cannot seed Pinecone — missing required configuration:")
        for e in errors:
            logger.error("  ✗ %s", e)
        sys.exit(1)

    logger.info("Starting Pinecone seed for Urimai AI schemes...")
    logger.info("  Pinecone index  : %s", settings.PINECONE_INDEX_NAME)
    logger.info("  Embedding model : models/text-embedding-004")
    logger.info("  Threshold       : %.2f", settings.RAG_SIMILARITY_THRESHOLD)

    # ── Load scheme data ──────────────────────────────────────────────────────
    from app.seed_data import SCHEMES_DATA
    # Merge with department-specific schemes
    from app.seed_data_departments.education import EDUCATION_SCHEMES
    from app.seed_data_departments.agriculture import AGRICULTURE_SCHEMES
    from app.seed_data_departments.labour import LABOUR_SCHEMES

    all_schemes = SCHEMES_DATA  # Already includes all departments via imports in seed_data.py
    logger.info("Loaded %d schemes to embed.", len(all_schemes))

    # ── Embed + Upsert ────────────────────────────────────────────────────────
    from app.services.rag_service import embed_and_upsert_schemes, build_scheme_document

    # Preview first scheme document
    if all_schemes:
        sample = build_scheme_document(all_schemes[0])
        logger.info("\nSample document for '%s':\n%s\n%s",
                    all_schemes[0].get("scheme_code"), "─" * 60,
                    sample[:500] + ("..." if len(sample) > 500 else ""))

    count = embed_and_upsert_schemes(all_schemes)
    logger.info("\n✅ Seeded %d scheme vectors into Pinecone index '%s'.",
                count, settings.PINECONE_INDEX_NAME)
    logger.info("You can now use the /guidance endpoints with RAG-grounded Tamil explanations.")


if __name__ == "__main__":
    main()
