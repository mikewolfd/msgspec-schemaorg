from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.Diet import Diet
    from msgspec_schemaorg.models.creativework.ExercisePlan import ExercisePlan
    from msgspec_schemaorg.models.creativework.HowTo import HowTo
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.event.SportsEvent import SportsEvent
    from msgspec_schemaorg.models.intangible.ActionStatusType import ActionStatusType
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.Distance import Distance
    from msgspec_schemaorg.models.intangible.EntryPoint import EntryPoint
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.VirtualLocation import VirtualLocation
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.organization.SportsActivityLocation import SportsActivityLocation
    from msgspec_schemaorg.models.organization.SportsTeam import SportsTeam
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import datetime, time


class ExerciseAction(Struct, frozen=True):
    """The act of participating in exertive activity for the purposes of improving health and fitness."""
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
    actionProcess: 'HowTo' | None = None
    startTime: time | datetime | None = None
    actionStatus: 'ActionStatusType' | None = None
    object: 'Thing' | None = None
    error: 'Thing' | None = None
    location: str | 'Place' | 'VirtualLocation' | 'PostalAddress' | None = None
    agent: 'Person' | 'Organization' | None = None
    result: 'Thing' | None = None
    target: 'EntryPoint' | str | None = None
    endTime: time | datetime | None = None
    instrument: 'Thing' | None = None
    participant: 'Person' | 'Organization' | None = None
    event: 'Event' | None = None
    audience: 'Audience' | None = None
    opponent: 'Person' | None = None
    sportsTeam: 'SportsTeam' | None = None
    distance: 'Distance' | None = None
    sportsEvent: 'SportsEvent' | None = None
    sportsActivityLocation: 'SportsActivityLocation' | None = None
    fromLocation: 'Place' | None = None
    exercisePlan: 'ExercisePlan' | None = None
    course: 'Place' | None = None
    exerciseRelatedDiet: 'Diet' | None = None
    diet: 'Diet' | None = None
    exerciseType: str | None = None
    exerciseCourse: 'Place' | None = None
    toLocation: 'Place' | None = None