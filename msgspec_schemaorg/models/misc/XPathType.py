from __future__ import annotations
from msgspec import Struct, field


class XPathType(Struct, frozen=True):
    """Text representing an XPath (typically but not necessarily version 1.0)."""