from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.EventStatusType import EventStatusType
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.MedicalCode import MedicalCode
    from msgspec_schemaorg.models.intangible.MedicalEnumeration import MedicalEnumeration
    from msgspec_schemaorg.models.intangible.MedicalSpecialty import MedicalSpecialty
    from msgspec_schemaorg.models.intangible.MedicalStudyStatus import MedicalStudyStatus
    from msgspec_schemaorg.models.intangible.MedicineSystem import MedicineSystem
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.product.Drug import Drug
    from msgspec_schemaorg.models.thing.AnatomicalStructure import AnatomicalStructure
    from msgspec_schemaorg.models.thing.AnatomicalSystem import AnatomicalSystem
    from msgspec_schemaorg.models.thing.DDxElement import DDxElement
    from msgspec_schemaorg.models.thing.DrugLegalStatus import DrugLegalStatus
    from msgspec_schemaorg.models.thing.MedicalConditionStage import MedicalConditionStage
    from msgspec_schemaorg.models.thing.MedicalGuideline import MedicalGuideline
    from msgspec_schemaorg.models.thing.MedicalRiskFactor import MedicalRiskFactor
    from msgspec_schemaorg.models.thing.MedicalSignOrSymptom import MedicalSignOrSymptom
    from msgspec_schemaorg.models.thing.MedicalStudy import MedicalStudy
    from msgspec_schemaorg.models.thing.MedicalTest import MedicalTest
    from msgspec_schemaorg.models.thing.MedicalTherapy import MedicalTherapy
    from msgspec_schemaorg.models.thing.SuperficialAnatomy import SuperficialAnatomy


class MedicalCondition(Struct, frozen=True):
    """Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc."""
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
    expectedPrognosis: str | None = None
    associatedAnatomy: 'SuperficialAnatomy' | 'AnatomicalStructure' | 'AnatomicalSystem' | None = None
    possibleComplication: str | None = None
    signOrSymptom: 'MedicalSignOrSymptom' | None = None
    primaryPrevention: 'MedicalTherapy' | None = None
    riskFactor: 'MedicalRiskFactor' | None = None
    secondaryPrevention: 'MedicalTherapy' | None = None
    possibleTreatment: 'MedicalTherapy' | None = None
    drug: 'Drug' | None = None
    naturalProgression: str | None = None
    status: 'EventStatusType' | str | 'MedicalStudyStatus' | None = None
    differentialDiagnosis: 'DDxElement' | None = None
    epidemiology: str | None = None
    stage: 'MedicalConditionStage' | None = None
    typicalTest: 'MedicalTest' | None = None
    pathophysiology: str | None = None