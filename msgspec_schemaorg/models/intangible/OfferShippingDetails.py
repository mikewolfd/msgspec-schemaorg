from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DefinedRegion import DefinedRegion
    from msgspec_schemaorg.models.intangible.Distance import Distance
    from msgspec_schemaorg.models.intangible.Mass import Mass
    from msgspec_schemaorg.models.intangible.MemberProgramTier import MemberProgramTier
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.ShippingDeliveryTime import ShippingDeliveryTime
    from msgspec_schemaorg.models.intangible.ShippingRateSettings import ShippingRateSettings
    from msgspec_schemaorg.models.intangible.ShippingService import ShippingService


class OfferShippingDetails(Struct, frozen=True):
    """OfferShippingDetails represents information about shipping destinations.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

E.g. Cheaper and slower: $5 in 5-7 days
or Fast and expensive: $15 in 1-2 days."""
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
    shippingRate: 'ShippingRateSettings' | 'MonetaryAmount' | None = None
    validForMemberTier: 'MemberProgramTier' | None = None
    weight: 'QuantitativeValue' | 'Mass' | None = None
    deliveryTime: 'ShippingDeliveryTime' | None = None
    shippingOrigin: 'DefinedRegion' | None = None
    width: 'Distance' | 'QuantitativeValue' | None = None
    doesNotShip: bool | None = None
    depth: 'QuantitativeValue' | 'Distance' | None = None
    height: 'Distance' | 'QuantitativeValue' | None = None
    shippingDestination: 'DefinedRegion' | None = None
    hasShippingService: 'ShippingService' | None = None