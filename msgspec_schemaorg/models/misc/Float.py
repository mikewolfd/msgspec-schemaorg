from __future__ import annotations
from msgspec import Struct, field


class Float(Struct, frozen=True):
    """Data type: Floating number."""