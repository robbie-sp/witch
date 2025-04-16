from fasthtml import ft
from fasthtml.common import (
    Redirect,
    fast_app,
)
from sqlmodel import Session, select

from witch.db import get_engine
from witch.models import Witch

app, rt = fast_app()

engine = get_engine()


# Route to display the list of witches and a form to add more
@rt("/")
def get():
    # Fetch witches from the database
    with Session(engine) as session:
        witches = session.exec(select(Witch)).all()

    # Generate the HTML for the list of witches
    witch_list = ft.Ul(*[ft.Li(f"{witch.name} - {witch.type}") for witch in witches])

    # Form to add a new witch
    add_form = ft.Form(
        Method="post",
        Action="/add",
        Children=[
            ft.Label("Name:", For="name"),
            ft.Input(Name="name", Type="text", Required=True),
            ft.Br(),
            ft.Label("Type:", For="type"),
            ft.Input(Name="type", Type="text", Required=True),
            ft.Br(),
            ft.Button("Add Witch", Type="submit"),
        ],
    )

    # Return the page
    return ft.Titled("Witches List", witch_list, ft.H2("Add a New Witch"), add_form)


# Route to handle adding a new witch
@rt("/add")
def post(name: str, type: str):
    # Add the new witch to the database
    with Session(engine) as session:
        new_witch = Witch(name=name, type=type)
        session.add(new_witch)
        session.commit()

    # Redirect back to the main page
    return Redirect("/")
