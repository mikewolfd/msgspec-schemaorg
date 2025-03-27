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
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.GeoShape import GeoShape
    from msgspec_schemaorg.models.intangible.IncentiveQualifiedExpenseType import IncentiveQualifiedExpenseType
    from msgspec_schemaorg.models.intangible.IncentiveStatus import IncentiveStatus
    from msgspec_schemaorg.models.intangible.IncentiveType import IncentiveType
    from msgspec_schemaorg.models.intangible.LoanOrCredit import LoanOrCredit
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.PurchaseType import PurchaseType
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.UnitPriceSpecification import UnitPriceSpecification
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Product import Product
from datetime import date, datetime


class FinancialIncentive(Struct, frozen=True):
    """<p>Represents financial incentives for goods/services offered by an organization (or individual).</p>

<p>Typically contains the [[name]] of the incentive, the [[incentivizedItem]], the [[incentiveAmount]], the [[incentiveStatus]], [[incentiveType]], the [[provider]] of the incentive, and [[eligibleWithSupplier]].</p>

<p>Optionally contains criteria on whether the incentive is limited based on [[purchaseType]], [[purchasePriceLimit]], [[incomeLimit]], and the [[qualifiedExpense]].
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
    provider: 'Person' | 'Organization' | None = None
    incentiveType: 'IncentiveType' | None = None
    incomeLimit: 'MonetaryAmount' | str | None = None
    purchasePriceLimit: 'MonetaryAmount' | None = None
    incentivizedItem: 'DefinedTerm' | 'Product' | None = None
    incentiveStatus: 'IncentiveStatus' | None = None
    validFrom: datetime | date | None = None
    validThrough: date | datetime | None = None
    incentiveAmount: 'QuantitativeValue' | 'LoanOrCredit' | 'UnitPriceSpecification' | None = None
    purchaseType: 'PurchaseType' | None = None
    publisher: 'Organization' | 'Person' | None = None
    areaServed: str | 'AdministrativeArea' | 'GeoShape' | 'Place' | None = None
    qualifiedExpense: 'IncentiveQualifiedExpenseType' | None = None
    eligibleWithSupplier: 'Organization' | None = None