from __future__ import annotations
from msgspec import Struct, field


class URL(Struct, frozen=True):
    """Data type: URL."""