from __future__ import annotations
from msgspec import Struct, field


class Integer(Struct, frozen=True):
    """Data type: Integer."""