"""Requirement analysis and planning engine."""

from __future__ import annotations

import re
from collections.abc import Iterable

from .models import Priority, ProjectPlan, ProjectTask
from .safety import redact_secrets, slugify


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        clean = line.strip()
        if clean.startswith("#"):
            return clean.lstrip("#").strip()
    return None


def _sentences(text: str) -> Iterable[str]:
    for part in re.split(r"[\n.;!?]+", text):
        clean = part.strip(" -\t")
        if len(clean) >= 8:
            yield clean


def infer_stack(text: str) -> str:
    """Infer a lightweight implementation stack from requirement text."""

    lowered = text.lower()
    if any(word in lowered for word in ("api", "dashboard", "admin", "auth", "web")):
        return "Python 3.10+, FastAPI, SQLite, responsive HTML/CSS"
    if any(word in lowered for word in ("cli", "automation", "script", "termux")):
        return "Python 3.10+ CLI, SQLite-compatible file storage"
    return "Python 3.10+ CLI with optional FastAPI service"


def build_plan(requirements: str, project_name: str | None = None) -> ProjectPlan:
    """Turn raw requirements into a prioritized implementation plan."""

    safe_requirements = redact_secrets(requirements).strip()
    title = project_name or _first_heading(safe_requirements) or "Compiled Project"
    slug = slugify(title)
    stack = infer_stack(safe_requirements)
    features = tuple(list(_sentences(safe_requirements))[:8]) or (
        "Command line workflow for compiling requirements into runnable projects",
        "HTTP API for automation and future UI integrations",
        "Production-minded docs, scripts, tests, and configuration",
    )

    tasks = (
        ProjectTask(
            title="Bootstrap runnable application structure",
            priority=Priority.CRITICAL,
            reason="A generated project must be installable and executable on Termux/Linux.",
            fix="Create package layout, entrypoints, scripts, and dependency metadata.",
            files=("pyproject.toml", "app/", "scripts/"),
            impact="Users can start the project with minimal commands.",
        ),
        ProjectTask(
            title="Validate and sanitize all user input",
            priority=Priority.CRITICAL,
            reason=(
                "Compiler agents process arbitrary documents and must avoid path "
                "traversal or secret leaks."
            ),
            fix="Normalize project names, reject unsafe paths, and redact common secret patterns.",
            files=("app/universal_compiler_agent/safety.py",),
            impact="Reduces security risk when compiling untrusted text.",
        ),
        ProjectTask(
            title="Generate docs, tests, and deployment helpers",
            priority=Priority.HIGH,
            reason=(
                "Production-grade output needs repeatable setup, validation, "
                "and maintenance workflows."
            ),
            fix="Emit README, tests, setup/start/update/backup scripts, and CI configuration.",
            files=("docs/", "tests/", ".github/workflows/ci.yml"),
            impact="Improves maintainability and release confidence.",
        ),
        ProjectTask(
            title="Provide responsive API dashboard",
            priority=Priority.MEDIUM,
            reason="Non-technical users need a clear interface to understand generated plans.",
            fix="Expose FastAPI routes with accessible responsive HTML and JSON endpoints.",
            files=("app/universal_compiler_agent/server.py",),
            impact="Supports both browser and automation workflows.",
        ),
    )

    return ProjectPlan(
        name=title,
        slug=slug,
        stack=stack,
        summary=(
            "A Termux-first compiler agent project scaffold generated from "
            "the provided requirements."
        ),
        features=features,
        tasks=tasks,
        security_notes=(
            "All generated file paths are constrained to the output directory.",
            "Potential secrets in source requirements are redacted before being written to disk.",
            "Generated web services include conservative security headers.",
        ),
        performance_notes=(
            "The default runtime avoids heavyweight services and works on low-memory "
            "Android/Termux devices.",
            "Generated projects use simple file IO and lazy optional web dependencies "
            "where practical.",
        ),
    )
