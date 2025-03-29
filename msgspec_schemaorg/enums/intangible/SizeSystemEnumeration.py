import enum
from typing import ClassVar, Dict, Any

class SizeSystemEnumeration(str, enum.Enum):
    """Schema.org enumeration values for SizeSystemEnumeration."""

    SizeSystemImperial = "SizeSystemImperial"  # "Imperial size system."
    SizeSystemMetric = "SizeSystemMetric"  # "Metric size system."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "SizeSystemImperial": {
            "id": "schema:SizeSystemImperial",
            "comment": """Imperial size system.""",
            "label": "SizeSystemImperial",
        },
        "SizeSystemMetric": {
            "id": "schema:SizeSystemMetric",
            "comment": """Metric size system.""",
            "label": "SizeSystemMetric",
        },
    }