from __future__ import annotations

from ..config.loader import get_config

def run_training() -> None:
    """Minimal training pipeline placeholder.
    """
    cfg = get_config(namespace="training")
    # For now, just prove we can touch config without error.
    _ = cfg  # noqa: F841
