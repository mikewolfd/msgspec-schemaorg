from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.Class import Class
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Enumeration import Enumeration
    from msgspec_schemaorg.models.intangible.MeasurementTypeEnumeration import MeasurementTypeEnumeration
    from msgspec_schemaorg.models.intangible.Property import Property
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QualitativeValue import QualitativeValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.StructuredValue import StructuredValue


class BedType(Struct, frozen=True):
    """A type of bed. This is used for indicating the bed or beds available in an accommodation."""
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
    supersededBy: 'Class' | 'Property' | 'Enumeration' | None = None
    valueReference: str | 'PropertyValue' | 'MeasurementTypeEnumeration' | 'DefinedTerm' | 'QuantitativeValue' | 'Enumeration' | 'StructuredValue' | 'QualitativeValue' | None = None
    lesser: 'QualitativeValue' | None = None
    greater: 'QualitativeValue' | None = None
    equal: 'QualitativeValue' | None = None
    lesserOrEqual: 'QualitativeValue' | None = None
    greaterOrEqual: 'QualitativeValue' | None = None
    additionalProperty: 'PropertyValue' | None = None
    nonEqual: 'QualitativeValue' | None = None