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
    from msgspec_schemaorg.models.intangible.BoardingPolicyType import BoardingPolicyType
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Distance import Distance
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.ItemList import ItemList
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.Trip import Trip
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.Airport import Airport
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Vehicle import Vehicle
from datetime import datetime, time


class Flight(Struct, frozen=True):
    """An airline flight."""
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
    tripOrigin: 'Place' | None = None
    departureTime: time | datetime | None = None
    partOfTrip: 'Trip' | None = None
    offers: 'Offer' | 'Demand' | None = None
    itinerary: 'ItemList' | 'Place' | None = None
    arrivalTime: time | datetime | None = None
    subTrip: 'Trip' | None = None
    departureAirport: 'Airport' | None = None
    flightDistance: 'Distance' | str | None = None
    estimatedFlightDuration: 'Duration' | str | None = None
    mealService: str | None = None
    arrivalGate: str | None = None
    webCheckinTime: datetime | None = None
    seller: 'Person' | 'Organization' | None = None
    departureTerminal: str | None = None
    flightNumber: str | None = None
    departureGate: str | None = None
    arrivalTerminal: str | None = None
    arrivalAirport: 'Airport' | None = None
    carrier: 'Organization' | None = None
    aircraft: str | 'Vehicle' | None = None
    boardingPolicy: 'BoardingPolicyType' | None = None