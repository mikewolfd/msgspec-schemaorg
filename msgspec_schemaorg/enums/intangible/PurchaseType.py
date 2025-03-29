import enum
from typing import ClassVar, Dict, Any

class PurchaseType(str, enum.Enum):
    """Schema.org enumeration values for PurchaseType."""

    PurchaseTypeLease = "PurchaseTypeLease"  # "This is a lease of an item."
    PurchaseTypeNewPurchase = "PurchaseTypeNewPurchase"  # "This is a purchase of a new item."
    PurchaseTypeTradeIn = "PurchaseTypeTradeIn"  # "This is a trade-in for an item."
    PurchaseTypeUsedPurchase = "PurchaseTypeUsedPurchase"  # "This is a purchase of a used item."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "PurchaseTypeLease": {
            "id": "schema:PurchaseTypeLease",
            "comment": """This is a lease of an item.""",
            "label": "PurchaseTypeLease",
        },
        "PurchaseTypeNewPurchase": {
            "id": "schema:PurchaseTypeNewPurchase",
            "comment": """This is a purchase of a new item.""",
            "label": "PurchaseTypeNewPurchase",
        },
        "PurchaseTypeTradeIn": {
            "id": "schema:PurchaseTypeTradeIn",
            "comment": """This is a trade-in for an item.""",
            "label": "PurchaseTypeTradeIn",
        },
        "PurchaseTypeUsedPurchase": {
            "id": "schema:PurchaseTypeUsedPurchase",
            "comment": """This is a purchase of a used item.""",
            "label": "PurchaseTypeUsedPurchase",
        },
    }