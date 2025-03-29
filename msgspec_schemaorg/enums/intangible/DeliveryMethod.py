import enum
from typing import ClassVar, Dict, Any

class DeliveryMethod(str, enum.Enum):
    """Schema.org enumeration values for DeliveryMethod."""

    LockerDelivery = "LockerDelivery"  # "A DeliveryMethod in which an item is made available via l..."
    OnSitePickup = "OnSitePickup"  # "A DeliveryMethod in which an item is collected on site, e..."
    ParcelService = "ParcelService"  # "A private parcel service as the delivery mode available f..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "LockerDelivery": {
            "id": "schema:LockerDelivery",
            "comment": """A DeliveryMethod in which an item is made available via locker.""",
            "label": "LockerDelivery",
        },
        "OnSitePickup": {
            "id": "schema:OnSitePickup",
            "comment": """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.""",
            "label": "OnSitePickup",
        },
        "ParcelService": {
            "id": "schema:ParcelService",
            "comment": """A private parcel service as the delivery mode available for a certain offer.\n\nCommonly used values:\n\n* http://purl.org/goodrelations/v1#DHL\n* http://purl.org/goodrelations/v1#FederalExpress\n* http://purl.org/goodrelations/v1#UPS
      """,
            "label": "ParcelService",
        },
    }