from witch import models
from sqlmodel import Session, select
from create_db import engine


def test_get_witches():
    with Session(engine) as session:
        witches = session.exec(select(models.Witch)).all()

    assert len(witches), "Should have at least one witch"
    assert isinstance(witches[0], models.Witch) is not None, (
        "Witches should not be None"
    )
