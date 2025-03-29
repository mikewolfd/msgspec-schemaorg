import enum
from typing import ClassVar, Dict, Any

class MedicalEvidenceLevel(str, enum.Enum):
    """Schema.org enumeration values for MedicalEvidenceLevel."""

    EvidenceLevelA = "EvidenceLevelA"  # "Data derived from multiple randomized clinical trials or ..."
    EvidenceLevelB = "EvidenceLevelB"  # "Data derived from a single randomized trial, or nonrandom..."
    EvidenceLevelC = "EvidenceLevelC"  # "Only consensus opinion of experts, case studies, or stand..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "EvidenceLevelA": {
            "id": "schema:EvidenceLevelA",
            "comment": """Data derived from multiple randomized clinical trials or meta-analyses.""",
            "label": "EvidenceLevelA",
        },
        "EvidenceLevelB": {
            "id": "schema:EvidenceLevelB",
            "comment": """Data derived from a single randomized trial, or nonrandomized studies.""",
            "label": "EvidenceLevelB",
        },
        "EvidenceLevelC": {
            "id": "schema:EvidenceLevelC",
            "comment": """Only consensus opinion of experts, case studies, or standard-of-care.""",
            "label": "EvidenceLevelC",
        },
    }