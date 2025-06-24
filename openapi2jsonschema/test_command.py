import os
import pytest  # type: ignore
from click.testing import CliRunner

from openapi2jsonschema.command import default

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../fixtures")


@pytest.mark.datafiles(FIXTURE_DIR)
def test_command(datafiles):
    runner = CliRunner()
    for spec in datafiles.iterdir():
        if not spec.is_file():
            continue
        result = runner.invoke(default, ["file://%s" % spec])
        assert result.exit_code == 0


def test_version():
    runner = CliRunner()
    result = runner.invoke(default, ["--help"])
    assert result.exit_code == 0
