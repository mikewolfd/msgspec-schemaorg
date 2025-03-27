from __future__ import annotations
from msgspec import Struct, field
from msgspec_schemaorg.utils import parse_iso8601
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from msgspec_schemaorg.models.action.Action import Action
    from msgspec_schemaorg.models.creativework.AudioObject import AudioObject
    from msgspec_schemaorg.models.creativework.Claim import Claim
    from msgspec_schemaorg.models.creativework.Clip import Clip
    from msgspec_schemaorg.models.creativework.Comment import Comment
    from msgspec_schemaorg.models.creativework.CorrectionComment import CorrectionComment
    from msgspec_schemaorg.models.creativework.CreativeWork import CreativeWork
    from msgspec_schemaorg.models.creativework.ImageObject import ImageObject
    from msgspec_schemaorg.models.creativework.MediaObject import MediaObject
    from msgspec_schemaorg.models.creativework.MusicRecording import MusicRecording
    from msgspec_schemaorg.models.creativework.Review import Review
    from msgspec_schemaorg.models.creativework.TextObject import TextObject
    from msgspec_schemaorg.models.creativework.VideoObject import VideoObject
    from msgspec_schemaorg.models.creativework.WebPage import WebPage
    from msgspec_schemaorg.models.event.Event import Event
    from msgspec_schemaorg.models.event.PublicationEvent import PublicationEvent
    from msgspec_schemaorg.models.intangible.AggregateRating import AggregateRating
    from msgspec_schemaorg.models.intangible.AlignmentObject import AlignmentObject
    from msgspec_schemaorg.models.intangible.Audience import Audience
    from msgspec_schemaorg.models.intangible.DefinedTerm import DefinedTerm
    from msgspec_schemaorg.models.intangible.Demand import Demand
    from msgspec_schemaorg.models.intangible.Duration import Duration
    from msgspec_schemaorg.models.intangible.Grant import Grant
    from msgspec_schemaorg.models.intangible.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration
    from msgspec_schemaorg.models.intangible.InteractionCounter import InteractionCounter
    from msgspec_schemaorg.models.intangible.ItemList import ItemList
    from msgspec_schemaorg.models.intangible.Language import Language
    from msgspec_schemaorg.models.intangible.Offer import Offer
    from msgspec_schemaorg.models.intangible.PropertyValue import PropertyValue
    from msgspec_schemaorg.models.intangible.QuantitativeValue import QuantitativeValue
    from msgspec_schemaorg.models.intangible.Rating import Rating
    from msgspec_schemaorg.models.intangible.SizeSpecification import SizeSpecification
    from msgspec_schemaorg.models.organization.MusicGroup import MusicGroup
    from msgspec_schemaorg.models.organization.Organization import Organization
    from msgspec_schemaorg.models.organization.PerformingGroup import PerformingGroup
    from msgspec_schemaorg.models.person.Person import Person
    from msgspec_schemaorg.models.place.Country import Country
    from msgspec_schemaorg.models.place.Place import Place
    from msgspec_schemaorg.models.product.Product import Product
    from msgspec_schemaorg.models.thing.Thing import Thing
from datetime import date, datetime


