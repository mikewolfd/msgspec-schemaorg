from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.GenderType import GenderType
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.thing.MedicalCondition import MedicalCondition


class MedicalAudience(Struct, frozen=True):
    """Target audiences for medical web pages."""
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
    audienceType: str | None = None
    geographicArea: 'AdministrativeArea' | None = None
    suggestedAge: 'QuantitativeValue' | None = None
    suggestedMinAge: int | float | None = None
    suggestedGender: str | 'GenderType' | None = None
    requiredMinAge: int | None = None
    suggestedMeasurement: 'QuantitativeValue' | None = None
    healthCondition: 'MedicalCondition' | None = None
    requiredGender: str | None = None
    requiredMaxAge: int | None = None
    suggestedMaxAge: int | float | None = None