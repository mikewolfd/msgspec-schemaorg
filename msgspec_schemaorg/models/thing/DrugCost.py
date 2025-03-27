from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.DrugCostCategory import DrugCostCategory
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.MedicalCode import MedicalCode
    from msgspec_schemaorg.models.intangible.MedicalEnumeration import MedicalEnumeration
    from msgspec_schemaorg.models.intangible.MedicalSpecialty import MedicalSpecialty
    from msgspec_schemaorg.models.intangible.MedicineSystem import MedicineSystem
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QualitativeValue import QualitativeValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.place.AdministrativeArea import AdministrativeArea
    from msgspec_schemaorg.models.thing.DrugLegalStatus import DrugLegalStatus
    from msgspec_schemaorg.models.thing.MedicalGuideline import MedicalGuideline
    from msgspec_schemaorg.models.thing.MedicalStudy import MedicalStudy


class DrugCost(Struct, frozen=True):
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema's markup."""
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
    drugUnit: str | None = None
    costCategory: 'DrugCostCategory' | None = None
    costOrigin: str | None = None
    applicableLocation: 'AdministrativeArea' | None = None
    costCurrency: str | None = None
    costPerUnit: 'QualitativeValue' | int | float | str | None = None