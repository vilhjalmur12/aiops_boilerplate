.PHONY: structure render validate test lint clean

# ---------------------------------------------
# Settings
# ---------------------------------------------

# Temp directory for rendering the template
BUILD_DIR := .build
RENDERED_PROJECT := $(BUILD_DIR)/rendered

# ---------------------------------------------
# Display project structure (your existing rule)
# ---------------------------------------------

EMPTY_DIRS := ./notebooks ./models ./docs/tmp ./inference/configs ./training/configs ./reports ./data

structure:
	@find . \
	  \( -type d \( -name venv -o -name .venv -o -name __pycache__ -o -name .idea -o -name .git \) \) -prune -o \
	  \( $(foreach d,$(EMPTY_DIRS),-path '$(d)' -o) -false \) -print -prune -o \
	  -print \
	| sed 's|^\./||' \
	| tree --fromfile

# ---------------------------------------------
# Template Utilities
# ---------------------------------------------

# Render the cookiecutter template using defaults
render:
	rm -rf $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)
	cookiecutter . --no-input --output-dir $(BUILD_DIR)
	@echo "Template rendered to: $(RENDERED_PROJECT)"

# Validate template using the repository script (ci/validate_template.py)
validate:
	python ci/validate_template.py

# Lint template repo (YAML, Python in ci/, cookiecutter JSON)
lint:
	ruff check .
	yamllint .
	jsonlint cookiecutter.json

# ---------------------------------------------
# Test generated project
# ---------------------------------------------
# - Installs dependencies of the rendered project
# - Runs pytest (in the generated repo)
# - Avoids mixing template dev env with generated env

test: render
	@echo "Running tests inside rendered project..."
	cd $(RENDERED_PROJECT) && pip install -r requirements.txt
	cd $(RENDERED_PROJECT) && pytest -q

# ---------------------------------------------
# Housekeeping
# ---------------------------------------------

clean:
	rm -rf $(BUILD_DIR)
	find . -name "__pycache__" -type d -exec rm -rf {} +
