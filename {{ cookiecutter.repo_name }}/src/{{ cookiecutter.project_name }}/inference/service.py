from __future__ import annotations

from .schemas import PredictionRequest


def predict(request: PredictionRequest) -> list[float]:
    """Dummy predict function.
    """
    _ = request  # noqa: F841
    return []
