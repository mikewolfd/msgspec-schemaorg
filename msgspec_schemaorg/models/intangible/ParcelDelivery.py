from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.DeliveryEvent import DeliveryEvent
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DeliveryMethod import DeliveryMethod
    from msgspec_schemaorg.models.intangible.Order import Order
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.product.Product import Product
from datetime import date, datetime


class ParcelDelivery(Struct, frozen=True):
    """The delivery of a parcel either via the postal service or a commercial service."""
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
    provider: 'Person' | 'Organization' | None = None
    hasDeliveryMethod: 'DeliveryMethod' | None = None
    expectedArrivalUntil: datetime | date | None = None
    partOfOrder: 'Order' | None = None
    trackingNumber: str | None = None
    itemShipped: 'Product' | None = None
    deliveryAddress: 'PostalAddress' | None = None
    deliveryStatus: 'DeliveryEvent' | None = None
    originAddress: 'PostalAddress' | None = None
    expectedArrivalFrom: datetime | date | None = None
    carrier: 'Organization' | None = None
    trackingUrl: str | None = None