"""FastAPI application for browser and automation workflows."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

from .compiler import compile_project
from .planner import build_plan
from .templates import INDEX_HTML

APP_VERSION = "0.1.1"


class PlanRequest(BaseModel):
    requirements: str = Field(min_length=1, max_length=100_000)
    project_name: str | None = Field(default=None, max_length=120)


class CompileRequest(PlanRequest):
    output_dir: str = Field(default="generated", max_length=240)


def _safe_output_dir(value: str) -> Path:
    output_dir = Path(value)
    if output_dir.is_absolute() or ".." in output_dir.parts:
        raise HTTPException(status_code=400, detail="output_dir must be a safe relative path")
    return output_dir


def create_app() -> FastAPI:
    app = FastAPI(title="Universal Project Compiler Agent", version=APP_VERSION)

    @app.middleware("http")
    async def security_headers(request: Request, call_next):  # type: ignore[no-untyped-def]
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        return response

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return INDEX_HTML

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/plan")
    def plan(request: PlanRequest) -> JSONResponse:
        generated_plan = build_plan(request.requirements, request.project_name)
        return JSONResponse(asdict(generated_plan), media_type="application/json")

    @app.post("/compile")
    def compile_endpoint(request: CompileRequest) -> dict[str, object]:
        result = compile_project(
            request.requirements,
            _safe_output_dir(request.output_dir),
            request.project_name,
        )
        return {"root": str(result.root), "file_count": result.file_count, "slug": result.plan.slug}

    return app


app = create_app()
