from pathlib import Path

import pytest
from universal_compiler_agent.cli import main


def test_cli_dry_run_prints_plan(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["compile", "--dry-run", "--text", "# Demo\nNeed API", "--name", "Demo"])

    assert exit_code == 0
    assert '"slug": "demo"' in capsys.readouterr().out


def test_cli_compile_rejects_unsafe_output_dir(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.chdir(tmp_path)

    with pytest.raises(SystemExit):
        main(["compile", "--text", "# Demo", "--output-dir", "../escape"])
