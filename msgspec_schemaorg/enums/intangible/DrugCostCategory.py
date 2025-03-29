import enum
from typing import ClassVar, Dict, Any

class DrugCostCategory(str, enum.Enum):
    """Schema.org enumeration values for DrugCostCategory."""

    ReimbursementCap = "ReimbursementCap"  # "The drug's cost represents the maximum reimbursement paid..."
    Retail = "Retail"  # "The drug's cost represents the retail cost of the drug."
    Wholesale = "Wholesale"  # "The drug's cost represents the wholesale acquisition cost..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ReimbursementCap": {
            "id": "schema:ReimbursementCap",
            "comment": """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.""",
            "label": "ReimbursementCap",
        },
        "Retail": {
            "id": "schema:Retail",
            "comment": """The drug's cost represents the retail cost of the drug.""",
            "label": "Retail",
        },
        "Wholesale": {
            "id": "schema:Wholesale",
            "comment": """The drug's cost represents the wholesale acquisition cost of the drug.""",
            "label": "Wholesale",
        },
    }