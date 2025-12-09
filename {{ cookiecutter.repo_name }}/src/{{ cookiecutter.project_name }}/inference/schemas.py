from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class PredictionRequest(BaseModel):
    # Later: add real feature fields here
    features: Any | None = None


class PredictionResponse(BaseModel):
    predictions: List[float]
