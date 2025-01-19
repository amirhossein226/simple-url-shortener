import pytest
import bddrest
from functools import partial
from shortener.shortener import app
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )))


@pytest.fixture
def Given():
    return partial(bddrest.Given, app)
