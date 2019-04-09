import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from conf import settings


@pytest.fixture(autouse=True)
def my_fixture():
    """
    To avoid sharing Settings state between tests, before running each of the tests
    settings are initialized with empty dict.
    """
    settings.data = {}
    yield
