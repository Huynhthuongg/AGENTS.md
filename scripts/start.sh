#!/usr/bin/env sh
set -eu
HOST="${UPCA_HOST:-127.0.0.1}"
PORT="${UPCA_PORT:-8000}"
if [ -d .venv ]; then
  . .venv/bin/activate
fi
python -m uvicorn universal_compiler_agent.server:app --host "$HOST" --port "$PORT"
