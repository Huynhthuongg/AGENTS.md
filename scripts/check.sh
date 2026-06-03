#!/usr/bin/env sh
set -eu

missing=""
for command in ruff codespell; do
  if ! command -v "$command" >/dev/null 2>&1; then
    missing="$missing $command"
  fi
done

for module in pytest httpx2 httpx; do
  if ! python -c "import ${module}" >/dev/null 2>&1; then
    missing="$missing $module"
  fi
done

if [ -n "$missing" ]; then
  echo "Missing development dependencies:$missing" >&2
  echo "Run: python -m pip install -e '.[dev]'" >&2
  exit 1
fi

ruff check .
codespell README.md docs app tests pyproject.toml scripts config public vercel.json
pytest -q
