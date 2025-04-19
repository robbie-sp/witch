from witch import db


def test_get_engine_sqlite() -> None:
    """Test the get_engine function."""
    config = {
        "sqlite_path": "witch_database.db",
        "db_echo": True,
        "db_driver": "sqlite",
    }

    # Test if the engine is created successfully
    engine = db.get_engine(config)
    assert engine is not None, "Engine should not be None"
    assert engine.name == "sqlite", "Engine should be SQLite"


def test_get_engine_postgres() -> None:
    """Test the get_engine function."""
    config = db.get_config()

    # Test if the engine is created successfully
    engine = db.get_engine(config)
    assert engine is not None, "Engine should not be None"
    assert engine.name == "postgresql", "Engine should be SQLite"


def test_create_url_object() -> None:
    """Test the create_url_object function."""
    config = {
        "db_driver": "postgresql",
        "db_username": "user",
        "db_password": "password",
        "db_host": "localhost",
        "db_database": "test_db",
    }

    url = db.create_url_object(config)
    url_string = url.render_as_string(hide_password=False)
    assert url_string == "postgresql://user:password@localhost/test_db", "URL string should be formatted correctly"
