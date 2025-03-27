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
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Enumeration import Enumeration
    from msgspec_schemaorg.models.intangible.MeasurementMethodEnum import MeasurementMethodEnum
    from msgspec_schemaorg.models.intangible.MeasurementTypeEnumeration import MeasurementTypeEnumeration
    from msgspec_schemaorg.models.intangible.OpeningHoursSpecification import OpeningHoursSpecification
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QualitativeValue import QualitativeValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.StructuredValue import StructuredValue
from datetime import date, datetime


class LocationFeatureSpecification(Struct, frozen=True):
    """Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality."""
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
    maxValue: int | float | None = None
    valueReference: str | 'PropertyValue' | 'MeasurementTypeEnumeration' | 'DefinedTerm' | 'QuantitativeValue' | 'Enumeration' | 'StructuredValue' | 'QualitativeValue' | None = None
    unitText: str | None = None
    propertyID: str | str | None = None
    value: 'StructuredValue' | int | float | bool | str | None = None
    measurementTechnique: str | 'DefinedTerm' | str | 'MeasurementMethodEnum' | None = None
    measurementMethod: 'DefinedTerm' | str | 'MeasurementMethodEnum' | str | None = None
    unitCode: str | str | None = None
    minValue: int | float | None = None
    hoursAvailable: 'OpeningHoursSpecification' | None = None
    validFrom: datetime | date | None = None
    validThrough: date | datetime | None = None