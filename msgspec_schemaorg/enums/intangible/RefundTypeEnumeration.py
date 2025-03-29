import enum
from typing import ClassVar, Dict, Any

class RefundTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for RefundTypeEnumeration."""

    ExchangeRefund = "ExchangeRefund"  # "Specifies that a refund can be done as an exchange for th..."
    FullRefund = "FullRefund"  # "Specifies that a refund can be done in the full amount th..."
    StoreCreditRefund = "StoreCreditRefund"  # "Specifies that the customer receives a store credit as re..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ExchangeRefund": {
            "id": "schema:ExchangeRefund",
            "comment": """Specifies that a refund can be done as an exchange for the same product.""",
            "label": "ExchangeRefund",
        },
        "FullRefund": {
            "id": "schema:FullRefund",
            "comment": """Specifies that a refund can be done in the full amount the customer paid for the product.""",
            "label": "FullRefund",
        },
        "StoreCreditRefund": {
            "id": "schema:StoreCreditRefund",
            "comment": """Specifies that the customer receives a store credit as refund when returning a product.""",
            "label": "StoreCreditRefund",
        },
    }