from __future__ import annotations
from msgspec import Struct, field


class CssSelectorType(Struct, frozen=True):
    """Text representing a CSS selector."""