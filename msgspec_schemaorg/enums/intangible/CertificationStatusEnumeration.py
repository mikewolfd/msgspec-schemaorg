import enum
from typing import ClassVar, Dict, Any

class CertificationStatusEnumeration(str, enum.Enum):
    """Schema.org enumeration values for CertificationStatusEnumeration."""

    CertificationActive = "CertificationActive"  # "Specifies that a certification is active."
    CertificationInactive = "CertificationInactive"  # "Specifies that a certification is inactive (no longer in ..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CertificationActive": {
            "id": "schema:CertificationActive",
            "comment": """Specifies that a certification is active.""",
            "label": "CertificationActive",
        },
        "CertificationInactive": {
            "id": "schema:CertificationInactive",
            "comment": """Specifies that a certification is inactive (no longer in effect).""",
            "label": "CertificationInactive",
        },
    }