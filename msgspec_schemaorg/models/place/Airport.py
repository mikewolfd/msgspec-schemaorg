from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.Certification import Certification
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.Map import Map
    from msgspec_schemaorg.models.creativework.Photograph import Photograph
    from msgspec_schemaorg.models.creativework.Review import Review
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.AggregateRating import AggregateRating
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.GeoCoordinates import GeoCoordinates
    from msgspec_schemaorg.models.intangible.GeoShape import GeoShape
    from msgspec_schemaorg.models.intangible.GeospatialGeometry import GeospatialGeometry
    from msgspec_schemaorg.models.intangible.LocationFeatureSpecification import LocationFeatureSpecification
    from msgspec_schemaorg.models.intangible.OpeningHoursSpecification import OpeningHoursSpecification
    from msgspec_schemaorg.models.intangible.PostalAddress import PostalAddress
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.place.Place import Place


class Airport(Struct, frozen=True):
    """An airport."""
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
    event: 'Event' | None = None
    isicV4: str | None = None
    photos: 'ImageObject' | 'Photograph' | None = None
    aggregateRating: 'AggregateRating' | None = None
    tourBookingPage: str | None = None
    containedInPlace: 'Place' | None = None
    hasCertification: 'Certification' | None = None
    geoIntersects: 'GeospatialGeometry' | 'Place' | None = None
    containsPlace: 'Place' | None = None
    telephone: str | None = None
    geoOverlaps: 'Place' | 'GeospatialGeometry' | None = None
    hasGS1DigitalLink: str | None = None
    reviews: 'Review' | None = None
    geoCrosses: 'GeospatialGeometry' | 'Place' | None = None
    keywords: 'DefinedTerm' | str | str | None = None
    hasDriveThroughService: bool | None = None
    maximumAttendeeCapacity: int | None = None
    specialOpeningHoursSpecification: 'OpeningHoursSpecification' | None = None
    containedIn: 'Place' | None = None
    geoCoveredBy: 'Place' | 'GeospatialGeometry' | None = None
    maps: str | None = None
    logo: str | 'ImageObject' | None = None
    geoContains: 'Place' | 'GeospatialGeometry' | None = None
    geo: 'GeoCoordinates' | 'GeoShape' | None = None
    publicAccess: bool | None = None
    latitude: int | float | str | None = None
    map: str | None = None
    hasMap: str | 'Map' | None = None
    geoTouches: 'GeospatialGeometry' | 'Place' | None = None
    amenityFeature: 'LocationFeatureSpecification' | None = None
    address: 'PostalAddress' | str | None = None
    additionalProperty: 'PropertyValue' | None = None
    slogan: str | None = None
    review: 'Review' | None = None
    globalLocationNumber: str | None = None
    geoWithin: 'GeospatialGeometry' | 'Place' | None = None
    smokingAllowed: bool | None = None
    longitude: int | float | str | None = None
    geoDisjoint: 'Place' | 'GeospatialGeometry' | None = None
    geoCovers: 'Place' | 'GeospatialGeometry' | None = None
    isAccessibleForFree: bool | None = None
    photo: 'ImageObject' | 'Photograph' | None = None
    faxNumber: str | None = None
    branchCode: str | None = None
    openingHoursSpecification: 'OpeningHoursSpecification' | None = None
    events: 'Event' | None = None
    geoEquals: 'GeospatialGeometry' | 'Place' | None = None
    openingHours: str | None = None
    icaoCode: str | None = None
    iataCode: str | None = None