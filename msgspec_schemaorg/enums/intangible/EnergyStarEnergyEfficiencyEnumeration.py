import enum
from typing import ClassVar, Dict, Any

class EnergyStarEnergyEfficiencyEnumeration(str, enum.Enum):
    """Schema.org enumeration values for EnergyStarEnergyEfficiencyEnumeration."""

    EnergyStarCertified = "EnergyStarCertified"  # "Represents EnergyStar certification."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "EnergyStarCertified": {
            "id": "schema:EnergyStarCertified",
            "comment": """Represents EnergyStar certification.""",
            "label": "EnergyStarCertified",
        },
    }