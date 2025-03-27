from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.Review import Review
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.AggregateRating import AggregateRating
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.EventAttendanceModeEnumeration import EventAttendanceModeEnumeration
    from msgspec_schemaorg.models.intangible.EventStatusType import EventStatusType
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.Language import Language
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.Schedule import Schedule
    from msgspec_schemaorg.models.intangible.VirtualLocation import VirtualLocation
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.organization.PerformingGroup import PerformingGroup
    from msgspec_schemaorg.models.organization.SportsTeam import SportsTeam
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import date, datetime, time


class SportsEvent(Struct, frozen=True):
    """Event type: Sports event."""
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
    doorTime: time | datetime | None = None
    endDate: datetime | date | None = None
    aggregateRating: 'AggregateRating' | None = None
    inLanguage: str | 'Language' | None = None
    eventSchedule: 'Schedule' | None = None
    attendees: 'Person' | 'Organization' | None = None
    eventStatus: 'EventStatusType' | None = None
    maximumPhysicalAttendeeCapacity: int | None = None
    composer: 'Person' | 'Organization' | None = None
    offers: 'Offer' | 'Demand' | None = None
    keywords: 'DefinedTerm' | str | str | None = None
    maximumAttendeeCapacity: int | None = None
    about: 'Thing' | None = None
    location: str | 'Place' | 'VirtualLocation' | 'PostalAddress' | None = None
    remainingAttendeeCapacity: int | None = None
    funding: 'Grant' | None = None
    attendee: 'Person' | 'Organization' | None = None
    workFeatured: 'CreativeWork' | None = None
    performer: 'Person' | 'Organization' | None = None
    subEvents: 'Event' | None = None
    workPerformed: 'CreativeWork' | None = None
    duration: 'QuantitativeValue' | 'Duration' | None = None
    organizer: 'Person' | 'Organization' | None = None
    actor: 'Person' | 'PerformingGroup' | None = None
    performers: 'Person' | 'Organization' | None = None
    startDate: date | datetime | None = None
    subEvent: 'Event' | None = None
    audience: 'Audience' | None = None
    translator: 'Person' | 'Organization' | None = None
    recordedIn: 'CreativeWork' | None = None
    funder: 'Person' | 'Organization' | None = None
    previousStartDate: date | None = None
    contributor: 'Person' | 'Organization' | None = None
    maximumVirtualAttendeeCapacity: int | None = None
    review: 'Review' | None = None
    eventAttendanceMode: 'EventAttendanceModeEnumeration' | None = None
    sponsor: 'Organization' | 'Person' | None = None
    typicalAgeRange: str | None = None
    superEvent: 'Event' | None = None
    isAccessibleForFree: bool | None = None
    director: 'Person' | None = None
    competitor: 'Person' | 'SportsTeam' | None = None
    sport: str | str | None = None
    homeTeam: 'Person' | 'SportsTeam' | None = None
    awayTeam: 'Person' | 'SportsTeam' | None = None