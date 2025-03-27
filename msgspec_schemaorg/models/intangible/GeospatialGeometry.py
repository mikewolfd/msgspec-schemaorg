from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.GeospatialGeometry import GeospatialGeometry
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.place.Place import Place


class GeospatialGeometry(Struct, frozen=True):
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices."""
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
    geoIntersects: 'GeospatialGeometry' | 'Place' | None = None
    geoOverlaps: 'Place' | 'GeospatialGeometry' | None = None
    geoCrosses: 'GeospatialGeometry' | 'Place' | None = None
    geoCoveredBy: 'Place' | 'GeospatialGeometry' | None = None
    geoContains: 'Place' | 'GeospatialGeometry' | None = None
    geoTouches: 'GeospatialGeometry' | 'Place' | None = None
    geoWithin: 'GeospatialGeometry' | 'Place' | None = None
    geoDisjoint: 'Place' | 'GeospatialGeometry' | None = None
    geoCovers: 'Place' | 'GeospatialGeometry' | None = None
    geoEquals: 'GeospatialGeometry' | 'Place' | None = None