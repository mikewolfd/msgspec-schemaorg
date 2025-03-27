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
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.Order import Order
    from msgspec_schemaorg.models.intangible.PaymentMethod import PaymentMethod
    from msgspec_schemaorg.models.intangible.PaymentStatusType import PaymentStatusType
    from msgspec_schemaorg.models.intangible.PhysicalActivityCategory import PhysicalActivityCategory
    from msgspec_schemaorg.models.intangible.PriceSpecification import PriceSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import date, datetime


class Invoice(Struct, frozen=True):
    """A statement of the money due for goods or services; a bill."""
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
    paymentMethod: 'PaymentMethod' | str | None = None
    scheduledPaymentDate: date | None = None
    paymentStatus: 'PaymentStatusType' | str | None = None
    broker: 'Person' | 'Organization' | None = None
    paymentDueDate: datetime | date | None = None
    billingPeriod: 'Duration' | None = None
    referencesOrder: 'Order' | None = None
    category: 'CategoryCode' | str | 'Thing' | 'PhysicalActivityCategory' | str | None = None
    totalPaymentDue: 'MonetaryAmount' | 'PriceSpecification' | None = None
    customer: 'Person' | 'Organization' | None = None
    paymentMethodId: str | None = None
    accountId: str | None = None
    paymentDue: datetime | None = None
    minimumPaymentDue: 'PriceSpecification' | 'MonetaryAmount' | None = None
    confirmationNumber: str | None = None