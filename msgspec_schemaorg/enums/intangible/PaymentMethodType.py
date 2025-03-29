import enum
from typing import ClassVar, Dict, Any

class PaymentMethodType(str, enum.Enum):
    """Schema.org enumeration values for PaymentMethodType."""

    ByBankTransferInAdvance = "ByBankTransferInAdvance"  # "Payment in advance by bank transfer, equivalent to <code>..."
    ByInvoice = "ByInvoice"  # "Payment by invoice, typically after the goods were delive..."
    COD = "COD"  # "Cash on Delivery (COD) payment, equivalent to <code>http:..."
    Cash = "Cash"  # "Payment using cash, on premises, equivalent to <code>http..."
    CheckInAdvance = "CheckInAdvance"  # "Payment in advance by sending a check, equivalent to <cod..."
    DirectDebit = "DirectDebit"  # "Payment in advance by direct debit from the bank, equival..."
    InStorePrepay = "InStorePrepay"  # "Payment in advance in some form of shop or kiosk for good..."
    PhoneCarrierPayment = "PhoneCarrierPayment"  # "Payment by billing via the phone carrier."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ByBankTransferInAdvance": {
            "id": "schema:ByBankTransferInAdvance",
            "comment": """Payment in advance by bank transfer, equivalent to <code>http://purl.org/goodrelations/v1#ByBankTransferInAdvance</code>.""",
            "label": "ByBankTransferInAdvance",
        },
        "ByInvoice": {
            "id": "schema:ByInvoice",
            "comment": """Payment by invoice, typically after the goods were delivered, equivalent to <code>http://purl.org/goodrelations/v1#ByInvoice</code>.""",
            "label": "ByInvoice",
        },
        "COD": {
            "id": "schema:COD",
            "comment": """Cash on Delivery (COD) payment, equivalent to <code>http://purl.org/goodrelations/v1#COD</code>.""",
            "label": "COD",
        },
        "Cash": {
            "id": "schema:Cash",
            "comment": """Payment using cash, on premises, equivalent to <code>http://purl.org/goodrelations/v1#Cash</code>.""",
            "label": "Cash",
        },
        "CheckInAdvance": {
            "id": "schema:CheckInAdvance",
            "comment": """Payment in advance by sending a check, equivalent to <code>http://purl.org/goodrelations/v1#CheckInAdvance</code>.""",
            "label": "CheckInAdvance",
        },
        "DirectDebit": {
            "id": "schema:DirectDebit",
            "comment": """Payment in advance by direct debit from the bank, equivalent to <code>http://purl.org/goodrelations/v1#DirectDebit</code>.""",
            "label": "DirectDebit",
        },
        "InStorePrepay": {
            "id": "schema:InStorePrepay",
            "comment": """Payment in advance in some form of shop or kiosk for goods purchased online.""",
            "label": "InStorePrepay",
        },
        "PhoneCarrierPayment": {
            "id": "schema:PhoneCarrierPayment",
            "comment": """Payment by billing via the phone carrier.""",
            "label": "PhoneCarrierPayment",
        },
    }