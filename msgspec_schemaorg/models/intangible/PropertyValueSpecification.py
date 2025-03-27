from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.thing.Thing import Thing


class PropertyValueSpecification(Struct, frozen=True):
    """A Property value specification."""
    name: str | None = None
    mainEntityOfPage: str | 'CreativeWork' | None = None
    url: str | None = None
    disambiguatingDescription: str | None = None
    identifier: str | 'PropertyValue' | str | None = None
    description: str | 'TextObject' | None = None
    subjectOf: 'Event' | 'CreativeWork' | None = None
    alternateName: str | None = None
    additionalType: str | str | None = None
    potentialAction: 'Action' | None = None
    sameAs: str | None = None
    image: 'ImageObject' | str | None = None
    maxValue: int | float | None = None
    valueMinLength: int | float | None = None
    stepValue: int | float | None = None
    valueName: str | None = None
    valuePattern: str | None = None
    multipleValues: bool | None = None
    defaultValue: 'Thing' | str | None = None
    valueMaxLength: int | float | None = None
    valueRequired: bool | None = None
    readonlyValue: bool | None = None
    minValue: int | float | None = None