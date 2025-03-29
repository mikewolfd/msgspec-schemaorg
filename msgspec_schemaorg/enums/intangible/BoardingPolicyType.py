import enum
from typing import ClassVar, Dict, Any

class BoardingPolicyType(str, enum.Enum):
    """Schema.org enumeration values for BoardingPolicyType."""

    GroupBoardingPolicy = "GroupBoardingPolicy"  # "The airline boards by groups based on check-in time, prio..."
    ZoneBoardingPolicy = "ZoneBoardingPolicy"  # "The airline boards by zones of the plane."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "GroupBoardingPolicy": {
            "id": "schema:GroupBoardingPolicy",
            "comment": """The airline boards by groups based on check-in time, priority, etc.""",
            "label": "GroupBoardingPolicy",
        },
        "ZoneBoardingPolicy": {
            "id": "schema:ZoneBoardingPolicy",
            "comment": """The airline boards by zones of the plane.""",
            "label": "ZoneBoardingPolicy",
        },
    }