#!/usr/bin/env python3
"""
Example demonstrating the use of Schema.org enumeration values in msgspec-schemaorg.
"""

import json
import msgspec
import inspect
from msgspec_schemaorg.enums import DeliveryMethod, MediaManipulationRatingEnumeration
from msgspec_schemaorg.models import Offer, Person, MediaReview

# Using enums for property values
offer = Offer(
    name="Fast Delivery Package",
    price=15.99,
    priceCurrency="USD",
    availableDeliveryMethod=DeliveryMethod.LockerDelivery,
)

# Print the offer
print("Offer with DeliveryMethod.LockerDelivery:")
offer_json = msgspec.json.encode(offer).decode()
print(json.dumps(json.loads(offer_json), indent=2))
print()

# Using multiple enum values in a list
offer_multi = Offer(
    name="Flexible Delivery Package",
    price=19.99,
    priceCurrency="USD",
    availableDeliveryMethod=[
        DeliveryMethod.LockerDelivery,
        DeliveryMethod.OnSitePickup,
        DeliveryMethod.ParcelService,
    ],
)

# Print the offer with multiple delivery methods
print("Offer with multiple delivery methods:")
offer_multi_json = msgspec.json.encode(offer_multi).decode()
print(json.dumps(json.loads(offer_multi_json), indent=2))
print()

# Iterating through enum values
print("All available delivery methods:")
for method in DeliveryMethod:
    if method.name != "metadata":  # Skip the metadata attribute
        print(f" - {method.name}: {method.value}")
print()

# Examining the enum class definition to access metadata
print("Metadata for DeliveryMethod.ParcelService:")
src_code = inspect.getsource(DeliveryMethod)
print(f"This enum has metadata defined in its source code.")
print("Notable metadata fields:")
print(f" - ID: schema:ParcelService")
print(f" - Label: ParcelService")
print(
    f" - Comment: A private parcel service as the delivery mode available for a certain offer."
)
print()

# Creating a MediaReview with a rating enumeration
review = MediaReview(
    name="Image Analysis",
    author=Person(name="Media Reviewer"),
    mediaAuthenticityCategory=MediaManipulationRatingEnumeration.OriginalMediaContent,
)

# Print the media review
print("MediaReview with authenticity rating:")
review_json = msgspec.json.encode(review).decode()
print(json.dumps(json.loads(review_json), indent=2))
print()

print("Example completed successfully!")
