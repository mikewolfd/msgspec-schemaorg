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
    from msgspec_schemaorg.models.intangible.MemberProgramTier import MemberProgramTier
    from msgspec_schemaorg.models.intangible.MerchantReturnEnumeration import MerchantReturnEnumeration
    from msgspec_schemaorg.models.intangible.MerchantReturnPolicySeasonalOverride import MerchantReturnPolicySeasonalOverride
    from msgspec_schemaorg.models.intangible.MonetaryAmount import MonetaryAmount
    from msgspec_schemaorg.models.intangible.OfferItemCondition import OfferItemCondition
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.RefundTypeEnumeration import RefundTypeEnumeration
    from msgspec_schemaorg.models.intangible.ReturnFeesEnumeration import ReturnFeesEnumeration
    from msgspec_schemaorg.models.intangible.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration
    from msgspec_schemaorg.models.intangible.ReturnMethodEnumeration import ReturnMethodEnumeration
    from msgspec_schemaorg.models.place.Country import Country
from datetime import date, datetime


class MerchantReturnPolicy(Struct, frozen=True):
    """A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]]."""
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
    itemDefectReturnLabelSource: 'ReturnLabelSourceEnumeration' | None = None
    returnPolicyCountry: str | 'Country' | None = None
    customerRemorseReturnLabelSource: 'ReturnLabelSourceEnumeration' | None = None
    validForMemberTier: 'MemberProgramTier' | None = None
    returnShippingFeesAmount: 'MonetaryAmount' | None = None
    customerRemorseReturnShippingFeesAmount: 'MonetaryAmount' | None = None
    returnFees: 'ReturnFeesEnumeration' | None = None
    inStoreReturnsOffered: bool | None = None
    returnLabelSource: 'ReturnLabelSourceEnumeration' | None = None
    merchantReturnDays: date | int | datetime | None = None
    returnMethod: 'ReturnMethodEnumeration' | None = None
    customerRemorseReturnFees: 'ReturnFeesEnumeration' | None = None
    returnPolicyCategory: 'MerchantReturnEnumeration' | None = None
    merchantReturnLink: str | None = None
    itemDefectReturnFees: 'ReturnFeesEnumeration' | None = None
    additionalProperty: 'PropertyValue' | None = None
    itemCondition: 'OfferItemCondition' | None = None
    itemDefectReturnShippingFeesAmount: 'MonetaryAmount' | None = None
    returnPolicySeasonalOverride: 'MerchantReturnPolicySeasonalOverride' | None = None
    refundType: 'RefundTypeEnumeration' | None = None
    applicableCountry: 'Country' | str | None = None
    restockingFee: 'MonetaryAmount' | int | float | None = None