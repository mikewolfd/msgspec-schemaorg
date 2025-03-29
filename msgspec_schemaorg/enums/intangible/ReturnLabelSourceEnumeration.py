import enum
from typing import ClassVar, Dict, Any

class ReturnLabelSourceEnumeration(str, enum.Enum):
    """Schema.org enumeration values for ReturnLabelSourceEnumeration."""

    ReturnLabelCustomerResponsibility = "ReturnLabelCustomerResponsibility"  # "Indicated that creating a return label is the responsibil..."
    ReturnLabelDownloadAndPrint = "ReturnLabelDownloadAndPrint"  # "Indicated that a return label must be downloaded and prin..."
    ReturnLabelInBox = "ReturnLabelInBox"  # "Specifies that a return label will be provided by the sel..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ReturnLabelCustomerResponsibility": {
            "id": "schema:ReturnLabelCustomerResponsibility",
            "comment": """Indicated that creating a return label is the responsibility of the customer.""",
            "label": "ReturnLabelCustomerResponsibility",
        },
        "ReturnLabelDownloadAndPrint": {
            "id": "schema:ReturnLabelDownloadAndPrint",
            "comment": """Indicated that a return label must be downloaded and printed by the customer.""",
            "label": "ReturnLabelDownloadAndPrint",
        },
        "ReturnLabelInBox": {
            "id": "schema:ReturnLabelInBox",
            "comment": """Specifies that a return label will be provided by the seller in the shipping box.""",
            "label": "ReturnLabelInBox",
        },
    }