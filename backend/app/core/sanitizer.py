import re
import html
from typing import Optional


# Regular expressions for stripping potential script tags and dangerous HTML/JS payloads
HTML_TAG_PATTERN = re.compile(r"<[^>]+>", re.IGNORECASE)
SCRIPT_PATTERN = re.compile(r"(<script.*?>.*?</script>|javascript:|onerror=|onload=|eval\(|prompt\()", re.IGNORECASE | re.DOTALL)
SQL_INJECTION_PATTERN = re.compile(r"(--|;|\b(DROP|DELETE|TRUNCATE|ALTER|EXEC|UNION SELECT)\b)", re.IGNORECASE)

# Prompt injection markers to strip or escape before forwarding text to LLM
PROMPT_INJECTION_PATTERNS = [
    re.compile(r"(system:\s*ignore\s+previous\s+instructions)", re.IGNORECASE),
    re.compile(r"(you\s+are\s+now\s+in\s+developer\s+mode)", re.IGNORECASE),
    re.compile(r"(disregard\s+all\s+prior\s+rules)", re.IGNORECASE),
]


def sanitize_text(text: Optional[str], max_length: int = 1000) -> str:
    """Sanitizes raw user input:
    1. Trims leading/trailing whitespace
    2. Enforces maximum character length
    3. Strips HTML tags and JS execution handlers
    4. Escapes special HTML characters
    5. Neutralizes prompt injection patterns
    """
    if not text:
        return ""

    cleaned = text.strip()

    # Enforce maximum length
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]

    # Strip script tags & active scripts
    cleaned = SCRIPT_PATTERN.sub("", cleaned)
    cleaned = HTML_TAG_PATTERN.sub("", cleaned)

    # Neutralize prompt injection markers
    for pattern in PROMPT_INJECTION_PATTERNS:
        cleaned = pattern.sub("[filtered]", cleaned)

    # Escape HTML entities
    cleaned = html.escape(cleaned, quote=True)

    return cleaned


def sanitize_phone(phone: Optional[str]) -> str:
    """Sanitizes and normalizes phone number input (e.g. +91 94441 23456 -> +919444123456)."""
    if not phone:
        return ""
    # Keep only digits and leading +
    cleaned = re.sub(r"[^\d+]", "", phone.strip())
    if not cleaned.startswith("+"):
        if len(cleaned) == 10:
            cleaned = "+91" + cleaned
        elif len(cleaned) == 12 and cleaned.startswith("91"):
            cleaned = "+" + cleaned
    return cleaned
