from __future__ import annotations
from msgspec import Struct, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.CreditCard import CreditCard
    from msgspec_schemaorg.models.intangible.MemberProgram import MemberProgram
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.TierBenefitEnumeration import TierBenefitEnumeration
    from msgspec_schemaorg.models.intangible.UnitPriceSpecification import UnitPriceSpecification


class MemberProgramTier(Struct, frozen=True):
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold"."""
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
    hasTierBenefit: 'TierBenefitEnumeration' | None = None
    hasTierRequirement: str | 'MonetaryAmount' | 'CreditCard' | 'UnitPriceSpecification' | None = None
    membershipPointsEarned: 'QuantitativeValue' | int | float | None = None
    isTierOf: 'MemberProgram' | None = None