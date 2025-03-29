import enum
from typing import ClassVar, Dict, Any

class InfectiousAgentClass(str, enum.Enum):
    """Schema.org enumeration values for InfectiousAgentClass."""

    Bacteria = "Bacteria"  # "Pathogenic bacteria that cause bacterial infection."
    Fungus = "Fungus"  # "Pathogenic fungus."
    MulticellularParasite = "MulticellularParasite"  # "Multicellular parasite that causes an infection."
    Prion = "Prion"  # "A prion is an infectious agent composed of protein in a m..."
    Protozoa = "Protozoa"  # "Single-celled organism that causes an infection."
    Virus = "Virus"  # "Pathogenic virus that causes viral infection."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Bacteria": {
            "id": "schema:Bacteria",
            "comment": """Pathogenic bacteria that cause bacterial infection.""",
            "label": "Bacteria",
        },
        "Fungus": {
            "id": "schema:Fungus",
            "comment": """Pathogenic fungus.""",
            "label": "Fungus",
        },
        "MulticellularParasite": {
            "id": "schema:MulticellularParasite",
            "comment": """Multicellular parasite that causes an infection.""",
            "label": "MulticellularParasite",
        },
        "Prion": {
            "id": "schema:Prion",
            "comment": """A prion is an infectious agent composed of protein in a misfolded form.""",
            "label": "Prion",
        },
        "Protozoa": {
            "id": "schema:Protozoa",
            "comment": """Single-celled organism that causes an infection.""",
            "label": "Protozoa",
        },
        "Virus": {
            "id": "schema:Virus",
            "comment": """Pathogenic virus that causes viral infection.""",
            "label": "Virus",
        },
    }