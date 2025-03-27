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
    from msgspec_schemaorg.models.intangible.DeliveryMethod import DeliveryMethod
    from msgspec_schemaorg.models.intangible.GeoShape import GeoShape
    from msgspec_schemaorg.models.intangible.MemberProgramTier import MemberProgramTier
    from msgspec_schemaorg.models.intangible.PriceSpecification import PriceSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Place import Place
from datetime import date, datetime


class DeliveryChargeSpecification(Struct, frozen=True):
    """The price for the delivery of an offer using a particular delivery method."""
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
    minPrice: int | float | None = None
    eligibleQuantity: 'QuantitativeValue' | None = None
    maxPrice: int | float | None = None
    validForMemberTier: 'MemberProgramTier' | None = None
    membershipPointsEarned: 'QuantitativeValue' | int | float | None = None
    price: str | int | float | None = None
    validFrom: datetime | date | None = None
    validThrough: date | datetime | None = None
    valueAddedTaxIncluded: bool | None = None
    eligibleTransactionVolume: 'PriceSpecification' | None = None
    priceCurrency: str | None = None
    eligibleRegion: str | 'GeoShape' | 'Place' | None = None
    appliesToDeliveryMethod: 'DeliveryMethod' | None = None
    ineligibleRegion: str | 'GeoShape' | 'Place' | None = None
    areaServed: str | 'AdministrativeArea' | 'GeoShape' | 'Place' | None = None