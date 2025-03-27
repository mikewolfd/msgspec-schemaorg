from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.SoftwareApplication import SoftwareApplication
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DigitalPlatformEnumeration import DigitalPlatformEnumeration
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue


class EntryPoint(Struct, frozen=True):
    """An entry point, within some Web-based protocol."""
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
    urlTemplate: str | None = None
    application: 'SoftwareApplication' | None = None
    contentType: str | None = None
    encodingType: str | None = None
    actionPlatform: str | 'DigitalPlatformEnumeration' | str | None = None
    actionApplication: 'SoftwareApplication' | None = None
    httpMethod: str | None = None