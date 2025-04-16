from pathlib import Path

from witch import db


def test_db_url():
    """Test the db_url function."""

    # Test with a specific file name and location
    db_file_name = "test_db.db"
    db_location = Path(__file__).parent

    assert db.db_url(db_file_name=db_file_name, db_location=db_location) == (
        f"sqlite:///{db_location}/{db_file_name}"
    ), "Should return the correct SQLite URL"


def test_get_engine():
    """Test the get_engine function."""

    # Test if the engine is created successfully
    engine = db.get_engine()
    assert engine is not None, "Engine should not be None"
    assert str(engine.url) == (
        f"sqlite:///{Path(__file__).parent}/witch_database.db"
    ), "Engine URL should match the expected SQLite URL"
