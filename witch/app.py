from fasthtml.common import fast_app
from fasthtml.common import Ul, Li, Form, Label, Input, Br, Button, Titled, H2, Redirect
from sqlmodel import Session, select
from witch.models import Witch
from witch.db import get_engine


app, rt = fast_app()

engine = get_engine()


# Route to display the list of witches and a form to add more
@rt("/")
def get():
    # Fetch witches from the database
    with Session(engine) as session:
        witches = session.exec(select(Witch)).all()

    # Generate the HTML for the list of witches
    witch_list = Ul(*[Li(f"{witch.name} - {witch.type}") for witch in witches])

    # Form to add a new witch
    add_form = Form(
        Method="post",
        Action="/add",
        Children=[
            Label("Name:", For="name"),
            Input(Name="name", Type="text", Required=True),
            Br(),
            Label("Type:", For="type"),
            Input(Name="type", Type="text", Required=True),
            Br(),
            Button("Add Witch", Type="submit"),
        ],
    )

    # Return the page
    return Titled("Witches List", witch_list, H2("Add a New Witch"), add_form)


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
