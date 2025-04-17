# ruff: noqa
from sqlmodel import Field, SQLModel


class Witch(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str


# class User:  noqa: ERA001
#     name: str


# class Img:
#     path: Path


# class Item:
#     ingredient: str
#     amount: float
#     units: str

#     def __str__(self):
#         return f"{self.ingredient}, {self.amount}, {self.units}"


# class thing(Protocol):
#     name: str
#     picture: Img

#     def make(self): ...


# class Potion(thing):
#     name: str
#     _items: list[Item] | None = None
#     picture: Img

#     def add_item(self, item: Item) -> None:
#         self._items.append(item)

#     def make(self) -> None:
#         return


# class Spell(thing):
#     name: str
#     words: str | None = None
#     actions: list[str] = None

#     def make(self): ...
