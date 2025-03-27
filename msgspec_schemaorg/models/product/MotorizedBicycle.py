from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.Certification import Certification
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.Review import Review
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.creativework.WebContent import WebContent
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.intangible.AdultOrientedEnumeration import AdultOrientedEnumeration
    from msgspec_schemaorg.models.intangible.AggregateRating import AggregateRating
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.Brand import Brand
    from msgspec_schemaorg.models.intangible.CarUsageType import CarUsageType
    from msgspec_schemaorg.models.intangible.CategoryCode import CategoryCode
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Distance import Distance
    from msgspec_schemaorg.models.intangible.DriveWheelConfigurationValue import DriveWheelConfigurationValue
    from msgspec_schemaorg.models.intangible.EnergyConsumptionDetails import EnergyConsumptionDetails
    from msgspec_schemaorg.models.intangible.EngineSpecification import EngineSpecification
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.ItemList import ItemList
    from msgspec_schemaorg.models.intangible.ListItem import ListItem
    from msgspec_schemaorg.models.intangible.Mass import Mass
    from msgspec_schemaorg.models.intangible.MerchantReturnPolicy import MerchantReturnPolicy
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.OfferItemCondition import OfferItemCondition
    from msgspec_schemaorg.models.intangible.PhysicalActivityCategory import PhysicalActivityCategory
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QualitativeValue import QualitativeValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.Service import Service
    from msgspec_schemaorg.models.intangible.SizeSpecification import SizeSpecification
    from msgspec_schemaorg.models.intangible.SteeringPositionValue import SteeringPositionValue
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.place.Country import Country
    from msgspec_schemaorg.models.product.Product import Product
    from msgspec_schemaorg.models.product.ProductGroup import ProductGroup
    from msgspec_schemaorg.models.product.ProductModel import ProductModel
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import date


class MotorizedBicycle(Struct, frozen=True):
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling."""
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
    productID: str | None = None
    aggregateRating: 'AggregateRating' | None = None
    hasCertification: 'Certification' | None = None
    isSimilarTo: 'Product' | 'Service' | None = None
    colorSwatch: str | 'ImageObject' | None = None
    productionDate: date | None = None
    countryOfAssembly: str | None = None
    countryOfOrigin: 'Country' | None = None
    sku: str | None = None
    hasMerchantReturnPolicy: 'MerchantReturnPolicy' | None = None
    weight: 'QuantitativeValue' | 'Mass' | None = None
    mpn: str | None = None
    hasGS1DigitalLink: str | None = None
    model: str | 'ProductModel' | None = None
    isRelatedTo: 'Product' | 'Service' | None = None
    reviews: 'Review' | None = None
    gtin12: str | None = None
    pattern: 'DefinedTerm' | str | None = None
    offers: 'Offer' | 'Demand' | None = None
    keywords: 'DefinedTerm' | str | str | None = None
    negativeNotes: str | 'ListItem' | 'ItemList' | 'WebContent' | None = None
    gtin13: str | None = None
    hasMeasurement: 'QuantitativeValue' | None = None
    gtin: str | str | None = None
    funding: 'Grant' | None = None
    isConsumableFor: 'Product' | None = None
    mobileUrl: str | None = None
    category: 'CategoryCode' | str | 'Thing' | 'PhysicalActivityCategory' | str | None = None
    asin: str | str | None = None
    color: str | None = None
    countryOfLastProcessing: str | None = None
    logo: str | 'ImageObject' | None = None
    award: str | None = None
    isFamilyFriendly: bool | None = None
    releaseDate: date | None = None
    brand: 'Brand' | 'Organization' | None = None
    inProductGroupWithID: str | None = None
    manufacturer: 'Organization' | None = None
    awards: str | None = None
    width: 'Distance' | 'QuantitativeValue' | None = None
    hasAdultConsideration: 'AdultOrientedEnumeration' | None = None
    audience: 'Audience' | None = None
    material: 'Product' | str | str | None = None
    additionalProperty: 'PropertyValue' | None = None
    slogan: str | None = None
    depth: 'QuantitativeValue' | 'Distance' | None = None
    review: 'Review' | None = None
    itemCondition: 'OfferItemCondition' | None = None
    nsn: str | None = None
    positiveNotes: 'WebContent' | str | 'ItemList' | 'ListItem' | None = None
    size: 'QuantitativeValue' | 'DefinedTerm' | 'SizeSpecification' | str | None = None
    hasEnergyConsumptionDetails: 'EnergyConsumptionDetails' | None = None
    gtin14: str | None = None
    height: 'Distance' | 'QuantitativeValue' | None = None
    purchaseDate: date | None = None
    isVariantOf: 'ProductModel' | 'ProductGroup' | None = None
    gtin8: str | None = None
    isAccessoryOrSparePartFor: 'Product' | None = None
    mileageFromOdometer: 'QuantitativeValue' | None = None
    fuelCapacity: 'QuantitativeValue' | None = None
    vehicleTransmission: 'QualitativeValue' | str | str | None = None
    bodyType: 'QualitativeValue' | str | str | None = None
    vehicleInteriorColor: str | None = None
    fuelConsumption: 'QuantitativeValue' | None = None
    vehicleSpecialUsage: 'CarUsageType' | str | None = None
    numberOfForwardGears: int | float | 'QuantitativeValue' | None = None
    fuelEfficiency: 'QuantitativeValue' | None = None
    vehicleModelDate: date | None = None
    vehicleEngine: 'EngineSpecification' | None = None
    numberOfDoors: 'QuantitativeValue' | int | float | None = None
    numberOfPreviousOwners: 'QuantitativeValue' | int | float | None = None
    weightTotal: 'QuantitativeValue' | None = None
    numberOfAxles: int | float | 'QuantitativeValue' | None = None
    payload: 'QuantitativeValue' | None = None
    cargoVolume: 'QuantitativeValue' | None = None
    meetsEmissionStandard: 'QualitativeValue' | str | str | None = None
    wheelbase: 'QuantitativeValue' | None = None
    speed: 'QuantitativeValue' | None = None
    modelDate: date | None = None
    numberOfAirbags: int | float | str | None = None
    accelerationTime: 'QuantitativeValue' | None = None
    callSign: str | None = None
    tongueWeight: 'QuantitativeValue' | None = None
    seatingCapacity: int | float | 'QuantitativeValue' | None = None
    driveWheelConfiguration: 'DriveWheelConfigurationValue' | str | None = None
    fuelType: str | 'QualitativeValue' | str | None = None
    vehicleInteriorType: str | None = None
    vehicleConfiguration: str | None = None
    dateVehicleFirstRegistered: date | None = None
    vehicleIdentificationNumber: str | None = None
    emissionsCO2: int | float | None = None
    knownVehicleDamages: str | None = None
    vehicleSeatingCapacity: 'QuantitativeValue' | int | float | None = None
    trailerWeight: 'QuantitativeValue' | None = None
    steeringPosition: 'SteeringPositionValue' | None = None