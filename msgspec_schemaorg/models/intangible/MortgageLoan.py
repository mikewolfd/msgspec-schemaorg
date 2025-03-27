from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.Certification import Certification
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.Review import Review
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.AggregateRating import AggregateRating
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.Brand import Brand
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.GeoShape import GeoShape
    from msgspec_schemaorg.models.intangible.GovernmentBenefitsType import GovernmentBenefitsType
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.OfferCatalog import OfferCatalog
    from msgspec_schemaorg.models.intangible.OpeningHoursSpecification import OpeningHoursSpecification
    from msgspec_schemaorg.models.intangible.PhysicalActivityCategory import PhysicalActivityCategory
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.RepaymentSpecification import RepaymentSpecification
    from msgspec_schemaorg.models.intangible.Service import Service
    from msgspec_schemaorg.models.intangible.ServiceChannel import ServiceChannel
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Product import Product
    from msgspec_schemaorg.models.thing.Thing import Thing


class MortgageLoan(Struct, frozen=True):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)"""
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
    aggregateRating: 'AggregateRating' | None = None
    hasCertification: 'Certification' | None = None
    isSimilarTo: 'Product' | 'Service' | None = None
    availableChannel: 'ServiceChannel' | None = None
    hoursAvailable: 'OpeningHoursSpecification' | None = None
    broker: 'Person' | 'Organization' | None = None
    serviceArea: 'GeoShape' | 'AdministrativeArea' | 'Place' | None = None
    isRelatedTo: 'Product' | 'Service' | None = None
    offers: 'Offer' | 'Demand' | None = None
    termsOfService: str | str | None = None
    category: 'CategoryCode' | str | 'Thing' | 'PhysicalActivityCategory' | str | None = None
    logo: str | 'ImageObject' | None = None
    award: str | None = None
    brand: 'Brand' | 'Organization' | None = None
    providerMobility: str | None = None
    audience: 'Audience' | None = None
    slogan: str | None = None
    review: 'Review' | None = None
    hasOfferCatalog: 'OfferCatalog' | None = None
    produces: 'Thing' | None = None
    areaServed: str | 'AdministrativeArea' | 'GeoShape' | 'Place' | None = None
    serviceAudience: 'Audience' | None = None
    serviceType: str | 'GovernmentBenefitsType' | None = None
    serviceOutput: 'Thing' | None = None
    feesAndCommissionsSpecification: str | str | None = None
    interestRate: 'QuantitativeValue' | int | float | None = None
    annualPercentageRate: int | float | 'QuantitativeValue' | None = None
    loanTerm: 'QuantitativeValue' | None = None
    loanRepaymentForm: 'RepaymentSpecification' | None = None
    loanType: str | str | None = None
    amount: 'MonetaryAmount' | int | float | None = None
    gracePeriod: 'Duration' | None = None
    recourseLoan: bool | None = None
    requiredCollateral: 'Thing' | str | None = None
    currency: str | None = None
    renegotiableLoan: bool | None = None
    domiciledMortgage: bool | None = None
    loanMortgageMandateAmount: 'MonetaryAmount' | None = None