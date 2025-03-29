import enum
from typing import ClassVar, Dict, Any

class NLNonprofitType(str, enum.Enum):
    """Schema.org enumeration values for NLNonprofitType."""

    NonprofitANBI = "NonprofitANBI"  # "NonprofitANBI: Non-profit type referring to a Public Bene..."
    NonprofitSBBI = "NonprofitSBBI"  # "NonprofitSBBI: Non-profit type referring to a Social Inte..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "NonprofitANBI": {
            "id": "schema:NonprofitANBI",
            "comment": """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).""",
            "label": "NonprofitANBI",
        },
        "NonprofitSBBI": {
            "id": "schema:NonprofitSBBI",
            "comment": """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).""",
            "label": "NonprofitSBBI",
        },
    }