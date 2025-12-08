from keyword import iskeyword
from operator import ge, le
import shutil
from pathlib import Path

try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

project_name = "{{cookiecutter.project_name}}"
python_version = "{{cookiecutter.python_version}}"
project_structure = "{{cookiecutter.project_structure}}"
# Support both old 'deps_manager' and new 'package_manager' for backward compatibility
package_manager = "{{cookiecutter.package_manager if cookiecutter.package_manager else cookiecutter.deps_manager}}"
use_databricks = "{{cookiecutter.use_databricks}}"
use_airflow = "{{cookiecutter.use_airflow}}"
use_terraform = "{{cookiecutter.use_terraform}}"
use_mlflow = "{{cookiecutter.use_mlflow}}"
enable_drift_monitoring = "{{cookiecutter.enable_drift_monitoring}}"
enable_etl = "{{cookiecutter.enable_etl}}"

logger.info(f"Project name: {project_name}")
logger.info(f"Python version: {python_version}")
logger.info(f"Project structure: {project_structure}")
logger.info(f"Package manager: {package_manager}")
logger.info(f"Use Databricks: {use_databricks}")
logger.info(f"Use Airflow: {use_airflow}")
logger.info(f"Use Terraform: {use_terraform}")
logger.info(f"Use MLflow: {use_mlflow}")
logger.info(f"Enable drift monitoring: {enable_drift_monitoring}")
logger.info(f"Enable ETL: {enable_etl}")

if not project_name.isidentifier() or not project_name.islower():
    raise ValueError(
        "\n"
        "Project name must be a valid project name, meaning that it must be a valid Python name and also be lowercase."
        " This means that it must not contain spaces or special characters, and must not start with a number."
        " In general it is best to use only lowercase letters and underscores."
        " You can read more about Python naming conventions for packages here:"
        " https://peps.python.org/pep-0008/#package-and-module-names"
        "\n",
    )
if iskeyword(project_name):
    raise ValueError(
        "Project name must not be a built-in keyword, as it will cause syntax errors.",
    )

min_version = "3.10"
max_version = "3.13"
if not (ge(python_version, min_version) and le(python_version, max_version)):
    raise ValueError(
        f"Python version must be between {min_version} and {max_version}."
        " These are the versions that still receive support."
        " You can read more about Python versioning here: https://devguide.python.org/versions/",
    )

# Remove unnecessary files and folders for the simple template
if project_structure == "simple":
    logger.info("Removing unnecessary files and folders for the simple template.")
    folder_and_files_to_remove = [
        ".github", ".devcontainer", "dockerfiles", "docs",
    ]
    for f in folder_and_files_to_remove:
        if Path(f).exists():
            shutil.rmtree(f)

# Rename files and folders for the uv template
if package_manager == "uv":
    logger.info("Renaming files and folders for the uv template.")
    Path("requirements.txt").unlink()
    Path("requirements_dev.txt").unlink()
    Path("pyproject_pip.toml").unlink()
    Path("pyproject_uv.toml").rename("pyproject.toml")
    Path("tasks_pip.py").unlink()
    Path("tasks_uv.py").rename("tasks.py")
    if project_structure == "advance":
        Path("dockerfiles/api_pip.dockerfile").unlink()
        Path("dockerfiles/api_uv.dockerfile").rename("dockerfiles/api.dockerfile")
        Path("dockerfiles/train_pip.dockerfile").unlink()
        Path("dockerfiles/train_uv.dockerfile").rename("dockerfiles/train.dockerfile")
        Path(".devcontainer/post_create_pip.sh").unlink()
        Path(".devcontainer/post_create_uv.sh").rename(".devcontainer/post_create.sh")

if package_manager == "pip":
    logger.info("Renaming files and folders for the pip template.")
    Path("pyproject_uv.toml").unlink()
    Path("pyproject_pip.toml").rename("pyproject.toml")
    Path("tasks_uv.py").unlink()
    Path("tasks_pip.py").rename("tasks.py")
    if project_structure == "advance":
        Path("dockerfiles/api_uv.dockerfile").unlink()
        Path("dockerfiles/api_pip.dockerfile").rename("dockerfiles/api.dockerfile")
        Path("dockerfiles/train_uv.dockerfile").unlink()
        Path("dockerfiles/train_pip.dockerfile").rename("dockerfiles/train.dockerfile")
        Path(".devcontainer/post_create_uv.sh").unlink()
        Path(".devcontainer/post_create_pip.sh").rename(".devcontainer/post_create.sh")

# Handle optional components - placeholder for future implementation
# When actual Databricks/Airflow/Terraform/MLflow scaffolding is added to the template,
# these conditionals will remove them if disabled
logger.info("Processing optional components...")

if use_databricks == "no":
    logger.info("Databricks disabled - no files to remove (placeholder for future)")
    # Future: Remove databricks-specific files/folders when they exist
    # if Path("databricks").exists():
    #     shutil.rmtree("databricks")

if use_airflow == "no":
    logger.info("Airflow disabled - no files to remove (placeholder for future)")
    # Future: Remove airflow-specific files/folders when they exist
    # if Path("airflow").exists():
    #     shutil.rmtree("airflow")

if use_terraform == "no":
    logger.info("Terraform disabled - no files to remove (placeholder for future)")
    # Future: Remove terraform-specific files/folders when they exist
    # if Path("terraform").exists():
    #     shutil.rmtree("terraform")

if use_mlflow == "no":
    logger.info("MLflow disabled - no files to remove (placeholder for future)")
    # Future: Remove mlflow-specific files/folders when they exist

if enable_drift_monitoring == "no":
    logger.info("Drift monitoring disabled - no files to remove (placeholder for future)")
    # Future: Remove drift monitoring specific files when they exist

if enable_etl == "no":
    logger.info("ETL disabled - no files to remove (placeholder for future)")
    # Future: Remove ETL-specific files/folders when they exist

logger.info("Project generation completed successfully!")
