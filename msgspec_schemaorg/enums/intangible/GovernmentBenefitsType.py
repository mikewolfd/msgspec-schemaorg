import enum
from typing import ClassVar, Dict, Any

class GovernmentBenefitsType(str, enum.Enum):
    """Schema.org enumeration values for GovernmentBenefitsType."""

    BasicIncome = "BasicIncome"  # "BasicIncome: this is a benefit for basic income."
    BusinessSupport = "BusinessSupport"  # "BusinessSupport: this is a benefit for supporting busines..."
    DisabilitySupport = "DisabilitySupport"  # "DisabilitySupport: this is a benefit for disability support."
    HealthCare = "HealthCare"  # "HealthCare: this is a benefit for health care."
    OneTimePayments = "OneTimePayments"  # "OneTimePayments: this is a benefit for one-time payments ..."
    PaidLeave = "PaidLeave"  # "PaidLeave: this is a benefit for paid leave."
    ParentalSupport = "ParentalSupport"  # "ParentalSupport: this is a benefit for parental support."
    UnemploymentSupport = "UnemploymentSupport"  # "UnemploymentSupport: this is a benefit for unemployment s..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "BasicIncome": {
            "id": "schema:BasicIncome",
            "comment": """BasicIncome: this is a benefit for basic income.""",
            "label": "BasicIncome",
        },
        "BusinessSupport": {
            "id": "schema:BusinessSupport",
            "comment": """BusinessSupport: this is a benefit for supporting businesses.""",
            "label": "BusinessSupport",
        },
        "DisabilitySupport": {
            "id": "schema:DisabilitySupport",
            "comment": """DisabilitySupport: this is a benefit for disability support.""",
            "label": "DisabilitySupport",
        },
        "HealthCare": {
            "id": "schema:HealthCare",
            "comment": """HealthCare: this is a benefit for health care.""",
            "label": "HealthCare",
        },
        "OneTimePayments": {
            "id": "schema:OneTimePayments",
            "comment": """OneTimePayments: this is a benefit for one-time payments for individuals.""",
            "label": "OneTimePayments",
        },
        "PaidLeave": {
            "id": "schema:PaidLeave",
            "comment": """PaidLeave: this is a benefit for paid leave.""",
            "label": "PaidLeave",
        },
        "ParentalSupport": {
            "id": "schema:ParentalSupport",
            "comment": """ParentalSupport: this is a benefit for parental support.""",
            "label": "ParentalSupport",
        },
        "UnemploymentSupport": {
            "id": "schema:UnemploymentSupport",
            "comment": """UnemploymentSupport: this is a benefit for unemployment support.""",
            "label": "UnemploymentSupport",
        },
    }