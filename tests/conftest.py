import pytest
from sqlalchemy.engine.base import Engine

from witch.db import get_config, get_engine


@pytest.fixture
def engine() -> Engine:
    config = get_config()
    return get_engine(config)
