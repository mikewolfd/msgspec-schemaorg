import enum
from typing import ClassVar, Dict, Any

class PriceComponentTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for PriceComponentTypeEnumeration."""

    ActivationFee = "ActivationFee"  # "Represents the activation fee part of the total price for..."
    CleaningFee = "CleaningFee"  # "Represents the cleaning fee part of the total price for a..."
    DistanceFee = "DistanceFee"  # "Represents the distance fee (e.g., price per km or mile) ..."
    Downpayment = "Downpayment"  # "Represents the downpayment (up-front payment) price compo..."
    Installment = "Installment"  # "Represents the installment pricing component of the total..."
    Subscription = "Subscription"  # "Represents the subscription pricing component of the tota..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ActivationFee": {
            "id": "schema:ActivationFee",
            "comment": """Represents the activation fee part of the total price for an offered product, for example a cellphone contract.""",
            "label": "ActivationFee",
        },
        "CleaningFee": {
            "id": "schema:CleaningFee",
            "comment": """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.""",
            "label": "CleaningFee",
        },
        "DistanceFee": {
            "id": "schema:DistanceFee",
            "comment": """Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental.""",
            "label": "DistanceFee",
        },
        "Downpayment": {
            "id": "schema:Downpayment",
            "comment": """Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments.""",
            "label": "Downpayment",
        },
        "Installment": {
            "id": "schema:Installment",
            "comment": """Represents the installment pricing component of the total price for an offered product.""",
            "label": "Installment",
        },
        "Subscription": {
            "id": "schema:Subscription",
            "comment": """Represents the subscription pricing component of the total price for an offered product.""",
            "label": "Subscription",
        },
    }