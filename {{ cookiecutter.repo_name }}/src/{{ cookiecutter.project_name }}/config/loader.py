from __future__ import annotations
from typing import Any, Dict


def get_config(namespace: str | None = None) -> Dict[str, Any]:
    """Return a minimal config dict.
    """
    base: Dict[str, Any] = {
        "project": "{{ cookiecutter.project_name }}",
    }

    if namespace is None:
        return base

    # Namespaced configs added later
    return {**base, "namespace": namespace}
