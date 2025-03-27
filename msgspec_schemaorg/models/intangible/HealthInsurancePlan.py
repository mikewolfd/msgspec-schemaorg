from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.ContactPoint import ContactPoint
    from msgspec_schemaorg.models.intangible.HealthPlanFormulary import HealthPlanFormulary
    from msgspec_schemaorg.models.intangible.HealthPlanNetwork import HealthPlanNetwork
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue


class HealthInsurancePlan(Struct, frozen=True):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs."""
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
    includesHealthPlanNetwork: 'HealthPlanNetwork' | None = None
    usesHealthPlanIdStandard: str | str | None = None
    healthPlanDrugOption: str | None = None
    healthPlanId: str | None = None
    benefitsSummaryUrl: str | None = None
    healthPlanMarketingUrl: str | None = None
    healthPlanDrugTier: str | None = None
    includesHealthPlanFormulary: 'HealthPlanFormulary' | None = None
    contactPoint: 'ContactPoint' | None = None