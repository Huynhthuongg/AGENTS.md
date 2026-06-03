from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from fastapi.testclient import TestClient
from universal_compiler_agent.server import app


def test_dashboard_uses_public_api_routes() -> None:
    response = TestClient(app).get("/")

    assert response.status_code == 200
    assert "submit('/plan'" in response.text
    assert "submit('/compile'" in response.text
    assert "/api/plan" not in response.text
    assert "/api/compile" not in response.text


def test_dashboard_includes_release_landing_content() -> None:
    response = TestClient(app).get("/")

    assert response.status_code == 200
    assert "Vercel-ready" in response.text
    assert "Built for fast release paths" in response.text
    assert "vercel deploy --prod" in response.text


def test_health_endpoint() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert response.headers["x-content-type-options"] == "nosniff"


def test_plan_endpoint() -> None:
    response = TestClient(app).post(
        "/plan", json={"requirements": "# Portal\nNeed API auth dashboard"}
    )

    assert response.status_code == 200
    assert response.json()["slug"] == "portal"


def test_compile_endpoint_rejects_unsafe_output_dir() -> None:
    response = TestClient(app).post(
        "/compile",
        json={"requirements": "# Portal", "output_dir": "../escape"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "output_dir must be a safe relative path"


def test_compile_endpoint_writes_scaffold(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.chdir(tmp_path)

    response = TestClient(app).post(
        "/compile",
        json={"requirements": "# Portal", "output_dir": "generated"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["slug"] == "portal"
    assert (tmp_path / body["root"] / "README.md").exists()


def test_compile_endpoint_honors_output_base(tmp_path: Path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setenv("UPCA_OUTPUT_BASE", str(tmp_path / "serverless"))

    response = TestClient(app).post(
        "/compile",
        json={"requirements": "# Portal", "output_dir": "generated"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["root"].startswith(str(tmp_path / "serverless"))
    assert (Path(body["root"]) / "compile-manifest.json").exists()


def test_vercel_entrypoint_exports_fastapi_app() -> None:
    spec = importlib.util.spec_from_file_location("vercel_entrypoint", "api/index.py")
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    assert module.app is app


def test_vercel_config_routes_to_python_entrypoint() -> None:
    config = json.loads(Path("vercel.json").read_text(encoding="utf-8"))

    assert config["rewrites"] == [{"source": "/(.*)", "destination": "/api/index.py"}]
    assert config["env"]["UPCA_OUTPUT_BASE"] == "/tmp/upca"
    assert "api/index.py" in config["functions"]
    assert Path(".python-version").read_text(encoding="utf-8").strip() == "3.12"
