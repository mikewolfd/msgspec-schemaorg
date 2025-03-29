import enum
from typing import ClassVar, Dict, Any

class MeasurementMethodEnum(str, enum.Enum):
    """Schema.org enumeration values for MeasurementMethodEnum."""

    ExampleMeasurementMethodEnum = "ExampleMeasurementMethodEnum"  # "An example [[MeasurementMethodEnum]] (to remove when real..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ExampleMeasurementMethodEnum": {
            "id": "schema:ExampleMeasurementMethodEnum",
            "comment": """An example [[MeasurementMethodEnum]] (to remove when real enums are added).""",
            "label": "ExampleMeasurementMethodEnum",
        },
    }