from fastapi.testclient import TestClient
from universal_compiler_agent.server import app


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
