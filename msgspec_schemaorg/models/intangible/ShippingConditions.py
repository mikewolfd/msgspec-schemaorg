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
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.OpeningHoursSpecification import OpeningHoursSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.ServicePeriod import ServicePeriod
    from msgspec_schemaorg.models.intangible.ShippingRateSettings import ShippingRateSettings


class ShippingConditions(Struct, frozen=True):
    """ShippingConditions represent a set of constraints and information about the conditions of shipping a product. Such conditions may apply to only a subset of the products being shipped, depending on aspects of the product like weight, size, price, destination, and others. All the specified conditions must be met for this ShippingConditions to apply."""
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
    numItems: 'QuantitativeValue' | None = None
    shippingRate: 'ShippingRateSettings' | 'MonetaryAmount' | None = None
    weight: 'QuantitativeValue' | 'Mass' | None = None
    orderValue: 'MonetaryAmount' | None = None
    seasonalOverride: 'OpeningHoursSpecification' | None = None
    shippingOrigin: 'DefinedRegion' | None = None
    width: 'Distance' | 'QuantitativeValue' | None = None
    doesNotShip: bool | None = None
    depth: 'QuantitativeValue' | 'Distance' | None = None
    height: 'Distance' | 'QuantitativeValue' | None = None
    shippingDestination: 'DefinedRegion' | None = None
    transitTime: 'ServicePeriod' | 'QuantitativeValue' | None = None