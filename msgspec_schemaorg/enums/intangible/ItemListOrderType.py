import enum
from typing import ClassVar, Dict, Any

class ItemListOrderType(str, enum.Enum):
    """Schema.org enumeration values for ItemListOrderType."""

    ItemListOrderAscending = "ItemListOrderAscending"  # "An ItemList ordered with lower values listed first."
    ItemListOrderDescending = "ItemListOrderDescending"  # "An ItemList ordered with higher values listed first."
    ItemListUnordered = "ItemListUnordered"  # "An ItemList ordered with no explicit order."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ItemListOrderAscending": {
            "id": "schema:ItemListOrderAscending",
            "comment": """An ItemList ordered with lower values listed first.""",
            "label": "ItemListOrderAscending",
        },
        "ItemListOrderDescending": {
            "id": "schema:ItemListOrderDescending",
            "comment": """An ItemList ordered with higher values listed first.""",
            "label": "ItemListOrderDescending",
        },
        "ItemListUnordered": {
            "id": "schema:ItemListUnordered",
            "comment": """An ItemList ordered with no explicit order.""",
            "label": "ItemListUnordered",
        },
    }