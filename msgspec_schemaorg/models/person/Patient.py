from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.Certification import Certification
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.EducationalOccupationalCredential import EducationalOccupationalCredential
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.Brand import Brand
    from msgspec_schemaorg.models.intangible.ContactPoint import ContactPoint
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Distance import Distance
    from msgspec_schemaorg.models.intangible.GenderType import GenderType
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.InteractionCounter import InteractionCounter
    from msgspec_schemaorg.models.intangible.Language import Language
    from msgspec_schemaorg.models.intangible.Mass import Mass
    from msgspec_schemaorg.models.intangible.MemberProgramTier import MemberProgramTier
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.Occupation import Occupation
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.OfferCatalog import OfferCatalog
    from msgspec_schemaorg.models.intangible.OwnershipInfo import OwnershipInfo
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PriceSpecification import PriceSpecification
    from msgspec_schemaorg.models.intangible.ProgramMembership import ProgramMembership
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.organization.EducationalOrganization import EducationalOrganization
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Country import Country
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Drug import Drug
    from msgspec_schemaorg.models.product.Product import Product
    from msgspec_schemaorg.models.thing.MedicalCondition import MedicalCondition
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import date


class Patient(Struct, frozen=True):
    """A patient is any person recipient of health care services."""
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
    audienceType: str | None = None
    geographicArea: 'AdministrativeArea' | None = None
    suggestedAge: 'QuantitativeValue' | None = None
    suggestedMinAge: int | float | None = None
    suggestedGender: str | 'GenderType' | None = None
    requiredMinAge: int | None = None
    suggestedMeasurement: 'QuantitativeValue' | None = None
    healthCondition: 'MedicalCondition' | None = None
    requiredGender: str | None = None
    requiredMaxAge: int | None = None
    suggestedMaxAge: int | float | None = None
    sibling: 'Person' | None = None
    knows: 'Person' | None = None
    isicV4: str | None = None
    nationality: 'Country' | None = None
    honorificPrefix: str | None = None
    siblings: 'Person' | None = None
    colleague: str | 'Person' | None = None
    hasCertification: 'Certification' | None = None
    parent: 'Person' | None = None
    skills: str | 'DefinedTerm' | None = None
    publishingPrinciples: str | 'CreativeWork' | None = None
    birthPlace: 'Place' | None = None
    hasPOS: 'Place' | None = None
    knowsAbout: 'Thing' | str | str | None = None
    telephone: str | None = None
    weight: 'QuantitativeValue' | 'Mass' | None = None
    seeks: 'Demand' | None = None
    additionalName: str | None = None
    hasCredential: 'EducationalOccupationalCredential' | None = None
    deathDate: date | None = None
    jobTitle: str | 'DefinedTerm' | None = None
    vatID: str | None = None
    taxID: str | None = None
    colleagues: 'Person' | None = None
    funding: 'Grant' | None = None
    givenName: str | None = None
    relatedTo: 'Person' | None = None
    birthDate: date | None = None
    homeLocation: 'ContactPoint' | 'Place' | None = None
    alumniOf: 'Organization' | 'EducationalOrganization' | None = None
    contactPoints: 'ContactPoint' | None = None
    naics: str | None = None
    owns: 'Product' | 'OwnershipInfo' | None = None
    callSign: str | None = None
    award: str | None = None
    brand: 'Brand' | 'Organization' | None = None
    children: 'Person' | None = None
    knowsLanguage: str | 'Language' | None = None
    awards: str | None = None
    affiliation: 'Organization' | None = None
    parents: 'Person' | None = None
    spouse: 'Person' | None = None
    agentInteractionStatistic: 'InteractionCounter' | None = None
    funder: 'Person' | 'Organization' | None = None
    address: 'PostalAddress' | str | None = None
    netWorth: 'MonetaryAmount' | 'PriceSpecification' | None = None
    interactionStatistic: 'InteractionCounter' | None = None
    globalLocationNumber: str | None = None
    hasOccupation: 'Occupation' | None = None
    deathPlace: 'Place' | None = None
    makesOffer: 'Offer' | None = None
    sponsor: 'Organization' | 'Person' | None = None
    memberOf: 'Organization' | 'ProgramMembership' | 'MemberProgramTier' | None = None
    hasOfferCatalog: 'OfferCatalog' | None = None
    height: 'Distance' | 'QuantitativeValue' | None = None
    duns: str | None = None
    familyName: str | None = None
    worksFor: 'Organization' | None = None
    follows: 'Person' | None = None
    faxNumber: str | None = None
    contactPoint: 'ContactPoint' | None = None
    honorificSuffix: str | None = None
    performerIn: 'Event' | None = None
    email: str | None = None
    workLocation: 'Place' | 'ContactPoint' | None = None
    gender: str | 'GenderType' | None = None
    drug: 'Drug' | None = None
    diagnosis: 'MedicalCondition' | None = None