# ruff: noqa: ANN201, D103

from fasthtml import ft
from fasthtml.common import Redirect, fast_app, picolink
from sqlmodel import Session, select

from witch.db import get_config, get_engine
from witch.models import Witch

app, rt = fast_app(hdrs=picolink, live=True, debug=True)

config = get_config()
engine = get_engine(config)


@rt("/")
def get():
    """Route to display the list of witches and a form to add more."""
    # Fetch witches from the database
    # with Session(engine) as session:
    #     witches = session.exec(select(Witch)).all()

    # Generate the HTML for the list of witches
    # witch_list = ft.Ul(*[ft.Li(f"{witch.name} - {witch.type}") for witch in witches])

    witch_list = ft.Ul(
        ft.Li("Witch 1 - Type A"),
        ft.Li("Witch 2 - Type B"),
        ft.Li("Witch 3 - Type C"),
    )

    # Form to add a new witch
    add_form = ft.Form(
        ft.Label("Name:", _for="name"),
        ft.Input(name="name", id="name"),
        ft.Br(),
        ft.Label("Type:", _for="witch_type"),
        ft.Input(Name="witch_type", id="witch_type"),
        ft.Br(),
        ft.Button("Add another Witch"),
        hx_post="/add",
        action="/add",
        method="post",
    )

    # Return the page
    return ft.Titled("Witches List", witch_list, ft.H2("Add a New Witch"), add_form)


@rt("/add")
def post(name: str, witch_type: str):
    """Route to handle adding a new witch."""
    # Add the new witch to the database
    with Session(engine) as session:
        new_witch = Witch(name=name, type=witch_type)
        session.add(new_witch)
        session.commit()

    # Redirect back to the main page
    return Redirect("/")
