import enum
from typing import ClassVar, Dict, Any

class MedicalProcedureType(str, enum.Enum):
    """Schema.org enumeration values for MedicalProcedureType."""

    NoninvasiveProcedure = "NoninvasiveProcedure"  # "A type of medical procedure that involves noninvasive tec..."
    PercutaneousProcedure = "PercutaneousProcedure"  # "A type of medical procedure that involves percutaneous te..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "NoninvasiveProcedure": {
            "id": "schema:NoninvasiveProcedure",
            "comment": """A type of medical procedure that involves noninvasive techniques.""",
            "label": "NoninvasiveProcedure",
        },
        "PercutaneousProcedure": {
            "id": "schema:PercutaneousProcedure",
            "comment": """A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.""",
            "label": "PercutaneousProcedure",
        },
    }