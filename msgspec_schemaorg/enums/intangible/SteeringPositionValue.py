import enum
from typing import ClassVar, Dict, Any

class SteeringPositionValue(str, enum.Enum):
    """Schema.org enumeration values for SteeringPositionValue."""

    LeftHandDriving = "LeftHandDriving"  # "The steering position is on the left side of the vehicle ..."
    RightHandDriving = "RightHandDriving"  # "The steering position is on the right side of the vehicle..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "LeftHandDriving": {
            "id": "schema:LeftHandDriving",
            "comment": """The steering position is on the left side of the vehicle (viewed from the main direction of driving).""",
            "label": "LeftHandDriving",
        },
        "RightHandDriving": {
            "id": "schema:RightHandDriving",
            "comment": """The steering position is on the right side of the vehicle (viewed from the main direction of driving).""",
            "label": "RightHandDriving",
        },
    }