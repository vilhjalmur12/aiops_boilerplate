from __future__ import annotations

from fastapi import FastAPI

from .schemas import HealthResponse, PredictionRequest, PredictionResponse
from .service import predict as _predict

app = FastAPI(title="{{ cookiecutter.project_name }} Inference API")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    predictions = _predict(request)
    return PredictionResponse(predictions=predictions)