class MovieSeries(Struct, frozen=True):
    """A series of movies. Included movies can be indicated with the hasPart property."""
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
    provider: 'Person' | 'Organization' | None = None
    aggregateRating: 'AggregateRating' | None = None
    citation: str | 'CreativeWork' | None = None
    locationCreated: 'Place' | None = None
    sdPublisher: 'Person' | 'Organization' | None = None
    thumbnail: 'ImageObject' | None = None
    accessModeSufficient: 'ItemList' | None = None
    publishingPrinciples: str | 'CreativeWork' | None = None
    inLanguage: str | 'Language' | None = None
    abstract: str | None = None
    countryOfOrigin: 'Country' | None = None
    contentLocation: 'Place' | None = None
    dateModified: datetime | date | None = None
    usageInfo: str | 'CreativeWork' | None = None
    sdDatePublished: date | None = None
    archivedAt: str | 'WebPage' | None = None
    workTranslation: 'CreativeWork' | None = None
    sdLicense: str | 'CreativeWork' | None = None
    educationalAlignment: 'AlignmentObject' | None = None
    editor: 'Person' | None = None
    license: str | 'CreativeWork' | None = None
    maintainer: 'Person' | 'Organization' | None = None
    sourceOrganization: 'Organization' | None = None
    reviews: 'Review' | None = None
    accessibilityHazard: str | None = None
    workExample: 'CreativeWork' | None = None
    pattern: 'DefinedTerm' | str | None = None
    offers: 'Offer' | 'Demand' | None = None
    hasPart: 'CreativeWork' | None = None
    keywords: 'DefinedTerm' | str | str | None = None
    exampleOfWork: 'CreativeWork' | None = None
    copyrightNotice: str | None = None
    encodingFormat: str | str | None = None
    mainEntity: 'Thing' | None = None
    editEIDR: str | str | None = None
    copyrightYear: int | float | None = None
    about: 'Thing' | None = None
    datePublished: date | datetime | None = None
    educationalLevel: str | 'DefinedTerm' | str | None = None
    accessibilityFeature: str | None = None
    materialExtent: str | 'QuantitativeValue' | None = None
    video: 'Clip' | 'VideoObject' | None = None
    funding: 'Grant' | None = None
    headline: str | None = None
    digitalSourceType: 'IPTCDigitalSourceEnumeration' | None = None
    learningResourceType: 'DefinedTerm' | str | None = None
    alternativeHeadline: str | None = None
    temporal: datetime | str | None = None
    isBasedOnUrl: str | 'CreativeWork' | 'Product' | None = None
    associatedMedia: 'MediaObject' | None = None
    commentCount: int | None = None
    dateCreated: date | datetime | None = None
    fileFormat: str | str | None = None
    teaches: 'DefinedTerm' | str | None = None
    accessibilityControl: str | None = None
    isPartOf: str | 'CreativeWork' | None = None
    accessibilityAPI: str | None = None
    contentReferenceTime: datetime | None = None
    isBasedOn: str | 'CreativeWork' | 'Product' | None = None
    creativeWorkStatus: 'DefinedTerm' | str | None = None
    award: str | None = None
    educationalUse: str | 'DefinedTerm' | None = None
    isFamilyFriendly: bool | None = None
    interactivityType: str | None = None
    publication: 'PublicationEvent' | None = None
    accountablePerson: 'Person' | None = None
    version: int | float | str | None = None
    expires: datetime | date | None = None
    awards: str | None = None
    text: str | None = None
    producer: 'Person' | 'Organization' | None = None
    thumbnailUrl: str | None = None
    copyrightHolder: 'Person' | 'Organization' | None = None
    wordCount: int | None = None
    recordedAt: 'Event' | None = None
    audience: 'Audience' | None = None
    spatial: 'Place' | None = None
    interpretedAsClaim: 'Claim' | None = None
    creditText: str | None = None
    material: 'Product' | str | str | None = None
    translator: 'Person' | 'Organization' | None = None
    character: 'Person' | None = None
    funder: 'Person' | 'Organization' | None = None
    encodings: 'MediaObject' | None = None
    contributor: 'Person' | 'Organization' | None = None
    position: int | str | None = None
    conditionsOfAccess: str | None = None
    review: 'Review' | None = None
    temporalCoverage: str | str | datetime | None = None
    mentions: 'Thing' | None = None
    interactionStatistic: 'InteractionCounter' | None = None
    schemaVersion: str | str | None = None
    acquireLicensePage: str | 'CreativeWork' | None = None
    sponsor: 'Organization' | 'Person' | None = None
    publisher: 'Organization' | 'Person' | None = None
    assesses: str | 'DefinedTerm' | None = None
    spatialCoverage: 'Place' | None = None
    size: 'QuantitativeValue' | 'DefinedTerm' | 'SizeSpecification' | str | None = None
    contentRating: str | 'Rating' | None = None
    accessMode: str | None = None
    creator: 'Person' | 'Organization' | None = None
    releasedEvent: 'PublicationEvent' | None = None
    accessibilitySummary: str | None = None
    translationOfWork: 'CreativeWork' | None = None
    publisherImprint: 'Organization' | None = None
    typicalAgeRange: str | None = None
    comment: 'Comment' | None = None
    encoding: 'MediaObject' | None = None
    discussionUrl: str | None = None
    timeRequired: 'Duration' | None = None
    isAccessibleForFree: bool | None = None
    audio: 'AudioObject' | 'MusicRecording' | 'Clip' | None = None
    correction: 'CorrectionComment' | str | str | None = None
    author: 'Person' | 'Organization' | None = None
    genre: str | str | None = None
    endDate: datetime | date | None = None
    startDate: date | datetime | None = None
    issn: str | None = None
    actors: 'Person' | None = None
    trailer: 'VideoObject' | None = None
    musicBy: 'Person' | 'MusicGroup' | None = None
    actor: 'Person' | 'PerformingGroup' | None = None
    directors: 'Person' | None = None
    productionCompany: 'Organization' | None = None
    director: 'Person' | None = None