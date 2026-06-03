# Changelog

## 0.1.2 - 2026-06-03

- Redesigned the dashboard into a polished project landing page with animated visual elements, release highlights, and deploy guidance.
- Added GitHub README badges for CI, Python versions, FastAPI, Vercel readiness, release, and license.
- Added Vercel deployment wiring with an ASGI entrypoint, `vercel.json`, runtime requirements, and serverless-safe compile output routing through `/tmp/upca`.
- Kept generated release screenshots out of review diffs to avoid unsupported binary-file rendering.

## 0.1.1 - 2026-06-02

- Added CLI `compile --dry-run` support for release-safe plan previews.
- Rejected unsafe CLI and API output directories before project generation.
- Served the maintained dashboard template from the FastAPI root route and aligned its buttons with `/plan` and `/compile`.
- Updated release metadata and development dependencies for the current test client stack.

## 0.1.0

- Implemented the initial Universal Project Compiler Agent CLI and FastAPI service.
- Added safe project generation, input sanitization, secret redaction, and path validation.
- Added Termux-friendly setup/start/update/backup scripts, tests, CI, and architecture docs.
