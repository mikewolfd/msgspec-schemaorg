from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.intangible.Language import Language


class PronounceableText(Struct, frozen=True):
    """Data type: PronounceableText."""
    phoneticText: str | None = None
    inLanguage: str | 'Language' | None = None
    speechToTextMarkup: str | None = None
    textValue: str | None = None