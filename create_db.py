from sqlmodel import Session, SQLModel, text

from witch.db import get_config, get_engine
from witch.models import Witch

config = get_config()


def create_db() -> None:
    """Create the database."""
    engine = get_engine(config)

    if config["db_driver"] == "postgresql":
        with engine.connect() as conn:
            conn.execute(text("commit"))  # commits an empty transaction to allow database creation
            query = "CREATE DATABASE witch"
            conn.execute(text(query))


def create_tables() -> None:
    """Create the database (if sqlite) and tables."""
    engine = get_engine(config)
    SQLModel.metadata.create_all(engine)


def populate_db() -> None:
    """Populate the database with initial data."""
    witches = [
        Witch(name="Hermione Granger", type="good"),
        Witch(name="Bellatrix Lestrange", type="evil"),
        Witch(name="Samantha Stephens", type="good"),
    ]
    engine = get_engine(config)
    with Session(engine) as session:
        for witch in witches:
            session.add(witch)

        session.commit()


def main() -> None:
    """Main function to create the database and populate it."""
    create_db()
    create_tables()
    populate_db()


if __name__ == "__main__":
    main()
