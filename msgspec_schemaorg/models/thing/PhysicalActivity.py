from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.MedicalCode import MedicalCode
    from msgspec_schemaorg.models.intangible.MedicalEnumeration import MedicalEnumeration
    from msgspec_schemaorg.models.intangible.MedicalSpecialty import MedicalSpecialty
    from msgspec_schemaorg.models.intangible.MedicineSystem import MedicineSystem
    from msgspec_schemaorg.models.intangible.PhysicalActivityCategory import PhysicalActivityCategory
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.thing.AnatomicalStructure import AnatomicalStructure
    from msgspec_schemaorg.models.thing.AnatomicalSystem import AnatomicalSystem
    from msgspec_schemaorg.models.thing.DrugLegalStatus import DrugLegalStatus
    from msgspec_schemaorg.models.thing.MedicalGuideline import MedicalGuideline
    from msgspec_schemaorg.models.thing.MedicalStudy import MedicalStudy
    from msgspec_schemaorg.models.thing.SuperficialAnatomy import SuperficialAnatomy
    from msgspec_schemaorg.models.thing.Thing import Thing


class PhysicalActivity(Struct, frozen=True):
    """Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan."""
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
    legalStatus: str | 'DrugLegalStatus' | 'MedicalEnumeration' | None = None
    relevantSpecialty: 'MedicalSpecialty' | None = None
    funding: 'Grant' | None = None
    recognizingAuthority: 'Organization' | None = None
    medicineSystem: 'MedicineSystem' | None = None
    guideline: 'MedicalGuideline' | None = None
    study: 'MedicalStudy' | None = None
    code: 'MedicalCode' | None = None
    associatedAnatomy: 'SuperficialAnatomy' | 'AnatomicalStructure' | 'AnatomicalSystem' | None = None
    category: 'CategoryCode' | str | 'Thing' | 'PhysicalActivityCategory' | str | None = None
    epidemiology: str | None = None
    pathophysiology: str | None = None