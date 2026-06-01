"""Safety helpers for filesystem operations and generated content."""

from __future__ import annotations

import re
from pathlib import Path

_SAFE_SLUG = re.compile(r"[^a-z0-9._-]+")
_SECRET_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?([A-Za-z0-9_\-]{16,})"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def slugify(value: str, fallback: str = "compiled-project") -> str:
    """Convert arbitrary text into a safe project slug."""

    normalized = _SAFE_SLUG.sub("-", value.strip().lower()).strip(".-_")
    return normalized[:64] or fallback


def assert_safe_relative_path(path: Path) -> None:
    """Reject absolute paths and traversal attempts before writing generated files."""

    if path.is_absolute() or ".." in path.parts:
        msg = f"Unsafe generated path rejected: {path}"
        raise ValueError(msg)


def redact_secrets(text: str) -> str:
    """Redact common secret formats from user-provided text before persisting it."""

    redacted = text
    for pattern in _SECRET_PATTERNS:
        redacted = pattern.sub(
            lambda match: (
                match.group(0).replace(match.group(2), "[REDACTED]")
                if match.groups()
                else "[REDACTED_PRIVATE_KEY]"
            ),
            redacted,
        )
    return redacted


def escape_markdown(text: str) -> str:
    """Keep generated markdown stable without allowing raw HTML/script injection."""

    return text.replace("<", "&lt;").replace(">", "&gt;")
