import enum
from typing import ClassVar, Dict, Any

class DriveWheelConfigurationValue(str, enum.Enum):
    """Schema.org enumeration values for DriveWheelConfigurationValue."""

    AllWheelDriveConfiguration = "AllWheelDriveConfiguration"  # "All-wheel Drive is a transmission layout where the engine..."
    FourWheelDriveConfiguration = "FourWheelDriveConfiguration"  # "Four-wheel drive is a transmission layout where the engin..."
    FrontWheelDriveConfiguration = "FrontWheelDriveConfiguration"  # "Front-wheel drive is a transmission layout where the engi..."
    RearWheelDriveConfiguration = "RearWheelDriveConfiguration"  # "Real-wheel drive is a transmission layout where the engin..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AllWheelDriveConfiguration": {
            "id": "schema:AllWheelDriveConfiguration",
            "comment": """All-wheel Drive is a transmission layout where the engine drives all four wheels.""",
            "label": "AllWheelDriveConfiguration",
        },
        "FourWheelDriveConfiguration": {
            "id": "schema:FourWheelDriveConfiguration",
            "comment": """Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.""",
            "label": "FourWheelDriveConfiguration",
        },
        "FrontWheelDriveConfiguration": {
            "id": "schema:FrontWheelDriveConfiguration",
            "comment": """Front-wheel drive is a transmission layout where the engine drives the front wheels.""",
            "label": "FrontWheelDriveConfiguration",
        },
        "RearWheelDriveConfiguration": {
            "id": "schema:RearWheelDriveConfiguration",
            "comment": """Real-wheel drive is a transmission layout where the engine drives the rear wheels.""",
            "label": "RearWheelDriveConfiguration",
        },
    }