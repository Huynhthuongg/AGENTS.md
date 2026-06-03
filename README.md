# Universal Project Compiler Agent

<p align="center">
  <img src="public/badges/termux.svg" alt="Termux ready" />
  <img src="public/badges/fastapi.svg" alt="FastAPI powered" />
  <img src="public/badges/vercel.svg" alt="Vercel ready" />
</p>

<p align="center">
  <strong>Android-first compiler agent for turning requirements into secure, runnable project scaffolds.</strong><br />
  <a href="public/index.html">Preview the landing page</a> · <a href="https://vercel.com/new">Deploy on Vercel</a>
</p>

Android-first, Termux-first development agent that transforms documents, specifications, repositories, OCR text, Markdown, or natural language requests into complete, runnable, maintainable software project scaffolds.

The original product specification is preserved in [docs/SPECIFICATION.md](docs/SPECIFICATION.md).

## What is included

- A Python CLI named `upca` for local compilation workflows.
- A FastAPI service with `/health`, `/plan`, and `/compile` endpoints.
- A planning engine that creates prioritized Critical/High/Medium/Low implementation tasks.
- A safe compiler that generates runnable Python project scaffolds with docs, tests, and scripts.
- Secret redaction, safe slug generation, path traversal protection, and HTTP security headers.
- Termux-friendly setup, start, update, and backup scripts.
- CI, tests, and architecture documentation.

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


## Vercel landing page

A polished static introduction page is included in `public/` with animated SVG badges and Vercel routing/security headers in `vercel.json`.

```bash
npm i -g vercel
vercel deploy --prod
```

If deploying from CI, provide your Vercel token as an environment secret and run `vercel deploy --prod --token "$VERCEL_TOKEN"`.

## Development

```bash
python -m pip install -e '.[dev]'
./scripts/check.sh
```

`./scripts/check.sh` verifies development dependencies, then runs Ruff, Codespell, and the full pytest suite so release checks match CI. The Vercel landing page lives in `public/` and is served as a static site.

## Current release

- Version: 0.1.1
- Release date: 2026-06-02
- Release focus: CLI dry-run previews, safe output directory validation, dashboard route alignment, and test workflow hardening.

## Security model

- Never hardcode secrets in generated output.
- Redact common API key, token, secret, and password patterns from persisted requirement snapshots.
- Reject unsafe generated paths and unsafe API `output_dir` values.
- Add conservative HTTP headers to API responses.

## License

AGPL-3.0-only. See [LICENSE](LICENSE).
