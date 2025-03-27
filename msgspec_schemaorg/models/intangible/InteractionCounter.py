from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.SoftwareApplication import SoftwareApplication
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.creativework.WebSite import WebSite
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.VirtualLocation import VirtualLocation
    from msgspec_schemaorg.models.place.Place import Place
from datetime import datetime, time


class InteractionCounter(Struct, frozen=True):
    """A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction."""
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
    startTime: time | datetime | None = None
    interactionType: 'Action' | None = None
    location: str | 'Place' | 'VirtualLocation' | 'PostalAddress' | None = None
    endTime: time | datetime | None = None
    interactionService: 'SoftwareApplication' | 'WebSite' | None = None
    userInteractionCount: int | None = None