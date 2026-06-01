"""FastAPI application for browser and automation workflows."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

from .compiler import compile_project
from .planner import build_plan


class PlanRequest(BaseModel):
    requirements: str = Field(min_length=1, max_length=100_000)
    project_name: str | None = Field(default=None, max_length=120)


class CompileRequest(PlanRequest):
    output_dir: str = Field(default="generated", max_length=240)


def create_app() -> FastAPI:
    app = FastAPI(title="Universal Project Compiler Agent", version="0.1.0")

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
        return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Universal Project Compiler Agent</title>
  <script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
  <style>
    :root { color-scheme: light dark; --bg:#0b1020; --card:#11172b; --text:#eef2ff; --muted:#aab4d4; --accent:#7c3aed; }
    * { box-sizing: border-box; }
    body { margin:0; min-height:100vh; font-family: Inter, ui-sans-serif, system-ui, sans-serif; background: radial-gradient(circle at top, #1d2b64, var(--bg)); color:var(--text); }
    main { width:min(1040px, 100%); margin:auto; padding: clamp(24px, 5vw, 72px); }
    .hero { display:grid; gap:24px; }
    .badge { width:max-content; border:1px solid #ffffff22; border-radius:999px; padding:8px 12px; color:var(--muted); background:#ffffff0d; }
    h1 { font-size:clamp(42px, 8vw, 82px); line-height:.95; letter-spacing:-0.06em; margin:0; }
    p { color:var(--muted); font-size:clamp(16px, 2vw, 20px); max-width:760px; }
    .grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-top:36px; }
    .card { background: color-mix(in srgb, var(--card) 88%, white 12%); border:1px solid #ffffff14; border-radius:24px; padding:22px; box-shadow:0 20px 60px #0006; }
    code { color:#c4b5fd; }
  </style>
</head>
<body><main><section class="hero">
  <div class="badge">Android-first • Termux-first • Production-ready</div>
  <h1>Compile requirements into runnable software projects.</h1>
  <p>Use <code>POST /plan</code> to analyze requirements or <code>POST /compile</code> to emit a secure, maintainable scaffold with docs, tests, and scripts.</p>
</section><section class="grid">
  <div class="card"><h2>CLI</h2><p><code>upca compile --input-file spec.md</code></p></div>
  <div class="card"><h2>API</h2><p>JSON endpoints for automation and future UI integrations.</p></div>
  <div class="card"><h2>Security</h2><p>Path safety, secret redaction, and hardened HTTP headers.</p></div>
</section></main></body></html>
"""

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/plan")
    def plan(request: PlanRequest) -> JSONResponse:
        generated_plan = build_plan(request.requirements, request.project_name)
        return JSONResponse(asdict(generated_plan), media_type="application/json")

    @app.post("/compile")
    def compile_endpoint(request: CompileRequest) -> dict[str, object]:
        output_dir = Path(request.output_dir)
        if output_dir.is_absolute() or ".." in output_dir.parts:
            raise HTTPException(status_code=400, detail="output_dir must be a safe relative path")
        result = compile_project(request.requirements, output_dir, request.project_name)
        return {"root": str(result.root), "file_count": result.file_count, "slug": result.plan.slug}

    return app


app = create_app()
