# Universal Project Compiler Agent

<p align="center">
  <a href="https://github.com/Huynhthuongg/AGENTS.md/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Huynhthuongg/AGENTS.md/ci.yml?branch=main&style=for-the-badge&logo=github&label=CI"></a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-ready-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img alt="Vercel" src="https://img.shields.io/badge/Vercel-deployable-000000?style=for-the-badge&logo=vercel&logoColor=white">
  <img alt="Version" src="https://img.shields.io/badge/release-0.1.2-8B5CF6?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-AGPL--3.0--only-blue?style=for-the-badge">
</p>

Android-first, Termux-first development agent that transforms documents, specifications, repositories, OCR text, Markdown, or natural language requests into complete, runnable, maintainable software project scaffolds.

The original product specification is preserved in [docs/SPECIFICATION.md](docs/SPECIFICATION.md). The project now ships with a polished dashboard, live API docs, GitHub badges, CI checks, and Vercel deployment wiring.

## What is included

- A Python CLI named `upca` for local compilation workflows.
- A FastAPI service with `/health`, `/plan`, and `/compile` endpoints.
- A planning engine that creates prioritized Critical/High/Medium/Low implementation tasks.
- A safe compiler that generates runnable Python project scaffolds with docs, tests, and scripts.
- Secret redaction, safe slug generation, path traversal protection, and HTTP security headers.
- Termux-friendly setup, start, update, and backup scripts.
- CI, tests, architecture documentation, Vercel configuration, and GitHub project badges.

## Quick start

```bash
./scripts/setup.sh
./scripts/start.sh
```

Open <http://127.0.0.1:8000> or use the CLI:

```bash
upca plan --text "# CRM Dashboard\nNeed auth, API, admin dashboard, dark mode"
upca compile --text "# CRM Dashboard\nNeed auth, API, admin dashboard" --output-dir generated
```

## Termux setup

```bash
pkg update
pkg install python git
./scripts/setup.sh
```

The default architecture avoids Docker, Kubernetes, and heavy services so it can run on low-memory Android devices.

## Deploy to Vercel

This repo includes a Vercel ASGI entrypoint and `vercel.json`, so the FastAPI dashboard and API can run as a Python Function.

```bash
npm i -g vercel
vercel login
vercel deploy --prod
```

Vercel routes every request to `api/index.py`, while generated compile output is redirected to `/tmp/upca` through `UPCA_OUTPUT_BASE` for serverless-safe writes.

## API examples

```bash
curl -s http://127.0.0.1:8000/health
curl -s -X POST http://127.0.0.1:8000/plan \
  -H 'content-type: application/json' \
  -d '{"requirements":"# Portal\nNeed API, dashboard, auth and mobile responsive UI"}'
```

## Project structure

```text
app/universal_compiler_agent/  Application package
config/                        Example runtime configuration
docs/                          Architecture and changelog
scripts/                       Setup, start, update, backup helpers
tests/                         Unit tests
.github/workflows/             CI checks
```

## Development

```bash
python -m pip install -e '.[dev]'
./scripts/check.sh
```

`./scripts/check.sh` runs Ruff and the full pytest suite so release checks match CI.

## Current release

- Version: 0.1.2
- Release date: 2026-06-03
- Release focus: redesigned project landing page, GitHub badges, Vercel deployment wiring, and serverless-safe compile output paths.

## Security model

- Never hardcode secrets in generated output.
- Redact common API key, token, secret, and password patterns from persisted requirement snapshots.
- Reject unsafe generated paths and unsafe API `output_dir` values.
- Add conservative HTTP headers to API responses.

## License

AGPL-3.0-only. See [LICENSE](LICENSE).
