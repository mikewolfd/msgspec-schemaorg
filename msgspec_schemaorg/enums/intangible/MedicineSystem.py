import enum
from typing import ClassVar, Dict, Any

class MedicineSystem(str, enum.Enum):
    """Schema.org enumeration values for MedicineSystem."""

    Ayurvedic = "Ayurvedic"  # "A system of medicine that originated in India over thousa..."
    Chiropractic = "Chiropractic"  # "A system of medicine focused on the relationship between ..."
    Homeopathic = "Homeopathic"  # "A system of medicine based on the principle that a diseas..."
    Osteopathic = "Osteopathic"  # "A system of medicine focused on promoting the body's inna..."
    TraditionalChinese = "TraditionalChinese"  # "A system of medicine based on common theoretical concepts..."
    WesternConventional = "WesternConventional"  # "The conventional Western system of medicine, that aims to..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Ayurvedic": {
            "id": "schema:Ayurvedic",
            "comment": """A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.""",
            "label": "Ayurvedic",
        },
        "Chiropractic": {
            "id": "schema:Chiropractic",
            "comment": """A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning.""",
            "label": "Chiropractic",
        },
        "Homeopathic": {
            "id": "schema:Homeopathic",
            "comment": """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.""",
            "label": "Homeopathic",
        },
        "Osteopathic": {
            "id": "schema:Osteopathic",
            "comment": """A system of medicine focused on promoting the body's innate ability to heal itself.""",
            "label": "Osteopathic",
        },
        "TraditionalChinese": {
            "id": "schema:TraditionalChinese",
            "comment": """A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.""",
            "label": "TraditionalChinese",
        },
        "WesternConventional": {
            "id": "schema:WesternConventional",
            "comment": """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.""",
            "label": "WesternConventional",
        },
    }