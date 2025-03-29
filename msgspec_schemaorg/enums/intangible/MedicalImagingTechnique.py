import enum
from typing import ClassVar, Dict, Any

class MedicalImagingTechnique(str, enum.Enum):
    """Schema.org enumeration values for MedicalImagingTechnique."""

    CT = "CT"  # "X-ray computed tomography imaging."
    MRI = "MRI"  # "Magnetic resonance imaging."
    PET = "PET"  # "Positron emission tomography imaging."
    Radiography = "Radiography"  # "Radiography is an imaging technique that uses electromagn..."
    Ultrasound = "Ultrasound"  # "Ultrasound imaging."
    XRay = "XRay"  # "X-ray imaging."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CT": {
            "id": "schema:CT",
            "comment": """X-ray computed tomography imaging.""",
            "label": "CT",
        },
        "MRI": {
            "id": "schema:MRI",
            "comment": """Magnetic resonance imaging.""",
            "label": "MRI",
        },
        "PET": {
            "id": "schema:PET",
            "comment": """Positron emission tomography imaging.""",
            "label": "PET",
        },
        "Radiography": {
            "id": "schema:Radiography",
            "comment": """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.""",
            "label": "Radiography",
        },
        "Ultrasound": {
            "id": "schema:Ultrasound",
            "comment": """Ultrasound imaging.""",
            "label": "Ultrasound",
        },
        "XRay": {
            "id": "schema:XRay",
            "comment": """X-ray imaging.""",
            "label": "XRay",
        },
    }