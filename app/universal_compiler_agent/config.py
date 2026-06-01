"""Runtime configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Small settings object sourced from environment variables."""

    host: str = "127.0.0.1"
    port: int = 8000
    default_output_dir: str = "generated"
    max_requirements_chars: int = 100_000


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError as exc:
        msg = f"{name} must be an integer"
        raise ValueError(msg) from exc


def load_settings() -> Settings:
    """Load runtime settings from UPCA_* environment variables."""

    return Settings(
        host=os.getenv("UPCA_HOST", Settings.host),
        port=_int_env("UPCA_PORT", Settings.port),
        default_output_dir=os.getenv("UPCA_DEFAULT_OUTPUT_DIR", Settings.default_output_dir),
        max_requirements_chars=_int_env(
            "UPCA_MAX_REQUIREMENTS_CHARS", Settings.max_requirements_chars
        ),
    )
