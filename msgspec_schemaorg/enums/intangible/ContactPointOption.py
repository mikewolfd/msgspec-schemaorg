import enum
from typing import ClassVar, Dict, Any

class ContactPointOption(str, enum.Enum):
    """Schema.org enumeration values for ContactPointOption."""

    HearingImpairedSupported = "HearingImpairedSupported"  # "Uses devices to support users with hearing impairments."
    TollFree = "TollFree"  # "The associated telephone number is toll free."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "HearingImpairedSupported": {
            "id": "schema:HearingImpairedSupported",
            "comment": """Uses devices to support users with hearing impairments.""",
            "label": "HearingImpairedSupported",
        },
        "TollFree": {
            "id": "schema:TollFree",
            "comment": """The associated telephone number is toll free.""",
            "label": "TollFree",
        },
    }