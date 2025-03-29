import enum
from typing import ClassVar, Dict, Any

class FulfillmentTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for FulfillmentTypeEnumeration."""

    FulfillmentTypeCollectionPoint = "FulfillmentTypeCollectionPoint"  # "Fulfillment to a collection point location."
    FulfillmentTypeDelivery = "FulfillmentTypeDelivery"  # "Fulfillment to a customer selected address."
    FulfillmentTypePickupDropoff = "FulfillmentTypePickupDropoff"  # "Fulfillment through pick-up drop-off locations."
    FulfillmentTypePickupInStore = "FulfillmentTypePickupInStore"  # "Fulfillment through pick-up in a store."
    FulfillmentTypeScheduledDelivery = "FulfillmentTypeScheduledDelivery"  # "Fulfillment to a customer selected address after scheduli..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "FulfillmentTypeCollectionPoint": {
            "id": "schema:FulfillmentTypeCollectionPoint",
            "comment": """Fulfillment to a collection point location.""",
            "label": "FulfillmentTypeCollectionPoint",
        },
        "FulfillmentTypeDelivery": {
            "id": "schema:FulfillmentTypeDelivery",
            "comment": """Fulfillment to a customer selected address.""",
            "label": "FulfillmentTypeDelivery",
        },
        "FulfillmentTypePickupDropoff": {
            "id": "schema:FulfillmentTypePickupDropoff",
            "comment": """Fulfillment through pick-up drop-off locations.""",
            "label": "FulfillmentTypePickupDropoff",
        },
        "FulfillmentTypePickupInStore": {
            "id": "schema:FulfillmentTypePickupInStore",
            "comment": """Fulfillment through pick-up in a store.""",
            "label": "FulfillmentTypePickupInStore",
        },
        "FulfillmentTypeScheduledDelivery": {
            "id": "schema:FulfillmentTypeScheduledDelivery",
            "comment": """Fulfillment to a customer selected address after scheduling with the customer.""",
            "label": "FulfillmentTypeScheduledDelivery",
        },
    }