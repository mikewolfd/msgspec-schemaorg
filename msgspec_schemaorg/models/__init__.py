"""Generated Schema.org models using msgspec."""

from . import action
from . import creativework
from . import event
from . import intangible
from . import misc
from . import organization
from . import person
from . import place
from . import product
from . import thing

# Import all classes directly
from .action import *
from .creativework import *
from .event import *
from .intangible import *
from .misc import *
from .organization import *
from .person import *
from .place import *
from .product import *
from .thing import *

__all__ = [
    'action',
    'creativework',
    'event',
    'intangible',
    'misc',
    'organization',
    'person',
    'place',
    'product',
    'thing',
    'Model3DModel',
    'AMRadioChannel',
    'APIReference',
    'AboutPage',
    'AcceptAction',
    'Accommodation',
    'AccountingService',
    'AchieveAction',
    'Action',
    'ActionAccessSpecification',
    'ActionStatusType',
    'ActivateAction',
    'AddAction',
    'AdministrativeArea',
    'AdultEntertainment',
    'AdultOrientedEnumeration',
    'AdvertiserContentArticle',
    'AggregateOffer',
    'AggregateRating',
    'AgreeAction',
    'Airline',
    'Airport',
    'AlignmentObject',
    'AllocateAction',
    'AmpStory',
    'AmusementPark',
    'AnalysisNewsArticle',
    'AnatomicalStructure',
    'AnatomicalSystem',
    'AnimalShelter',
    'Answer',
    'Apartment',
    'ApartmentComplex',
    'AppendAction',
    'ApplyAction',
    'ApprovedIndication',
    'Aquarium',
    'ArchiveComponent',
    'ArchiveOrganization',
    'ArriveAction',
    'ArtGallery',
    'Artery',
    'Article',
    'AskAction',
    'AskPublicNewsArticle',
    'AssessAction',
    'AssignAction',
    'Atlas',
    'Attorney',
    'Audience',
    'AudioObject',
    'AudioObjectSnapshot',
    'Audiobook',
    'AuthorizeAction',
    'AutoBodyShop',
    'AutoDealer',
    'AutoPartsStore',
    'AutoRental',
    'AutoRepair',
    'AutoWash',
    'AutomatedTeller',
    'AutomotiveBusiness',
    'BackgroundNewsArticle',
    'Bakery',
    'BankAccount',
    'BankOrCreditUnion',
    'BarOrPub',
    'Barcode',
    'Beach',
    'BeautySalon',
    'BedAndBreakfast',
    'BedDetails',
    'BedType',
    'BefriendAction',
    'BikeStore',
    'BioChemEntity',
    'Blog',
    'BlogPosting',
    'BloodTest',
    'BoardingPolicyType',
    'BoatReservation',
    'BoatTerminal',
    'BoatTrip',
    'BodyMeasurementTypeEnumeration',
    'BodyOfWater',
    'Bone',
    'Book',
    'BookFormatType',
    'BookSeries',
    'BookStore',
    'BookmarkAction',
    'BorrowAction',
    'BowlingAlley',
    'BrainStructure',
    'Brand',
    'BreadcrumbList',
    'Brewery',
    'Bridge',
    'BroadcastChannel',
    'BroadcastEvent',
    'BroadcastFrequencySpecification',
    'BroadcastService',
    'BrokerageAccount',
    'BuddhistTemple',
    'BusOrCoach',
    'BusReservation',
    'BusStation',
    'BusStop',
    'BusTrip',
    'BusinessAudience',
    'BusinessEntityType',
    'BusinessEvent',
    'BusinessFunction',
    'BuyAction',
    'CDCPMDRecord',
    'CableOrSatelliteService',
    'CafeOrCoffeeShop',
    'Campground',
    'CampingPitch',
    'Canal',
    'CancelAction',
    'Car',
    'CarUsageType',
    'Casino',
    'CategoryCode',
    'CategoryCodeSet',
    'CatholicChurch',
    'Cemetery',
    'Certification',
    'CertificationStatusEnumeration',
    'Chapter',
    'CheckAction',
    'CheckInAction',
    'CheckOutAction',
    'CheckoutPage',
    'ChemicalSubstance',
    'ChildCare',
    'ChildrensEvent',
    'ChooseAction',
    'Church',
    'City',
    'CityHall',
    'CivicStructure',
    'Claim',
    'ClaimReview',
    'Class',
    'Clip',
    'ClothingStore',
    'Code',
    'Collection',
    'CollectionPage',
    'CollegeOrUniversity',
    'ComedyClub',
    'ComedyEvent',
    'ComicCoverArt',
    'ComicIssue',
    'ComicSeries',
    'ComicStory',
    'Comment',
    'CommentAction',
    'CommunicateAction',
    'CompleteDataFeed',
    'CompoundPriceSpecification',
    'ComputerLanguage',
    'ComputerStore',
    'ConfirmAction',
    'Consortium',
    'ConstraintNode',
    'ConsumeAction',
    'ContactPage',
    'ContactPoint',
    'ContactPointOption',
    'Continent',
    'ControlAction',
    'ConvenienceStore',
    'Conversation',
    'CookAction',
    'Corporation',
    'CorrectionComment',
    'Country',
    'Course',
    'CourseInstance',
    'Courthouse',
    'CoverArt',
    'CovidTestingFacility',
    'CreateAction',
    'CreativeWork',
    'CreativeWorkSeason',
    'CreativeWorkSeries',
    'CreditCard',
    'Crematorium',
    'CriticReview',
    'CssSelectorType',
    'CurrencyConversionService',
    'DDxElement',
    'DanceEvent',
    'DanceGroup',
    'DataCatalog',
    'DataDownload',
    'DataFeed',
    'DataFeedItem',
    'DataType',
    'Dataset',
    'DatedMoneySpecification',
    'DayOfWeek',
    'DaySpa',
    'DeactivateAction',
    'DefenceEstablishment',
    'DefinedRegion',
    'DefinedTerm',
    'DefinedTermSet',
    'DeleteAction',
    'DeliveryChargeSpecification',
    'DeliveryEvent',
    'DeliveryMethod',
    'Demand',
    'Dentist',
    'DepartAction',
    'DepartmentStore',
    'DepositAccount',
    'DiagnosticLab',
    'DiagnosticProcedure',
    'Diet',
    'DietarySupplement',
    'DigitalDocument',
    'DigitalDocumentPermission',
    'DigitalDocumentPermissionType',
    'DigitalPlatformEnumeration',
    'DisagreeAction',
    'DiscoverAction',
    'DiscussionForumPosting',
    'DislikeAction',
    'Distance',
    'Distillery',
    'DonateAction',
    'DoseSchedule',
    'DownloadAction',
    'DrawAction',
    'Drawing',
    'DrinkAction',
    'DriveWheelConfigurationValue',
    'Drug',
    'DrugClass',
    'DrugCost',
    'DrugCostCategory',
    'DrugLegalStatus',
    'DrugPregnancyCategory',
    'DrugPrescriptionStatus',
    'DrugStrength',
    'DryCleaningOrLaundry',
    'Duration',
    'EUEnergyEfficiencyEnumeration',
    'EatAction',
    'EducationEvent',
    'EducationalAudience',
    'EducationalOccupationalCredential',
    'EducationalOccupationalProgram',
    'EducationalOrganization',
    'Electrician',
    'ElectronicsStore',
    'ElementarySchool',
    'EmailMessage',
    'Embassy',
    'EmergencyService',
    'EmployeeRole',
    'EmployerAggregateRating',
    'EmployerReview',
    'EmploymentAgency',
    'EndorseAction',
    'EndorsementRating',
    'Energy',
    'EnergyConsumptionDetails',
    'EnergyEfficiencyEnumeration',
    'EnergyStarEnergyEfficiencyEnumeration',
    'EngineSpecification',
    'EntertainmentBusiness',
    'EntryPoint',
    'Enumeration',
    'Episode',
    'Event',
    'EventAttendanceModeEnumeration',
    'EventReservation',
    'EventSeries',
    'EventStatusType',
    'EventVenue',
    'ExchangeRateSpecification',
    'ExerciseAction',
    'ExerciseGym',
    'ExercisePlan',
    'ExhibitionEvent',
    'FAQPage',
    'FMRadioChannel',
    'FastFoodRestaurant',
    'Festival',
    'FilmAction',
    'FinancialIncentive',
    'FinancialProduct',
    'FinancialService',
    'FindAction',
    'FireStation',
    'Flight',
    'FlightReservation',
    'Float',
    'FloorPlan',
    'Florist',
    'FollowAction',
    'FoodEstablishment',
    'FoodEstablishmentReservation',
    'FoodEvent',
    'FoodService',
    'FulfillmentTypeEnumeration',
    'FundingAgency',
    'FundingScheme',
    'FurnitureStore',
    'Game',
    'GameAvailabilityEnumeration',
    'GamePlayMode',
    'GameServer',
    'GameServerStatus',
    'GardenStore',
    'GasStation',
    'GatedResidenceCommunity',
    'GenderType',
    'Gene',
    'GeneralContractor',
    'GeoCircle',
    'GeoCoordinates',
    'GeoShape',
    'GeospatialGeometry',
    'GiveAction',
    'GolfCourse',
    'GovernmentBenefitsType',
    'GovernmentBuilding',
    'GovernmentOffice',
    'GovernmentOrganization',
    'GovernmentPermit',
    'GovernmentService',
    'Grant',
    'GroceryStore',
    'Guide',
    'HVACBusiness',
    'Hackathon',
    'HairSalon',
    'HardwareStore',
    'HealthAndBeautyBusiness',
    'HealthAspectEnumeration',
    'HealthClub',
    'HealthInsurancePlan',
    'HealthPlanCostSharingSpecification',
    'HealthPlanFormulary',
    'HealthPlanNetwork',
    'HealthTopicContent',
    'HighSchool',
    'HinduTemple',
    'HobbyShop',
    'HomeAndConstructionBusiness',
    'HomeGoodsStore',
    'Hospital',
    'Hostel',
    'Hotel',
    'HotelRoom',
    'House',
    'HousePainter',
    'HowTo',
    'HowToDirection',
    'HowToItem',
    'HowToSection',
    'HowToStep',
    'HowToSupply',
    'HowToTip',
    'HowToTool',
    'HyperToc',
    'HyperTocEntry',
    'IPTCDigitalSourceEnumeration',
    'IceCreamShop',
    'IgnoreAction',
    'ImageGallery',
    'ImageObject',
    'ImageObjectSnapshot',
    'ImagingTest',
    'IncentiveQualifiedExpenseType',
    'IncentiveStatus',
    'IncentiveType',
    'IndividualPhysician',
    'IndividualProduct',
    'InfectiousAgentClass',
    'InfectiousDisease',
    'InformAction',
    'InsertAction',
    'InstallAction',
    'InsuranceAgency',
    'Intangible',
    'Integer',
    'InteractAction',
    'InteractionCounter',
    'InternetCafe',
    'InvestmentFund',
    'InvestmentOrDeposit',
    'InviteAction',
    'Invoice',
    'ItemAvailability',
    'ItemList',
    'ItemListOrderType',
    'ItemPage',
    'JewelryStore',
    'JobPosting',
    'JoinAction',
    'Joint',
    'LakeBodyOfWater',
    'Landform',
    'LandmarksOrHistoricalBuildings',
    'Language',
    'LearningResource',
    'LeaveAction',
    'LegalForceStatus',
    'LegalService',
    'LegalValueLevel',
    'Legislation',
    'LegislationObject',
    'LegislativeBuilding',
    'LendAction',
    'Library',
    'LibrarySystem',
    'LifestyleModification',
    'Ligament',
    'LikeAction',
    'LinkRole',
    'LiquorStore',
    'ListItem',
    'ListenAction',
    'LiteraryEvent',
    'LiveBlogPosting',
    'LoanOrCredit',
    'LocalBusiness',
    'LocationFeatureSpecification',
    'Locksmith',
    'LodgingBusiness',
    'LodgingReservation',
    'LoseAction',
    'LymphaticVessel',
    'Manuscript',
    'Map',
    'MapCategoryType',
    'MarryAction',
    'Mass',
    'MathSolver',
    'MaximumDoseSchedule',
    'MeasurementMethodEnum',
    'MeasurementTypeEnumeration',
    'MediaEnumeration',
    'MediaGallery',
    'MediaManipulationRatingEnumeration',
    'MediaObject',
    'MediaReview',
    'MediaReviewItem',
    'MediaSubscription',
    'MedicalAudience',
    'MedicalAudienceType',
    'MedicalBusiness',
    'MedicalCause',
    'MedicalClinic',
    'MedicalCode',
    'MedicalCondition',
    'MedicalConditionStage',
    'MedicalContraindication',
    'MedicalDevice',
    'MedicalDevicePurpose',
    'MedicalEntity',
    'MedicalEnumeration',
    'MedicalEvidenceLevel',
    'MedicalGuideline',
    'MedicalGuidelineContraindication',
    'MedicalGuidelineRecommendation',
    'MedicalImagingTechnique',
    'MedicalIndication',
    'MedicalIntangible',
    'MedicalObservationalStudy',
    'MedicalObservationalStudyDesign',
    'MedicalOrganization',
    'MedicalProcedure',
    'MedicalProcedureType',
    'MedicalRiskCalculator',
    'MedicalRiskEstimator',
    'MedicalRiskFactor',
    'MedicalRiskScore',
    'MedicalScholarlyArticle',
    'MedicalSign',
    'MedicalSignOrSymptom',
    'MedicalSpecialty',
    'MedicalStudy',
    'MedicalStudyStatus',
    'MedicalSymptom',
    'MedicalTest',
    'MedicalTestPanel',
    'MedicalTherapy',
    'MedicalTrial',
    'MedicalTrialDesign',
    'MedicalWebPage',
    'MedicineSystem',
    'MeetingRoom',
    'MemberProgram',
    'MemberProgramTier',
    'MensClothingStore',
    'Menu',
    'MenuItem',
    'MenuSection',
    'MerchantReturnEnumeration',
    'MerchantReturnPolicy',
    'MerchantReturnPolicySeasonalOverride',
    'Message',
    'MiddleSchool',
    'MobileApplication',
    'MobilePhoneStore',
    'MolecularEntity',
    'MonetaryAmount',
    'MonetaryAmountDistribution',
    'MonetaryGrant',
    'MoneyTransfer',
    'MortgageLoan',
    'Mosque',
    'Motel',
    'Motorcycle',
    'MotorcycleDealer',
    'MotorcycleRepair',
    'MotorizedBicycle',
    'Mountain',
    'MoveAction',
    'Movie',
    'MovieClip',
    'MovieRentalStore',
    'MovieSeries',
    'MovieTheater',
    'MovingCompany',
    'Muscle',
    'Museum',
    'MusicAlbum',
    'MusicAlbumProductionType',
    'MusicAlbumReleaseType',
    'MusicComposition',
    'MusicEvent',
    'MusicGroup',
    'MusicPlaylist',
    'MusicRecording',
    'MusicRelease',
    'MusicReleaseFormatType',
    'MusicStore',
    'MusicVenue',
    'MusicVideoObject',
    'NGO',
    'NLNonprofitType',
    'NailSalon',
    'Nerve',
    'NewsArticle',
    'NewsMediaOrganization',
    'Newspaper',
    'NightClub',
    'NonprofitType',
    'Notary',
    'NoteDigitalDocument',
    'NutritionInformation',
    'Observation',
    'Occupation',
    'OccupationalExperienceRequirements',
    'OccupationalTherapy',
    'OceanBodyOfWater',
    'Offer',
    'OfferCatalog',
    'OfferForLease',
    'OfferForPurchase',
    'OfferItemCondition',
    'OfferShippingDetails',
    'OfficeEquipmentStore',
    'OnDemandEvent',
    'OnlineBusiness',
    'OnlineStore',
    'OpeningHoursSpecification',
    'OpinionNewsArticle',
    'Optician',
    'Order',
    'OrderAction',
    'OrderItem',
    'OrderStatus',
    'Organization',
    'OrganizationRole',
    'OrganizeAction',
    'OutletStore',
    'OwnershipInfo',
    'PaintAction',
    'Painting',
    'PalliativeProcedure',
    'ParcelDelivery',
    'ParentAudience',
    'Park',
    'ParkingFacility',
    'PathologyTest',
    'Patient',
    'PawnShop',
    'PayAction',
    'PaymentCard',
    'PaymentChargeSpecification',
    'PaymentMethod',
    'PaymentMethodType',
    'PaymentService',
    'PaymentStatusType',
    'PeopleAudience',
    'PerformAction',
    'PerformanceRole',
    'PerformingArtsTheater',
    'PerformingGroup',
    'Periodical',
    'Permit',
    'Person',
    'PetStore',
    'Pharmacy',
    'Photograph',
    'PhotographAction',
    'PhysicalActivity',
    'PhysicalExam',
    'PhysicalTherapy',
    'Physician',
    'PhysiciansOffice',
    'Place',
    'PlaceOfWorship',
    'PlanAction',
    'Play',
    'PlayAction',
    'PlayGameAction',
    'Playground',
    'Plumber',
    'PodcastEpisode',
    'PodcastSeason',
    'PodcastSeries',
    'PoliceStation',
    'PoliticalParty',
    'Pond',
    'PostOffice',
    'PostalAddress',
    'PostalCodeRangeSpecification',
    'Poster',
    'PreOrderAction',
    'PrependAction',
    'Preschool',
    'PresentationDigitalDocument',
    'PreventionIndication',
    'PriceComponentTypeEnumeration',
    'PriceSpecification',
    'PriceTypeEnumeration',
    'Product',
    'ProductCollection',
    'ProductGroup',
    'ProductModel',
    'ProfessionalService',
    'ProfilePage',
    'ProgramMembership',
    'Project',
    'PronounceableText',
    'Property',
    'PropertyValue',
    'PropertyValueSpecification',
    'Protein',
    'PsychologicalTreatment',
    'PublicSwimmingPool',
    'PublicToilet',
    'PublicationEvent',
    'PublicationIssue',
    'PublicationVolume',
    'PurchaseType',
    'QAPage',
    'QualitativeValue',
    'QuantitativeValue',
    'QuantitativeValueDistribution',
    'Quantity',
    'Question',
    'Quiz',
    'Quotation',
    'QuoteAction',
    'RVPark',
    'RadiationTherapy',
    'RadioBroadcastService',
    'RadioChannel',
    'RadioClip',
    'RadioEpisode',
    'RadioSeason',
    'RadioSeries',
    'RadioStation',
    'Rating',
    'ReactAction',
    'ReadAction',
    'RealEstateAgent',
    'RealEstateListing',
    'ReceiveAction',
    'Recipe',
    'Recommendation',
    'RecommendedDoseSchedule',
    'RecyclingCenter',
    'RefundTypeEnumeration',
    'RegisterAction',
    'RejectAction',
    'RentAction',
    'RentalCarReservation',
    'RepaymentSpecification',
    'ReplaceAction',
    'ReplyAction',
    'Report',
    'ReportageNewsArticle',
    'ReportedDoseSchedule',
    'ResearchOrganization',
    'ResearchProject',
    'Researcher',
    'Reservation',
    'ReservationPackage',
    'ReservationStatusType',
    'ReserveAction',
    'Reservoir',
    'Residence',
    'Resort',
    'Restaurant',
    'RestrictedDiet',
    'ResumeAction',
    'ReturnAction',
    'ReturnFeesEnumeration',
    'ReturnLabelSourceEnumeration',
    'ReturnMethodEnumeration',
    'Review',
    'ReviewAction',
    'ReviewNewsArticle',
    'RiverBodyOfWater',
    'Role',
    'RoofingContractor',
    'Room',
    'RsvpAction',
    'RsvpResponseType',
    'SaleEvent',
    'SatiricalArticle',
    'Schedule',
    'ScheduleAction',
    'ScholarlyArticle',
    'School',
    'SchoolDistrict',
    'ScreeningEvent',
    'Sculpture',
    'SeaBodyOfWater',
    'SearchAction',
    'SearchRescueOrganization',
    'SearchResultsPage',
    'Season',
    'Seat',
    'SeekToAction',
    'SelfStorage',
    'SellAction',
    'SendAction',
    'Series',
    'Service',
    'ServiceChannel',
    'ServicePeriod',
    'ShareAction',
    'SheetMusic',
    'ShippingConditions',
    'ShippingDeliveryTime',
    'ShippingRateSettings',
    'ShippingService',
    'ShoeStore',
    'ShoppingCenter',
    'ShortStory',
    'SingleFamilyResidence',
    'SiteNavigationElement',
    'SizeGroupEnumeration',
    'SizeSpecification',
    'SizeSystemEnumeration',
    'SkiResort',
    'SocialEvent',
    'SocialMediaPosting',
    'SoftwareApplication',
    'SoftwareSourceCode',
    'SolveMathAction',
    'SomeProducts',
    'SpeakableSpecification',
    'SpecialAnnouncement',
    'Specialty',
    'SportingGoodsStore',
    'SportsActivityLocation',
    'SportsClub',
    'SportsEvent',
    'SportsOrganization',
    'SportsTeam',
    'SpreadsheetDigitalDocument',
    'StadiumOrArena',
    'State',
    'Statement',
    'StatisticalPopulation',
    'StatisticalVariable',
    'StatusEnumeration',
    'SteeringPositionValue',
    'Store',
    'StructuredValue',
    'SubscribeAction',
    'Substance',
    'SubwayStation',
    'Suite',
    'SuperficialAnatomy',
    'SurgicalProcedure',
    'SuspendAction',
    'Syllabus',
    'Synagogue',
    'TVClip',
    'TVEpisode',
    'TVSeason',
    'TVSeries',
    'Table',
    'TakeAction',
    'TattooParlor',
    'Taxi',
    'TaxiReservation',
    'TaxiService',
    'TaxiStand',
    'Taxon',
    'TechArticle',
    'TelevisionChannel',
    'TelevisionStation',
    'TennisComplex',
    'TextDigitalDocument',
    'TextObject',
    'TheaterEvent',
    'TheaterGroup',
    'TherapeuticProcedure',
    'Thesis',
    'Thing',
    'Ticket',
    'TieAction',
    'TierBenefitEnumeration',
    'TipAction',
    'TireShop',
    'TouristAttraction',
    'TouristDestination',
    'TouristInformationCenter',
    'TouristTrip',
    'ToyStore',
    'TrackAction',
    'TradeAction',
    'TrainReservation',
    'TrainStation',
    'TrainTrip',
    'TransferAction',
    'TravelAction',
    'TravelAgency',
    'TreatmentIndication',
    'Trip',
    'TypeAndQuantityNode',
    'UKNonprofitType',
    'URL',
    'USNonprofitType',
    'UnRegisterAction',
    'UnitPriceSpecification',
    'UpdateAction',
    'UseAction',
    'UserBlocks',
    'UserCheckins',
    'UserComments',
    'UserDownloads',
    'UserInteraction',
    'UserLikes',
    'UserPageVisits',
    'UserPlays',
    'UserPlusOnes',
    'UserReview',
    'UserTweets',
    'VacationRental',
    'Vehicle',
    'Vein',
    'Vessel',
    'VeterinaryCare',
    'VideoGallery',
    'VideoGame',
    'VideoGameClip',
    'VideoGameSeries',
    'VideoObject',
    'VideoObjectSnapshot',
    'ViewAction',
    'VirtualLocation',
    'VisualArtsEvent',
    'VisualArtwork',
    'VitalSign',
    'Volcano',
    'VoteAction',
    'WPAdBlock',
    'WPFooter',
    'WPHeader',
    'WPSideBar',
    'WantAction',
    'WarrantyPromise',
    'WarrantyScope',
    'WatchAction',
    'Waterfall',
    'WearAction',
    'WearableMeasurementTypeEnumeration',
    'WearableSizeGroupEnumeration',
    'WearableSizeSystemEnumeration',
    'WebAPI',
    'WebApplication',
    'WebContent',
    'WebPage',
    'WebPageElement',
    'WebSite',
    'WholesaleStore',
    'WinAction',
    'Winery',
    'WorkBasedProgram',
    'WorkersUnion',
    'WriteAction',
    'XPathType',
    'Zoo',
]
