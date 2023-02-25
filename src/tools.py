from typing import TypeVar, NamedTuple, Generic


IndexedT = TypeVar("IndexedT")


class Indexed(NamedTuple, Generic[IndexedT]):
    object_: IndexedT
    index: int