import enum
from typing import ClassVar, Dict, Any

class MedicalDevicePurpose(str, enum.Enum):
    """Schema.org enumeration values for MedicalDevicePurpose."""

    Diagnostic = "Diagnostic"  # "A medical device used for diagnostic purposes."
    Therapeutic = "Therapeutic"  # "A medical device used for therapeutic purposes."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Diagnostic": {
            "id": "schema:Diagnostic",
            "comment": """A medical device used for diagnostic purposes.""",
            "label": "Diagnostic",
        },
        "Therapeutic": {
            "id": "schema:Therapeutic",
            "comment": """A medical device used for therapeutic purposes.""",
            "label": "Therapeutic",
        },
    }