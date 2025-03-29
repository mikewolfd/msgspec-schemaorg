import enum
from typing import ClassVar, Dict, Any

class IncentiveQualifiedExpenseType(str, enum.Enum):
    """Schema.org enumeration values for IncentiveQualifiedExpenseType."""

    IncentiveQualifiedExpenseTypeGoodsOnly = "IncentiveQualifiedExpenseTypeGoodsOnly"  # "This incentive applies to goods only."
    IncentiveQualifiedExpenseTypeGoodsOrServices = "IncentiveQualifiedExpenseTypeGoodsOrServices"  # "This incentive can apply to either goods or services (or ..."
    IncentiveQualifiedExpenseTypeServicesOnly = "IncentiveQualifiedExpenseTypeServicesOnly"  # "This incentive applies to services only."
    IncentiveQualifiedExpenseTypeUtilityBill = "IncentiveQualifiedExpenseTypeUtilityBill"  # "This incentive applies to utility bills."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "IncentiveQualifiedExpenseTypeGoodsOnly": {
            "id": "schema:IncentiveQualifiedExpenseTypeGoodsOnly",
            "comment": """This incentive applies to goods only.""",
            "label": "IncentiveQualifiedExpenseTypeGoodsOnly",
        },
        "IncentiveQualifiedExpenseTypeGoodsOrServices": {
            "id": "schema:IncentiveQualifiedExpenseTypeGoodsOrServices",
            "comment": """This incentive can apply to either goods or services (or both).""",
            "label": "IncentiveQualifiedExpenseTypeGoodsOrServices",
        },
        "IncentiveQualifiedExpenseTypeServicesOnly": {
            "id": "schema:IncentiveQualifiedExpenseTypeServicesOnly",
            "comment": """This incentive applies to services only.""",
            "label": "IncentiveQualifiedExpenseTypeServicesOnly",
        },
        "IncentiveQualifiedExpenseTypeUtilityBill": {
            "id": "schema:IncentiveQualifiedExpenseTypeUtilityBill",
            "comment": """This incentive applies to utility bills.""",
            "label": "IncentiveQualifiedExpenseTypeUtilityBill",
        },
    }