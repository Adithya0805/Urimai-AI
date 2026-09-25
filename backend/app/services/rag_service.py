"""RAG Service — Pinecone vector store for Urimai AI scheme documents.

Responsibilities:
1. build_scheme_document()      → Build text to embed per scheme
2. embed_and_upsert_schemes()   → Embed + push to Pinecone
3. retrieve_scheme_context()    → Query Pinecone by scheme_code
4. is_rag_available()           → Feature flag check
"""
from __future__ import annotations

import logging
from typing import List, Tuple, Dict, Any, Optional

from app.config import get_settings

logger = logging.getLogger(__name__)

# ── Constants ──────────────────────────────────────────────────────────────────
EMBEDDING_MODEL = "models/text-embedding-004"
EMBEDDING_DIMENSION = 768  # text-embedding-004 dimension
PINECONE_NAMESPACE = "schemes"


def is_rag_available() -> bool:
    """Returns True only when Pinecone + Google API keys are configured."""
    return get_settings().rag_available


# ── Document Builder ────────────────────────────────────────────────────────────

def build_scheme_document(scheme: Dict[str, Any]) -> str:
    """Constructs the plaintext document to embed for each scheme.

    Combines all human-readable scheme fields into a single rich text string
    so the embedding captures the full semantic content of the scheme.

    Args:
        scheme: Dict with scheme fields (from SCHEMES_DATA or DB row).

    Returns:
        A single text string ready for embedding.
    """
    parts = [
        f"Scheme Code: {scheme.get('scheme_code', '')}",
        f"Name (English): {scheme.get('name_english', '')}",
        f"Name (Tamil): {scheme.get('name_tamil', '')}",
        f"Transliteration: {scheme.get('name_transliteration', '')}",
        f"Department: {scheme.get('department', '')}",
        f"Category: {scheme.get('category', '')}",
        f"Benefit Amount: {scheme.get('benefit_amount', '')}",
        f"Description (English): {scheme.get('description_english', '')}",
        f"Description (Tamil): {scheme.get('description_tamil', '')}",
        f"Application Office: {scheme.get('application_office', '')}",
        f"Source URL: {scheme.get('source_url', '')}",
    ]

    docs = scheme.get("required_documents", [])
    if docs:
        parts.append("Required Documents: " + ", ".join(docs))

    return "\n".join(p for p in parts if p.split(": ", 1)[-1].strip())


# ── Pinecone Client ─────────────────────────────────────────────────────────────

def _get_pinecone_index():
    """Lazily initialise and return the Pinecone index object."""
    settings = get_settings()
    if not settings.PINECONE_API_KEY:
        raise RuntimeError("PINECONE_API_KEY is not set in environment.")

    from pinecone import Pinecone, ServerlessSpec  # type: ignore
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)

    index_name = settings.PINECONE_INDEX_NAME
    existing_indexes = [i.name for i in pc.list_indexes()]

    if index_name not in existing_indexes:
        logger.info("Creating Pinecone index '%s' (dim=%d).", index_name, EMBEDDING_DIMENSION)
        pc.create_index(
            name=index_name,
            dimension=EMBEDDING_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=settings.PINECONE_ENVIRONMENT),
        )

    return pc.Index(index_name)


def _get_embeddings():
    """Returns a Google Generative AI embeddings instance."""
    settings = get_settings()
    if not settings.GOOGLE_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY is not set in environment.")

    from langchain_google_genai import GoogleGenerativeAIEmbeddings  # type: ignore
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=settings.GOOGLE_API_KEY,
    )


# ── Embed + Upsert ──────────────────────────────────────────────────────────────

def embed_and_upsert_schemes(schemes: List[Dict[str, Any]], batch_size: int = 50) -> int:
    """Embeds scheme documents and upserts them into Pinecone.

    Each vector is stored with metadata:
        - scheme_code   (used for filtered retrieval)
        - department
        - category
        - text          (the full document text, for display)

    Args:
        schemes: List of scheme dicts (from SCHEMES_DATA).
        batch_size: Number of vectors to upsert per batch.

    Returns:
        Total number of vectors upserted.
    """
    if not is_rag_available():
        logger.warning("RAG not available (missing API keys). Skipping embed+upsert.")
        return 0

    index = _get_pinecone_index()
    embeddings_fn = _get_embeddings()

    documents = [build_scheme_document(s) for s in schemes]
    scheme_codes = [s["scheme_code"] for s in schemes]

    total_upserted = 0
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i : i + batch_size]
        batch_codes = scheme_codes[i : i + batch_size]
        batch_schemes = schemes[i : i + batch_size]

        logger.info("Embedding batch %d–%d ...", i, i + len(batch_docs))
        vectors = embeddings_fn.embed_documents(batch_docs)

        pinecone_vectors = []
        for j, (vec, code, doc, scheme) in enumerate(
            zip(vectors, batch_codes, batch_docs, batch_schemes)
        ):
            pinecone_vectors.append({
                "id": code,  # scheme_code is unique → use as vector ID
                "values": vec,
                "metadata": {
                    "scheme_code": code,
                    "department": scheme.get("department", ""),
                    "category": scheme.get("category", ""),
                    "text": doc[:2000],  # Pinecone metadata cap ~40KB per vector
                },
            })

        index.upsert(vectors=pinecone_vectors, namespace=PINECONE_NAMESPACE)
        total_upserted += len(pinecone_vectors)
        logger.info("Upserted %d vectors (total so far: %d).", len(pinecone_vectors), total_upserted)

    return total_upserted


# ── Retrieve ────────────────────────────────────────────────────────────────────

def retrieve_scheme_context(
    scheme_code: str,
    query_text: Optional[str] = None,
    top_k: int = 3,
) -> Tuple[List[str], float]:
    """Retrieves stored passages for a scheme from Pinecone.

    Uses scheme_code as the vector ID for direct lookup (fetch), which is
    faster and more precise than a similarity search for this use case —
    we always know exactly which scheme we need context for.

    Args:
        scheme_code: The unique scheme code, e.g. "TN-SW-OAP".
        query_text: Optional query text for similarity search fallback.
        top_k: Number of results to retrieve if doing similarity search.

    Returns:
        (passages, best_score) — passages is a list of text strings from
        the Pinecone metadata["text"] field; best_score is 1.0 for direct
        fetch (exact match), or the cosine similarity for search.
    """
    if not is_rag_available():
        return [], 0.0

    try:
        index = _get_pinecone_index()

        # Try direct fetch by vector ID (scheme_code) first — O(1), no embedding needed
        fetch_result = index.fetch(ids=[scheme_code], namespace=PINECONE_NAMESPACE)
        vectors = fetch_result.get("vectors", {})

        if scheme_code in vectors:
            text = vectors[scheme_code].get("metadata", {}).get("text", "")
            if text:
                return [text], 1.0

        # Fallback: similarity search if scheme not found by ID
        if query_text:
            embeddings_fn = _get_embeddings()
            query_vector = embeddings_fn.embed_query(query_text)
            results = index.query(
                vector=query_vector,
                top_k=top_k,
                namespace=PINECONE_NAMESPACE,
                filter={"scheme_code": {"$eq": scheme_code}},
                include_metadata=True,
            )
            matches = results.get("matches", [])
            if matches:
                passages = [m["metadata"].get("text", "") for m in matches if m.get("metadata")]
                best_score = matches[0].get("score", 0.0)
                return passages, best_score

        return [], 0.0

    except Exception as exc:
        logger.error("Pinecone retrieval failed for scheme '%s': %s", scheme_code, exc)
        return [], 0.0
