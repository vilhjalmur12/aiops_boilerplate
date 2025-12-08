import os
import shutil
import tempfile
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def load_expectations() -> dict:
    cfg_path = REPO_ROOT / "tests" / "ci" / "template_expectations.yaml"
    with cfg_path.open() as f:
        return yaml.safe_load(f)


def assert_paths_exist(base: Path, paths: list[str], project_name: str):
    for raw in paths:
        rel = raw.replace("{{ cookiecutter.project_name }}", project_name)
        p = base / rel
        if not p.exists():
            raise AssertionError(f"Expected path missing: {p}")


def main():
    expectations = load_expectations()

    with tempfile.TemporaryDirectory() as tmpdir:
        project_root = REPO_ROOT / "build" / "repo_name"
        project_name = "project_name"  # assuming this is cookiecutter.project_name

        # 1) Structural checks
        assert_paths_exist(
            project_root,
            expectations.get("required_directories", []),
            project_name,
        )
        assert_paths_exist(
            project_root,
            expectations.get("required_files", []),
            project_name,
        )

        # 2) Very light smoke checks (optional)
        #    - Install & import basic modules
        #    - Avoid running heavy tests here

        venv_dir = project_root / ".venv"  # optional, or just rely on CI env
        # You can skip venv and just use CI python, e.g.:
        #   subprocess.check_call(["pip", "install", "-e", "."], cwd=project_root)

        print(f"Template validation succeeded for project at {project_root}")


if __name__ == "__main__":
    main()
