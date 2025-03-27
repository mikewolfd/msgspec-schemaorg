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
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
from datetime import date, datetime


class CDCPMDRecord(Struct, frozen=True):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format
      used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for details, and the linked CDC materials for authoritative
      definitions used as the source here.
      """
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
    cvdNumTotBeds: int | float | None = None
    datePosted: datetime | date | None = None
    cvdFacilityCounty: str | None = None
    cvdNumICUBedsOcc: int | float | None = None
    cvdFacilityId: str | None = None
    cvdNumC19HospPats: int | float | None = None
    cvdNumBedsOcc: int | float | None = None
    cvdNumVentUse: int | float | None = None
    cvdNumBeds: int | float | None = None
    cvdNumC19Died: int | float | None = None
    cvdNumICUBeds: int | float | None = None
    cvdNumC19HOPats: int | float | None = None
    cvdNumC19OverflowPats: int | float | None = None
    cvdCollectionDate: datetime | str | None = None
    cvdNumVent: int | float | None = None
    cvdNumC19OFMechVentPats: int | float | None = None
    cvdNumC19MechVentPats: int | float | None = None