import enum
from typing import ClassVar, Dict, Any

class ItemAvailability(str, enum.Enum):
    """Schema.org enumeration values for ItemAvailability."""

    BackOrder = "BackOrder"  # "Indicates that the item is available on back order."
    Discontinued = "Discontinued"  # "Indicates that the item has been discontinued."
    InStock = "InStock"  # "Indicates that the item is in stock."
    InStoreOnly = "InStoreOnly"  # "Indicates that the item is available only at physical loc..."
    LimitedAvailability = "LimitedAvailability"  # "Indicates that the item has limited availability."
    MadeToOrder = "MadeToOrder"  # "Indicates that the item is made to order (custom made)."
    OnlineOnly = "OnlineOnly"  # "Indicates that the item is available only online."
    OutOfStock = "OutOfStock"  # "Indicates that the item is out of stock."
    PreOrder = "PreOrder"  # "Indicates that the item is available for pre-order."
    PreSale = "PreSale"  # "Indicates that the item is available for ordering and del..."
    Reserved = "Reserved"  # "Indicates that the item is reserved and therefore not ava..."
    SoldOut = "SoldOut"  # "Indicates that the item has sold out."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "BackOrder": {
            "id": "schema:BackOrder",
            "comment": """Indicates that the item is available on back order.""",
            "label": "BackOrder",
        },
        "Discontinued": {
            "id": "schema:Discontinued",
            "comment": """Indicates that the item has been discontinued.""",
            "label": "Discontinued",
        },
        "InStock": {
            "id": "schema:InStock",
            "comment": """Indicates that the item is in stock.""",
            "label": "InStock",
        },
        "InStoreOnly": {
            "id": "schema:InStoreOnly",
            "comment": """Indicates that the item is available only at physical locations.""",
            "label": "InStoreOnly",
        },
        "LimitedAvailability": {
            "id": "schema:LimitedAvailability",
            "comment": """Indicates that the item has limited availability.""",
            "label": "LimitedAvailability",
        },
        "MadeToOrder": {
            "id": "schema:MadeToOrder",
            "comment": """Indicates that the item is made to order (custom made).""",
            "label": "MadeToOrder",
        },
        "OnlineOnly": {
            "id": "schema:OnlineOnly",
            "comment": """Indicates that the item is available only online.""",
            "label": "OnlineOnly",
        },
        "OutOfStock": {
            "id": "schema:OutOfStock",
            "comment": """Indicates that the item is out of stock.""",
            "label": "OutOfStock",
        },
        "PreOrder": {
            "id": "schema:PreOrder",
            "comment": """Indicates that the item is available for pre-order.""",
            "label": "PreOrder",
        },
        "PreSale": {
            "id": "schema:PreSale",
            "comment": """Indicates that the item is available for ordering and delivery before general availability.""",
            "label": "PreSale",
        },
        "Reserved": {
            "id": "schema:Reserved",
            "comment": """Indicates that the item is reserved and therefore not available.""",
            "label": "Reserved",
        },
        "SoldOut": {
            "id": "schema:SoldOut",
            "comment": """Indicates that the item has sold out.""",
            "label": "SoldOut",
        },
    }