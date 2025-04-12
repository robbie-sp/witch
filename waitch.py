from fasthtml.common import FastHTML, Main, Title, Div, P
from pathlib import Path
from typing import Protocol

app = FastHTML()

rt = app.route


@rt("/", methods="get")
def home():
    Title("Waitch")
    Main(Div(P("This is where Waitch goes.")))


# def db_setup()
#     db = database("witch.db")
#     if "Todo" not in db.t:
#     db.t["Todo"].create(id=int, title=str, done=bool, pk="id")


class User:
    name: str


class Img:
    path: Path


class Item:
    ingredient: str
    amount: float
    units: str

    def __str__(self):
        return f"{self.ingredient}, {self.amount}, {self.units}"


class thing(Protocol):
    name: str
    picture: Img

    def make(self): ...


class Potion(thing):
    name: str
    _items: list[Item] | None = None
    picture: Img

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    def make(self) -> None:
        return


class Spell(thing):
    name: str
    words: str | None = None
    actions: list[str] = None

    def make(self): ...
