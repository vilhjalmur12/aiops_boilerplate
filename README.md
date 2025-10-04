# AIOps Boilerplate

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
[![Release](https://img.shields.io/github/v/release/vilhjalmur12/aiops_boilerplate)](https://github.com/vilhjalmur12/aiops_boilerplate/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Cookiecutter](https://img.shields.io/badge/cookiecutter-template-blue.svg)](https://cookiecutter.readthedocs.io)
[![pre-commit](https://results.pre-commit.ci/badge/github/vilhjalmur12/aiops_boilerplate/main.svg)](https://results.pre-commit.ci/latest/github/vilhjalmur12/aiops_boilerplate/main)
[![codecov](https://codecov.io/gh/vilhjalmur12/aiops_boilerplate/branch/main/graph/badge.svg)](https://codecov.io/gh/vilhjalmur12/aiops_boilerplate)

A **full-stack AI/ML Ops boilerplate ecosystem** designed to accelerate development of AI/ML projects and services.
This template allows you to generate a **monorepo skeleton** and add **modular service templates** on the fly — covering the entire AI stack, from data services to ML pipelines and LLMOps.

## 📖 Description

The AIOps Boilerplate provides a consistent way to start, extend, and manage AI/ML projects.
It is designed to:

* Speed up project setup with ready-made templates for different AI/ML use cases.
* Ensure reproducibility and governance with built-in versioning and CI/CD.
* Support both open-source and cloud-native toolchains.
* Serve as a foundation for experimentation and production deployments across the AI stack.

## 🧭 Positioning

Unlike single-purpose templates or monolithic ML frameworks, the AIOps Boilerplate offers:

* **Full-stack coverage**: from data infrastructure and orchestration to ML pipelines, LLMOps, governance, and deployment.
* **Composable templates**: add services on the fly, tailored for specific AI/ML use cases.
* **OSS + Cloud parity**: runs locally with open-source services and scales seamlessly to cloud equivalents.
* **Maintainability built-in**: semantic versioning, changelogs, and upgrade path via Cruft/Copier.

This makes the project not just a starting point, but an evolving **ecosystem** for AI and ML operations.

## ✨ Features

* **Cookiecutter-powered** project generation.
* **Monorepo skeleton** with CI/CD, Docker/K8s, and observability.
* **13 service templates** for common AI/ML use cases:

  * MLOps pipeline
  * LLMOps
  * Forecasting
  * Data stacks (initial & extended)
  * Evaluation & testing
  * Governance
  * Streaming analytics
  * Simulation & synthetic data
  * Deployment-first microservices
  * Pre-analysis/EDA
  * Recommenders
* **OSS + cloud ready**: works with Postgres, Spark, Kafka, MinIO, Qdrant, and cloud equivalents.
* **Versioned and maintainable**: per-template semantic versioning, changelogs, and upgrade path via [Cruft](https://cruft.github.io/cruft/) or [Copier](https://copier.readthedocs.io).

## 🚀 Quickstart

Generate the monorepo:

```bash
cookiecutter gh:vilhjalmur12/aiops_boilerplate
```

Add a service:

```bash
./scripts/new_service.sh llmops service_slug=docs-rag svc_port=8092
```

Run locally:

```bash
docker-compose up
```

## 📚 Documentation

* [Project Overview](./docs/project_overview.md)
* [Epics and Roadmap](./docs/epics/)
* [Implementation Details](./docs/implementation/)

## 📜 License

This project is licensed under the MIT License.
It is **forked from [SkafteNicki/mlops_template](https://github.com/SkafteNicki/mlops_template)** and builds upon that foundation.
Please review the LICENSE file for details.

## 🔗 References

* [SkafteNicki/mlops_template](https://github.com/SkafteNicki/mlops_template) – Original MLOps template this project builds upon.
* [Cruft](https://cruft.github.io/cruft/) – Template evolution tool.
* [Copier](https://copier.readthedocs.io) – Alternative tool for template updating.
* [Cookiecutter](https://cookiecutter.readthedocs.io/) – Framework for generating project templates.
* [Qdrant](https://qdrant.tech/) – Open source vector database.
* [MinIO](https://min.io/) – S3-compatible object storage.
* [Apache Spark](https://spark.apache.org/) – Distributed compute engine.
* [Apache Kafka](https://kafka.apache.org/) – Streaming backbone.
* [MLflow](https://mlflow.org/) – Experiment tracking and model registry.

