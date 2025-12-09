# drift/pipeline.py
from __future__ import annotations

from .data_drift import compute_data_drift
from .model_drift import compute_model_drift
from .reference_sets import get_reference_data


def run_drift_monitoring() -> None:
    """Minimal drift monitoring pipeline placeholder."""
    ref = get_reference_data()
    _ = ref  # noqa: F841
    compute_data_drift()
    compute_model_drift()
