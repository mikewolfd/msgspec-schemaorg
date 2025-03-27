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
    from msgspec_schemaorg.models.intangible.Property import Property
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QualitativeValue import QualitativeValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.StatisticalVariable import StatisticalVariable
    from msgspec_schemaorg.models.intangible.StructuredValue import StructuredValue
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import datetime


class Observation(Struct, frozen=True):
    """Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].
    """
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
    value: 'StructuredValue' | int | float | bool | str | None = None
    additionalProperty: 'PropertyValue' | None = None
    unitCode: str | str | None = None
    minValue: int | float | None = None
    measurementDenominator: 'StatisticalVariable' | None = None
    observationDate: datetime | None = None
    marginOfError: 'QuantitativeValue' | None = None
    measurementQualifier: 'Enumeration' | None = None
    measuredProperty: 'Property' | None = None
    observationAbout: 'Place' | 'Thing' | None = None
    measurementTechnique: str | 'DefinedTerm' | str | 'MeasurementMethodEnum' | None = None
    measurementMethod: 'DefinedTerm' | str | 'MeasurementMethodEnum' | str | None = None
    observationPeriod: str | None = None
    variableMeasured: 'Property' | 'StatisticalVariable' | 'PropertyValue' | str | None = None