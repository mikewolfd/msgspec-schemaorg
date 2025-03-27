from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.EducationalOccupationalCredential import EducationalOccupationalCredential
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.ContactPoint import ContactPoint
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.MonetaryAmountDistribution import MonetaryAmountDistribution
    from msgspec_schemaorg.models.intangible.Occupation import Occupation
    from msgspec_schemaorg.models.intangible.OccupationalExperienceRequirements import OccupationalExperienceRequirements
    from msgspec_schemaorg.models.intangible.PriceSpecification import PriceSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.place.Place import Place
from datetime import date, datetime


class JobPosting(Struct, frozen=True):
    """A listing that describes a job opening in a certain organization."""
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
    physicalRequirement: str | 'DefinedTerm' | str | None = None
    applicationContact: 'ContactPoint' | None = None
    responsibilities: str | None = None
    educationRequirements: str | 'EducationalOccupationalCredential' | None = None
    benefits: str | None = None
    skills: str | 'DefinedTerm' | None = None
    employmentType: str | None = None
    experienceInPlaceOfEducation: bool | None = None
    workHours: str | None = None
    datePosted: datetime | date | None = None
    applicantLocationRequirements: 'AdministrativeArea' | None = None
    securityClearanceRequirement: str | str | None = None
    occupationalCategory: 'CategoryCode' | str | None = None
    employmentUnit: 'Organization' | None = None
    jobImmediateStart: bool | None = None
    directApply: bool | None = None
    jobStartDate: str | date | None = None
    qualifications: 'EducationalOccupationalCredential' | str | None = None
    specialCommitments: str | None = None
    incentiveCompensation: str | None = None
    baseSalary: 'PriceSpecification' | int | float | 'MonetaryAmount' | None = None
    jobBenefits: str | None = None
    validThrough: date | datetime | None = None
    estimatedSalary: 'MonetaryAmountDistribution' | int | float | 'MonetaryAmount' | None = None
    totalJobOpenings: int | None = None
    hiringOrganization: 'Organization' | 'Person' | None = None
    relevantOccupation: 'Occupation' | None = None
    experienceRequirements: 'OccupationalExperienceRequirements' | str | None = None
    jobLocationType: str | None = None
    eligibilityToWorkRequirement: str | None = None
    jobLocation: 'Place' | None = None
    sensoryRequirement: 'DefinedTerm' | str | str | None = None
    employerOverview: str | None = None
    incentives: str | None = None
    title: str | None = None
    industry: str | 'DefinedTerm' | None = None
    salaryCurrency: str | None = None