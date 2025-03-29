import enum
from typing import ClassVar, Dict, Any

class PriceTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for PriceTypeEnumeration."""

    InvoicePrice = "InvoicePrice"  # "Represents the invoice price of an offered product."
    ListPrice = "ListPrice"  # "Represents the list price of an offered product. Typicall..."
    MSRP = "MSRP"  # "Represents the manufacturer suggested retail price (\"MSRP..."
    MinimumAdvertisedPrice = "MinimumAdvertisedPrice"  # "Represents the minimum advertised price (\"MAP\") (as dicta..."
    RegularPrice = "RegularPrice"  # "Represents the regular price of an offered product. This ..."
    SRP = "SRP"  # "Represents the suggested retail price (\"SRP\") of an offer..."
    SalePrice = "SalePrice"  # "Represents a sale price (usually active for a limited per..."
    StrikethroughPrice = "StrikethroughPrice"  # "Represents the strikethrough price (the previous advertis..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "InvoicePrice": {
            "id": "schema:InvoicePrice",
            "comment": """Represents the invoice price of an offered product.""",
            "label": "InvoicePrice",
        },
        "ListPrice": {
            "id": "schema:ListPrice",
            "comment": """Represents the list price of an offered product. Typically the same as the [MSRP](https://schema.org/MSRP).""",
            "label": "ListPrice",
        },
        "MSRP": {
            "id": "schema:MSRP",
            "comment": """Represents the manufacturer suggested retail price ("MSRP") of an offered product.""",
            "label": "MSRP",
        },
        "MinimumAdvertisedPrice": {
            "id": "schema:MinimumAdvertisedPrice",
            "comment": """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.""",
            "label": "MinimumAdvertisedPrice",
        },
        "RegularPrice": {
            "id": "schema:RegularPrice",
            "comment": """Represents the regular price of an offered product. This is usually the advertised price before a temporary sale. Once the sale period ends the advertised price will go back to the regular price.""",
            "label": "RegularPrice",
        },
        "SRP": {
            "id": "schema:SRP",
            "comment": """Represents the suggested retail price ("SRP") of an offered product.""",
            "label": "SRP",
        },
        "SalePrice": {
            "id": "schema:SalePrice",
            "comment": """Represents a sale price (usually active for a limited period) of an offered product.""",
            "label": "SalePrice",
        },
        "StrikethroughPrice": {
            "id": "schema:StrikethroughPrice",
            "comment": """Represents the strikethrough price (the previous advertised price) of an offered product.""",
            "label": "StrikethroughPrice",
        },
    }