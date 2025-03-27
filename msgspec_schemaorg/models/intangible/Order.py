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
    from msgspec_schemaorg.models.intangible.Invoice import Invoice
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.OrderItem import OrderItem
    from msgspec_schemaorg.models.intangible.OrderStatus import OrderStatus
    from msgspec_schemaorg.models.intangible.ParcelDelivery import ParcelDelivery
    from msgspec_schemaorg.models.intangible.PaymentMethod import PaymentMethod
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.Service import Service
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.product.Product import Product
from datetime import date, datetime


class Order(Struct, frozen=True):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer."""
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
    paymentMethod: 'PaymentMethod' | str | None = None
    billingAddress: 'PostalAddress' | None = None
    broker: 'Person' | 'Organization' | None = None
    merchant: 'Person' | 'Organization' | None = None
    paymentDueDate: datetime | date | None = None
    seller: 'Person' | 'Organization' | None = None
    isGift: bool | None = None
    orderStatus: 'OrderStatus' | None = None
    acceptedOffer: 'Offer' | None = None
    orderNumber: str | None = None
    orderDate: datetime | date | None = None
    customer: 'Person' | 'Organization' | None = None
    paymentMethodId: str | None = None
    orderDelivery: 'ParcelDelivery' | None = None
    discountCode: str | None = None
    discountCurrency: str | None = None
    partOfInvoice: 'Invoice' | None = None
    orderedItem: 'Product' | 'OrderItem' | 'Service' | None = None
    paymentDue: datetime | None = None
    discount: int | float | str | None = None
    confirmationNumber: str | None = None
    paymentUrl: str | None = None