from sqlalchemy.engine.base import Engine
from sqlmodel import Session, select

from witch import models


def test_get_witches(engine: Engine) -> None:
    with Session(engine) as session:
        witches = session.exec(select(models.Witch)).all()

    assert len(witches), "Should have at least one witch"
    assert isinstance(witches[0], models.Witch) is not None, "Witches should not be None"
