"""Command line interface for Universal Project Compiler Agent."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .compiler import compile_project
from .planner import build_plan


def _read_input(args: argparse.Namespace) -> str:
    if args.input_file:
        return Path(args.input_file).read_text(encoding="utf-8")
    if args.text:
        return args.text
    return "Universal Project Compiler Agent"


def _safe_output_dir(value: str) -> Path:
    output_dir = Path(value)
    if output_dir.is_absolute() or ".." in output_dir.parts:
        msg = "output_dir must be a safe relative path"
        raise argparse.ArgumentTypeError(msg)
    return output_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile requirements into a runnable project scaffold."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan = subparsers.add_parser(
        "plan", help="Analyze requirements and print a prioritized plan as JSON."
    )
    plan.add_argument("--input-file", help="Path to a requirements document.")
    plan.add_argument("--text", help="Inline requirements text.")
    plan.add_argument("--name", help="Override generated project name.")

    compile_cmd = subparsers.add_parser("compile", help="Generate a project from requirements.")
    compile_cmd.add_argument("--input-file", help="Path to a requirements document.")
    compile_cmd.add_argument("--text", help="Inline requirements text.")
    compile_cmd.add_argument("--name", help="Override generated project name.")
    compile_cmd.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated plan as JSON without writing files.",
    )
    compile_cmd.add_argument(
        "--output-dir",
        default=Path("generated"),
        type=_safe_output_dir,
        help="Safe relative directory that will receive output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    requirements = _read_input(args)

    if args.command == "plan" or args.dry_run:
        plan = build_plan(requirements, args.name)
        print(json.dumps(asdict(plan), indent=2))
        return 0

    result = compile_project(requirements, args.output_dir, args.name)
    print(f"Generated {result.file_count} files in {result.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
