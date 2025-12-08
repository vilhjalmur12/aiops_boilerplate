import pytest
import os
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter


def test_wrong_config1(tmpdir):
    """Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config1.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )


def test_wrong_config2(tmpdir):
    """Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config2.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )


def test_wrong_config3(tmpdir):
    """Test that numbers are not allowed in the project name."""
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config3.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )

def test_wrong_config4(tmpdir):
    with pytest.raises(FailedHookException):
        cookiecutter(
            template=".",
            config_file="tests/wrong_config4.yaml",
            overwrite_if_exists=True,
            no_input=True,
            output_dir=str(tmpdir),
        )


def test_minimal_config(tmpdir):
    """Test that template generation works with all optional components disabled."""
    result = cookiecutter(
        template=".",
        config_file="configs/minimal_config.yaml",
        overwrite_if_exists=True,
        no_input=True,
        output_dir=str(tmpdir),
    )
    assert result is not None
    # Verify the generated directory exists
    assert os.path.exists(result)
