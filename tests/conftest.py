import pytest
import bddrest
from functools import partial
from shortener import app


@pytest.fixture
def Given():
    return partial(bddrest.Given, app)
