from witch.models import Witch
from sqlmodel import SQLModel, Session
from witch.db import get_engine


def create_db_and_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
    print(f"Database is stored at: {engine.url.database}")


def populate_db():
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


def main():
    create_db_and_tables()
    populate_db()


if __name__ == "__main__":
    main()
