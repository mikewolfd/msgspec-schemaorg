import enum
from typing import ClassVar, Dict, Any

class DrugPrescriptionStatus(str, enum.Enum):
    """Schema.org enumeration values for DrugPrescriptionStatus."""

    OTC = "OTC"  # "The character of a medical substance, typically a medicin..."
    PrescriptionOnly = "PrescriptionOnly"  # "Available by prescription only."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "OTC": {
            "id": "schema:OTC",
            "comment": """The character of a medical substance, typically a medicine, of being available over the counter or not.""",
            "label": "OTC",
        },
        "PrescriptionOnly": {
            "id": "schema:PrescriptionOnly",
            "comment": """Available by prescription only.""",
            "label": "PrescriptionOnly",
        },
    }