from __future__ import annotations
from msgspec import Struct, field


class DataType(Struct, frozen=True):
    """The basic data types such as Integers, Strings, etc."""