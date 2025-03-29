import enum
from typing import ClassVar, Dict, Any

class MedicalAudienceType(str, enum.Enum):
    """Schema.org enumeration values for MedicalAudienceType."""

    Clinician = "Clinician"  # "Medical clinicians, including practicing physicians and o..."
    MedicalResearcher = "MedicalResearcher"  # "Medical researchers."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Clinician": {
            "id": "schema:Clinician",
            "comment": """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.""",
            "label": "Clinician",
        },
        "MedicalResearcher": {
            "id": "schema:MedicalResearcher",
            "comment": """Medical researchers.""",
            "label": "MedicalResearcher",
        },
    }