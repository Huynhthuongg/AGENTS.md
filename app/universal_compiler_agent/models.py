"""Typed domain models for project compilation."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class Priority(str, Enum):
    """Task priority levels used by the planning engine."""

    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


@dataclass(frozen=True)
class ProjectTask:
    """A concrete implementation task generated from a user requirement."""

    title: str
    priority: Priority
    reason: str
    fix: str
    files: tuple[str, ...]
    impact: str


@dataclass(frozen=True)
class ProjectPlan:
    """A production-oriented plan for the generated project."""

    name: str
    slug: str
    stack: str
    summary: str
    features: tuple[str, ...]
    tasks: tuple[ProjectTask, ...]
    security_notes: tuple[str, ...]
    performance_notes: tuple[str, ...]


@dataclass(frozen=True)
class GeneratedFile:
    """A file emitted by the compiler."""

    path: Path
    content: str


@dataclass
class CompileResult:
    """Result returned after generating a project."""

    plan: ProjectPlan
    root: Path
    files: list[GeneratedFile] = field(default_factory=list)

    @property
    def file_count(self) -> int:
        return len(self.files)
