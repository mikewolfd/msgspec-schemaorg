import enum
from typing import ClassVar, Dict, Any

class OfferItemCondition(str, enum.Enum):
    """Schema.org enumeration values for OfferItemCondition."""

    DamagedCondition = "DamagedCondition"  # "Indicates that the item is damaged."
    NewCondition = "NewCondition"  # "Indicates that the item is new."
    RefurbishedCondition = "RefurbishedCondition"  # "Indicates that the item is refurbished."
    UsedCondition = "UsedCondition"  # "Indicates that the item is used."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "DamagedCondition": {
            "id": "schema:DamagedCondition",
            "comment": """Indicates that the item is damaged.""",
            "label": "DamagedCondition",
        },
        "NewCondition": {
            "id": "schema:NewCondition",
            "comment": """Indicates that the item is new.""",
            "label": "NewCondition",
        },
        "RefurbishedCondition": {
            "id": "schema:RefurbishedCondition",
            "comment": """Indicates that the item is refurbished.""",
            "label": "RefurbishedCondition",
        },
        "UsedCondition": {
            "id": "schema:UsedCondition",
            "comment": """Indicates that the item is used.""",
            "label": "UsedCondition",
        },
    }