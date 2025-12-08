# ML Boilerplate

*A modern, Databricks-friendly, end-to-end machine learning project template.*

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
[![Made with Cookiecutter](https://img.shields.io/badge/cookiecutter-template-blue.svg)](https://cookiecutter.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![pre-commit](https://results.pre-commit.ci/badge/github/vilhjalmur12/aiops_boilerplate/main.svg)](https://results.pre-commit.ci/latest/github/vilhjalmur12/aiops_boilerplate/main)

This repository provides a **single, unified boilerplate** for building production-grade ML pipelines with:

* **ETL**
* **Data Quality**
* **Training (MLflow)**
* **Inference (FastAPI + batch)**
* **Drift Monitoring (Evidently)**
* **Airflow orchestration**
* **Databricks compatibility**
* **Optional Terraform provisioning**

The template is intentionally **minimal**, **environment-agnostic**, and **flexible** — suitable for local development, Airflow pipelines, Databricks jobs, or cloud deployment.

---

## Development

### CI

The project uses GitHub Actions for CI, i would suggest having **act** installed locally to run the workflows before pushing.

Optional CI test runs:

```bash

```


---
## Features

#### End-to-End Lifecycle Out of the Box

The boilerplate supports the full ML workflow:

```
Raw Data 
   ↓
ETL (Ingest → Transform → Materialize)
   ↓
Data Quality (Great Expectations optional)
   ↓
Training (MLflow)
   ↓
Model Artifact
   ↓
Online Inference (FastAPI) + Batch Inference
   ↓
Monitoring & Drift (Evidently)
```

---

#### Databricks-Friendly, Not Databricks-Required

Run locally or on Databricks with no code changes.

Includes:

* Spark session builder (local + Databricks)
* Delta Lake utilities
* Databricks Job definitions
* Optional Databricks Asset Bundle scaffold
* Project-scoped Terraform examples

---

#### Airflow-Ready

Ships with:

* `etl_dag.py`
* `train_model_dag.py`
* `drift_monitoring_dag.py`

Each DAG calls the modular pipelines directly.

---

#### Strong Observability Patterns

* Centralized logging utilities
* Metrics middleware for the FastAPI service
* Evidently drift reports (HTML & JSON)
* Optional MLflow tracking of drift + metrics

---

#### Clean, Modular Code Structure

Everything is neatly separated:

```
src/
  project/
    config/        # YAML-driven configuration loader
    io/            # Spark/Delta + datasource utilities
    etl/           # Ingest, transform, materialize
    quality/       # Data validation (start with GE stubs)
    training/      # MLflow training pipeline
    inference/     # FastAPI + batch inference
    drift/         # Evidently drift pipelines
    evaluation/    # Model evaluation utilities
    monitoring/    # Logging + metrics helpers
    cli.py         # Optional unified CLI
```

---

#### Developer Experience Built-In

* `pip` or `uv` support
* Dockerfiles for API + training images
* `tasks_pip.py` and `tasks_uv.py` for easy execution
* Pre-commit hooks
* Initial tests that validate pipelines + structure
* MkDocs documentation scaffolding

---

## Getting Started

#### 1. Generate a project

```bash
cookiecutter gh:vilhjalmur12/aiops_boilerplate
```

Choose your:

* Project name
* Package name
* Whether to enable Databricks, Airflow, Terraform, etc.

---

#### 2. Install dependencies

```bash
pip install -r requirements.txt
# or
pip install -e .
```

---

#### 3. Run pipelines

#### ETL

```bash
python -m <project>.etl.pipeline
```

#### Data Quality

```bash
python -m <project>.quality.data_quality
```

#### Training

```bash
python -m <project>.training.train
```

#### Drift Monitoring

```bash
python -m <project>.drift.pipeline
```

---

#### 4. Start the inference API

```bash
uvicorn <project>.inference.api:app --reload
```

Visit:

* `http://localhost:8000/health`
* `http://localhost:8000/predict`
* `http://localhost:8000/docs`
* `http://localhost:8000/metrics`

---

## Project Structure (Generated Repo)

See `project_overview.md` for the full tree, but at a glance:

```
configs/          # YAML configs for Spark, MLflow, Airflow, Databricks, etc.
src/<project>/    # ML pipelines + utilities
airflow/          # DAGs
databricks/       # Job definitions + optional bundle
infra/terraform/  # Minimal Databricks IaC scaffold
dockerfiles/      # API + training images
docs/             # MkDocs documentation
tests/            # Unit tests across all modules
```

---

## Documentation

Once generated:

```bash
mkdocs serve
```

Documentation includes:

* Architecture overview
* How to run ETL, quality, training, inference, drift
* Databricks setup
* Airflow setup
* Data quality & Evidently examples

---

## Tooling & Integrations

| Area                | Tech                       |
| ------------------- | -------------------------- |
| Compute             | Spark (local + Databricks) |
| Storage Format      | Delta Lake                 |
| Orchestration       | Airflow (optional)         |
| Experiment Tracking | MLflow                     |
| Drift Detection     | Evidently                  |
| API Serving         | FastAPI                    |
| Infrastructure      | Terraform (optional)       |
| Containerization    | Docker                     |

---

## License

This project is licensed under the MIT License.
Forked and evolved from earlier MLOps template work.

---

## Contributing

Contributions are welcome!
Feel free to open issues or PRs to improve the template or add optional integrations.

---

## References

* [SkafteNicki/mlops_template](https://github.com/SkafteNicki/mlops_template) – Original MLOps template this project builds upon.


