from pathlib import Path

from universal_compiler_agent.compiler import compile_project
from universal_compiler_agent.safety import assert_safe_relative_path, redact_secrets, slugify


def test_compile_project_writes_expected_files(tmp_path: Path) -> None:
    result = compile_project("# Demo App\nBuild a CLI automation tool", tmp_path)

    assert result.root.name == "demo-app"
    assert (result.root / "README.md").exists()
    assert (result.root / "compile-manifest.json").exists()
    assert result.file_count >= 6


def test_safety_helpers() -> None:
    assert slugify("Hello World!") == "hello-world"
    assert "[REDACTED]" in redact_secrets("api_key=abcdefghijklmnopqrstuvwxyz")


def test_rejects_unsafe_relative_path() -> None:
    try:
        assert_safe_relative_path(Path("../escape.txt"))
    except ValueError:
        return
    raise AssertionError("unsafe path was not rejected")
