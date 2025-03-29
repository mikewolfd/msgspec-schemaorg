import enum
from typing import ClassVar, Dict, Any

class GenderType(str, enum.Enum):
    """Schema.org enumeration values for GenderType."""

    Female = "Female"  # "The female gender."
    Male = "Male"  # "The male gender."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Female": {
            "id": "schema:Female",
            "comment": """The female gender.""",
            "label": "Female",
        },
        "Male": {
            "id": "schema:Male",
            "comment": """The male gender.""",
            "label": "Male",
        },
    }