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
