import enum
from typing import ClassVar, Dict, Any

class ReturnMethodEnumeration(str, enum.Enum):
    """Schema.org enumeration values for ReturnMethodEnumeration."""

    KeepProduct = "KeepProduct"  # "Specifies that the consumer can keep the product, even wh..."
    ReturnAtKiosk = "ReturnAtKiosk"  # "Specifies that product returns must be made at a kiosk."
    ReturnByMail = "ReturnByMail"  # "Specifies that product returns must be done by mail."
    ReturnInStore = "ReturnInStore"  # "Specifies that product returns must be made in a store."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "KeepProduct": {
            "id": "schema:KeepProduct",
            "comment": """Specifies that the consumer can keep the product, even when receiving a refund or store credit.""",
            "label": "KeepProduct",
        },
        "ReturnAtKiosk": {
            "id": "schema:ReturnAtKiosk",
            "comment": """Specifies that product returns must be made at a kiosk.""",
            "label": "ReturnAtKiosk",
        },
        "ReturnByMail": {
            "id": "schema:ReturnByMail",
            "comment": """Specifies that product returns must be done by mail.""",
            "label": "ReturnByMail",
        },
        "ReturnInStore": {
            "id": "schema:ReturnInStore",
            "comment": """Specifies that product returns must be made in a store.""",
            "label": "ReturnInStore",
        },
    }