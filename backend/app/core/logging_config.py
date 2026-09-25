import logging
import sys
import json
from datetime import datetime, timezone
from typing import Any, Dict


class StructuredJsonFormatter(logging.Formatter):
    """Formats log records as structured JSON for production ingestion (CloudWatch, Datadog, Supabase)."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Include contextual fields if present
        if hasattr(record, "request_id"):
            log_entry["request_id"] = getattr(record, "request_id")
        if hasattr(record, "path"):
            log_entry["path"] = getattr(record, "path")
        if hasattr(record, "method"):
            log_entry["method"] = getattr(record, "method")
        if hasattr(record, "status_code"):
            log_entry["status_code"] = getattr(record, "status_code")
        if hasattr(record, "duration_ms"):
            log_entry["duration_ms"] = getattr(record, "duration_ms")
        if hasattr(record, "user_id"):
            log_entry["user_id"] = getattr(record, "user_id")

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry, ensure_ascii=False)


def setup_logging(log_level: str = "INFO", json_format: bool = False) -> logging.Logger:
    """Configures application-wide logging with consistent level and formatting."""
    root_logger = logging.getLogger("urimai")
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    # Remove existing handlers to avoid duplicates
    if root_logger.handlers:
        root_logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    if json_format:
        handler.setFormatter(StructuredJsonFormatter())
    else:
        fmt = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
        handler.setFormatter(logging.Formatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S"))

    root_logger.addHandler(handler)
    root_logger.propagate = False
    return root_logger


logger = logging.getLogger("urimai")
