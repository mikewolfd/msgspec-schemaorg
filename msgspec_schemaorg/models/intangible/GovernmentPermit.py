from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.Service import Service
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
from datetime import date, datetime


class GovernmentPermit(Struct, frozen=True):
    """A permit issued by a government agency."""
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
    issuedThrough: 'Service' | None = None
    validFor: 'Duration' | None = None
    validFrom: datetime | date | None = None
    validIn: 'AdministrativeArea' | None = None
    validUntil: date | None = None
    issuedBy: 'Organization' | None = None
    permitAudience: 'Audience' | None = None