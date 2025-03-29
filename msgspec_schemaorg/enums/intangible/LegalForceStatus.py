import enum
from typing import ClassVar, Dict, Any

class LegalForceStatus(str, enum.Enum):
    """Schema.org enumeration values for LegalForceStatus."""

    InForce = "InForce"  # "Indicates that a legislation is in force."
    NotInForce = "NotInForce"  # "Indicates that a legislation is currently not in force."
    PartiallyInForce = "PartiallyInForce"  # "Indicates that parts of the legislation are in force, and..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "InForce": {
            "id": "schema:InForce",
            "comment": """Indicates that a legislation is in force.""",
            "label": "InForce",
        },
        "NotInForce": {
            "id": "schema:NotInForce",
            "comment": """Indicates that a legislation is currently not in force.""",
            "label": "NotInForce",
        },
        "PartiallyInForce": {
            "id": "schema:PartiallyInForce",
            "comment": """Indicates that parts of the legislation are in force, and parts are not.""",
            "label": "PartiallyInForce",
        },
    }