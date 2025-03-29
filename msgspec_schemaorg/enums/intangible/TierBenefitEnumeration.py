import enum
from typing import ClassVar, Dict, Any

class TierBenefitEnumeration(str, enum.Enum):
    """Schema.org enumeration values for TierBenefitEnumeration."""

    TierBenefitLoyaltyPoints = "TierBenefitLoyaltyPoints"  # "Benefit of the tier is earning of loyalty points."
    TierBenefitLoyaltyPrice = "TierBenefitLoyaltyPrice"  # "Benefit of the tier is a members-only price."
    TierBenefitLoyaltyReturns = "TierBenefitLoyaltyReturns"  # "Benefit of the tier is members-only returns, for example ..."
    TierBenefitLoyaltyShipping = "TierBenefitLoyaltyShipping"  # "Benefit of the tier is a members-only shipping price or s..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "TierBenefitLoyaltyPoints": {
            "id": "schema:TierBenefitLoyaltyPoints",
            "comment": """Benefit of the tier is earning of loyalty points.""",
            "label": "TierBenefitLoyaltyPoints",
        },
        "TierBenefitLoyaltyPrice": {
            "id": "schema:TierBenefitLoyaltyPrice",
            "comment": """Benefit of the tier is a members-only price.""",
            "label": "TierBenefitLoyaltyPrice",
        },
        "TierBenefitLoyaltyReturns": {
            "id": "schema:TierBenefitLoyaltyReturns",
            "comment": """Benefit of the tier is members-only returns, for example free unlimited returns.""",
            "label": "TierBenefitLoyaltyReturns",
        },
        "TierBenefitLoyaltyShipping": {
            "id": "schema:TierBenefitLoyaltyShipping",
            "comment": """Benefit of the tier is a members-only shipping price or speed (for example free shipping or 1-day shipping).""",
            "label": "TierBenefitLoyaltyShipping",
        },
    }