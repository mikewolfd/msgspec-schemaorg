import enum
from typing import ClassVar, Dict, Any

class ReturnFeesEnumeration(str, enum.Enum):
    """Schema.org enumeration values for ReturnFeesEnumeration."""

    FreeReturn = "FreeReturn"  # "Specifies that product returns are free of charge for the..."
    OriginalShippingFees = "OriginalShippingFees"  # "Specifies that the customer must pay the original shippin..."
    RestockingFees = "RestockingFees"  # "Specifies that the customer must pay a restocking fee whe..."
    ReturnFeesCustomerResponsibility = "ReturnFeesCustomerResponsibility"  # "Specifies that product returns must be paid for, and are ..."
    ReturnShippingFees = "ReturnShippingFees"  # "Specifies that the customer must pay the return shipping ..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "FreeReturn": {
            "id": "schema:FreeReturn",
            "comment": """Specifies that product returns are free of charge for the customer.""",
            "label": "FreeReturn",
        },
        "OriginalShippingFees": {
            "id": "schema:OriginalShippingFees",
            "comment": """Specifies that the customer must pay the original shipping costs when returning a product.""",
            "label": "OriginalShippingFees",
        },
        "RestockingFees": {
            "id": "schema:RestockingFees",
            "comment": """Specifies that the customer must pay a restocking fee when returning a product.""",
            "label": "RestockingFees",
        },
        "ReturnFeesCustomerResponsibility": {
            "id": "schema:ReturnFeesCustomerResponsibility",
            "comment": """Specifies that product returns must be paid for, and are the responsibility of, the customer.""",
            "label": "ReturnFeesCustomerResponsibility",
        },
        "ReturnShippingFees": {
            "id": "schema:ReturnShippingFees",
            "comment": """Specifies that the customer must pay the return shipping costs when returning a product.""",
            "label": "ReturnShippingFees",
        },
    }