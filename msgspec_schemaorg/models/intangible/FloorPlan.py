from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.LocationFeatureSpecification import LocationFeatureSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.place.Accommodation import Accommodation


class FloorPlan(Struct, frozen=True):
    """A FloorPlan is an explicit representation of a collection of similar accommodations, allowing the provision of common information (room counts, sizes, layout diagrams) and offers for rental or sale. In typical use, some [[ApartmentComplex]] has an [[accommodationFloorPlan]] which is a [[FloorPlan]].  A FloorPlan is always in the context of a particular place, either a larger [[ApartmentComplex]] or a single [[Apartment]]. The visual/spatial aspects of a floor plan (i.e. room layout, [see wikipedia](https://en.wikipedia.org/wiki/Floor_plan)) can be indicated using [[image]]. """
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
    petsAllowed: bool | str | None = None
    numberOfBathroomsTotal: int | None = None
    floorSize: 'QuantitativeValue' | None = None
    numberOfBedrooms: int | float | 'QuantitativeValue' | None = None
    numberOfFullBathrooms: int | float | None = None
    numberOfAccommodationUnits: 'QuantitativeValue' | None = None
    numberOfAvailableAccommodationUnits: 'QuantitativeValue' | None = None
    numberOfPartialBathrooms: int | float | None = None
    isPlanForApartment: 'Accommodation' | None = None
    numberOfRooms: 'QuantitativeValue' | int | float | None = None
    amenityFeature: 'LocationFeatureSpecification' | None = None
    layoutImage: 'ImageObject' | str | None = None