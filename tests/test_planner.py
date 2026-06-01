from universal_compiler_agent.planner import build_plan, infer_stack


def test_build_plan_prioritizes_security() -> None:
    plan = build_plan("# Client Portal\nNeed API, auth, dashboard, dark mode")

    assert plan.slug == "client-portal"
    assert any(task.priority.value == "Critical" for task in plan.tasks)
    assert any("secret" in note.lower() for note in plan.security_notes)


def test_infer_stack_detects_api() -> None:
    assert "FastAPI" in infer_stack("Build an API dashboard")
