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
    from msgspec_schemaorg.models.intangible.AggregateOffer import AggregateOffer
    from msgspec_schemaorg.models.intangible.BusinessEntityType import BusinessEntityType
    from msgspec_schemaorg.models.intangible.BusinessFunction import BusinessFunction
    from msgspec_schemaorg.models.intangible.DeliveryMethod import DeliveryMethod
    from msgspec_schemaorg.models.intangible.GeoShape import GeoShape
    from msgspec_schemaorg.models.intangible.ItemAvailability import ItemAvailability
    from msgspec_schemaorg.models.intangible.LoanOrCredit import LoanOrCredit
    from msgspec_schemaorg.models.intangible.MenuItem import MenuItem
    from msgspec_schemaorg.models.intangible.OfferItemCondition import OfferItemCondition
    from msgspec_schemaorg.models.intangible.PaymentMethod import PaymentMethod
    from msgspec_schemaorg.models.intangible.PriceSpecification import PriceSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.Service import Service
    from msgspec_schemaorg.models.intangible.Trip import Trip
    from msgspec_schemaorg.models.intangible.TypeAndQuantityNode import TypeAndQuantityNode
    from msgspec_schemaorg.models.intangible.WarrantyPromise import WarrantyPromise
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Product import Product
from datetime import date, datetime, time


class Demand(Struct, frozen=True):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply."""
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
    eligibleQuantity: 'QuantitativeValue' | None = None
    eligibleRegion: str | 'GeoShape' | 'Place' | None = None
    availabilityStarts: time | datetime | date | None = None
    sku: str | None = None
    priceSpecification: 'PriceSpecification' | None = None
    eligibleCustomerType: 'BusinessEntityType' | None = None
    availability: 'ItemAvailability' | None = None
    inventoryLevel: 'QuantitativeValue' | None = None
    eligibleDuration: 'QuantitativeValue' | None = None
    mpn: str | None = None
    serialNumber: str | None = None
    gtin12: str | None = None
    gtin13: str | None = None
    deliveryLeadTime: 'QuantitativeValue' | None = None
    seller: 'Person' | 'Organization' | None = None
    advanceBookingRequirement: 'QuantitativeValue' | None = None
    gtin: str | str | None = None
    validFrom: datetime | date | None = None
    asin: str | str | None = None
    availableDeliveryMethod: 'DeliveryMethod' | None = None
    validThrough: date | datetime | None = None
    warranty: 'WarrantyPromise' | None = None
    businessFunction: 'BusinessFunction' | None = None
    eligibleTransactionVolume: 'PriceSpecification' | None = None
    itemCondition: 'OfferItemCondition' | None = None
    includesObject: 'TypeAndQuantityNode' | None = None
    ineligibleRegion: str | 'GeoShape' | 'Place' | None = None
    gtin14: str | None = None
    areaServed: str | 'AdministrativeArea' | 'GeoShape' | 'Place' | None = None
    acceptedPaymentMethod: 'PaymentMethod' | str | 'LoanOrCredit' | None = None
    gtin8: str | None = None
    availableAtOrFrom: 'Place' | None = None
    itemOffered: 'Trip' | 'Product' | 'AggregateOffer' | 'MenuItem' | 'Service' | 'Event' | 'CreativeWork' | None = None
    availabilityEnds: date | time | datetime | None = None