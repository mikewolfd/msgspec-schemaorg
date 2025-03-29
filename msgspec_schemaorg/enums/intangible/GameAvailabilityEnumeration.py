import enum
from typing import ClassVar, Dict, Any

class GameAvailabilityEnumeration(str, enum.Enum):
    """Schema.org enumeration values for GameAvailabilityEnumeration."""

    DemoGameAvailability = "DemoGameAvailability"  # "Indicates demo game availability, i.e. a somehow limited ..."
    FullGameAvailability = "FullGameAvailability"  # "Indicates full game availability."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "DemoGameAvailability": {
            "id": "schema:DemoGameAvailability",
            "comment": """Indicates demo game availability, i.e. a somehow limited demonstration of the full game.""",
            "label": "DemoGameAvailability",
        },
        "FullGameAvailability": {
            "id": "schema:FullGameAvailability",
            "comment": """Indicates full game availability.""",
            "label": "FullGameAvailability",
        },
    }