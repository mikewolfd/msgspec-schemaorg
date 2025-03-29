import enum
from typing import ClassVar, Dict, Any

class IncentiveType(str, enum.Enum):
    """Schema.org enumeration values for IncentiveType."""

    IncentiveTypeLoan = "IncentiveTypeLoan"  # "An incentive where the recipient can receive additional f..."
    IncentiveTypeRebateOrSubsidy = "IncentiveTypeRebateOrSubsidy"  # "An incentive that reduces the purchase/lease cost of the ..."
    IncentiveTypeTaxCredit = "IncentiveTypeTaxCredit"  # "An incentive that directly reduces the amount of tax owed..."
    IncentiveTypeTaxDeduction = "IncentiveTypeTaxDeduction"  # "An incentive that reduces the recipient's amount of taxab..."
    IncentiveTypeTaxWaiver = "IncentiveTypeTaxWaiver"  # "An incentive that reduces/exempts the recipient from taxa..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "IncentiveTypeLoan": {
            "id": "schema:IncentiveTypeLoan",
            "comment": """An incentive where the recipient can receive additional funding for the purchase/lease of the good/service, which must be paid back.""",
            "label": "IncentiveTypeLoan",
        },
        "IncentiveTypeRebateOrSubsidy": {
            "id": "schema:IncentiveTypeRebateOrSubsidy",
            "comment": """An incentive that reduces the purchase/lease cost of the good/service in question.""",
            "label": "IncentiveTypeRebateOrSubsidy",
        },
        "IncentiveTypeTaxCredit": {
            "id": "schema:IncentiveTypeTaxCredit",
            "comment": """An incentive that directly reduces the amount of tax owed by the recipient.""",
            "label": "IncentiveTypeTaxCredit",
        },
        "IncentiveTypeTaxDeduction": {
            "id": "schema:IncentiveTypeTaxDeduction",
            "comment": """An incentive that reduces the recipient's amount of taxable income.""",
            "label": "IncentiveTypeTaxDeduction",
        },
        "IncentiveTypeTaxWaiver": {
            "id": "schema:IncentiveTypeTaxWaiver",
            "comment": """An incentive that reduces/exempts the recipient from taxation applicable to the incentivized good/service (e.g. luxury taxes, registration taxes, circulation tax).""",
            "label": "IncentiveTypeTaxWaiver",
        },
    }