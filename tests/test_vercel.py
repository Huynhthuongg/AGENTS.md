import importlib.util
import json
from pathlib import Path

from fastapi.testclient import TestClient


def test_vercel_routes_all_paths_to_fastapi_entrypoint() -> None:
    config = json.loads(Path("vercel.json").read_text(encoding="utf-8"))

    assert config["builds"] == [{"src": "api/index.py", "use": "@vercel/python"}]
    assert config["routes"] == [{"src": "/(.*)", "dest": "api/index.py"}]


def test_vercel_entrypoint_exposes_fastapi_app() -> None:
    spec = importlib.util.spec_from_file_location("vercel_entrypoint", "api/index.py")
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    response = TestClient(module.app).get("/")

    assert response.status_code == 200
    assert "Universal Project Compiler Agent" in response.text
