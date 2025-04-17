from sqlmodel import Session, SQLModel

from witch.db import get_engine
from witch.models import Witch


def create_db_and_tables() -> None:
    """Create the database and tables."""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def populate_db() -> None:
    """Populate the database with initial data."""
    witches = [
        Witch(name="Hermione Granger", type="good"),
        Witch(name="Bellatrix Lestrange", type="evil"),
        Witch(name="Samantha Stephens", type="good"),
    ]
    engine = get_engine()
    with Session(engine) as session:
        for witch in witches:
            session.add(witch)

        session.commit()


def main() -> None:
    """Main function to create the database and populate it."""
    create_db_and_tables()
    populate_db()


if __name__ == "__main__":
    main()
