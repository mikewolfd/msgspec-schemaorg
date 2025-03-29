import enum
from typing import ClassVar, Dict, Any

class PaymentStatusType(str, enum.Enum):
    """Schema.org enumeration values for PaymentStatusType."""

    PaymentAutomaticallyApplied = "PaymentAutomaticallyApplied"  # "An automatic payment system is in place and will be used."
    PaymentComplete = "PaymentComplete"  # "The payment has been received and processed."
    PaymentDeclined = "PaymentDeclined"  # "The payee received the payment, but it was declined for s..."
    PaymentDue = "PaymentDue"  # "The payment is due, but still within an acceptable time t..."
    PaymentPastDue = "PaymentPastDue"  # "The payment is due and considered late."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "PaymentAutomaticallyApplied": {
            "id": "schema:PaymentAutomaticallyApplied",
            "comment": """An automatic payment system is in place and will be used.""",
            "label": "PaymentAutomaticallyApplied",
        },
        "PaymentComplete": {
            "id": "schema:PaymentComplete",
            "comment": """The payment has been received and processed.""",
            "label": "PaymentComplete",
        },
        "PaymentDeclined": {
            "id": "schema:PaymentDeclined",
            "comment": """The payee received the payment, but it was declined for some reason.""",
            "label": "PaymentDeclined",
        },
        "PaymentDue": {
            "id": "schema:PaymentDue",
            "comment": """The payment is due, but still within an acceptable time to be received.""",
            "label": "PaymentDue",
        },
        "PaymentPastDue": {
            "id": "schema:PaymentPastDue",
            "comment": """The payment is due and considered late.""",
            "label": "PaymentPastDue",
        },
    }