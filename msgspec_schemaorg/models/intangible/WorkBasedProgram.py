from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.Course import Course
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.EducationalOccupationalCredential import EducationalOccupationalCredential
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.AlignmentObject import AlignmentObject
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.DayOfWeek import DayOfWeek
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.MonetaryAmountDistribution import MonetaryAmountDistribution
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.StructuredValue import StructuredValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
from datetime import date, datetime


class WorkBasedProgram(Struct, frozen=True):
    """A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs."""
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
    endDate: datetime | date | None = None
    educationalCredentialAwarded: 'EducationalOccupationalCredential' | str | str | None = None
    trainingSalary: 'MonetaryAmountDistribution' | None = None
    salaryUponCompletion: 'MonetaryAmountDistribution' | None = None
    programPrerequisites: 'EducationalOccupationalCredential' | 'AlignmentObject' | str | 'Course' | None = None
    offers: 'Offer' | 'Demand' | None = None
    occupationalCategory: 'CategoryCode' | str | None = None
    programType: str | 'DefinedTerm' | None = None
    timeToComplete: 'Duration' | None = None
    numberOfCredits: 'StructuredValue' | int | None = None
    timeOfDay: str | None = None
    termsPerYear: int | float | None = None
    financialAidEligible: str | 'DefinedTerm' | None = None
    startDate: date | datetime | None = None
    dayOfWeek: 'DayOfWeek' | None = None
    occupationalCredentialAwarded: 'EducationalOccupationalCredential' | str | str | None = None
    educationalProgramMode: str | str | None = None
    hasCourse: 'Course' | None = None
    typicalCreditsPerTerm: 'StructuredValue' | int | None = None
    applicationStartDate: date | None = None
    maximumEnrollment: int | None = None
    applicationDeadline: str | date | None = None
    termDuration: 'Duration' | None = None