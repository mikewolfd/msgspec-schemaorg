import enum
from typing import ClassVar, Dict, Any

class MerchantReturnEnumeration(str, enum.Enum):
    """Schema.org enumeration values for MerchantReturnEnumeration."""

    MerchantReturnFiniteReturnWindow = "MerchantReturnFiniteReturnWindow"  # "Specifies that there is a finite window for product returns."
    MerchantReturnNotPermitted = "MerchantReturnNotPermitted"  # "Specifies that product returns are not permitted."
    MerchantReturnUnlimitedWindow = "MerchantReturnUnlimitedWindow"  # "Specifies that there is an unlimited window for product r..."
    MerchantReturnUnspecified = "MerchantReturnUnspecified"  # "Specifies that a product return policy is not provided."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "MerchantReturnFiniteReturnWindow": {
            "id": "schema:MerchantReturnFiniteReturnWindow",
            "comment": """Specifies that there is a finite window for product returns.""",
            "label": "MerchantReturnFiniteReturnWindow",
        },
        "MerchantReturnNotPermitted": {
            "id": "schema:MerchantReturnNotPermitted",
            "comment": """Specifies that product returns are not permitted.""",
            "label": "MerchantReturnNotPermitted",
        },
        "MerchantReturnUnlimitedWindow": {
            "id": "schema:MerchantReturnUnlimitedWindow",
            "comment": """Specifies that there is an unlimited window for product returns.""",
            "label": "MerchantReturnUnlimitedWindow",
        },
        "MerchantReturnUnspecified": {
            "id": "schema:MerchantReturnUnspecified",
            "comment": """Specifies that a product return policy is not provided.""",
            "label": "MerchantReturnUnspecified",
        },
    }