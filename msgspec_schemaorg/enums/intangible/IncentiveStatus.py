import enum
from typing import ClassVar, Dict, Any

class IncentiveStatus(str, enum.Enum):
    """Schema.org enumeration values for IncentiveStatus."""

    IncentiveStatusActive = "IncentiveStatusActive"  # "This incentive is currently active."
    IncentiveStatusInDevelopment = "IncentiveStatusInDevelopment"  # "This incentive is currently being developed, and may beco..."
    IncentiveStatusOnHold = "IncentiveStatusOnHold"  # "This incentive is currently active, but may not be accept..."
    IncentiveStatusRetired = "IncentiveStatusRetired"  # "This incentive is not longer available."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "IncentiveStatusActive": {
            "id": "schema:IncentiveStatusActive",
            "comment": """This incentive is currently active.""",
            "label": "IncentiveStatusActive",
        },
        "IncentiveStatusInDevelopment": {
            "id": "schema:IncentiveStatusInDevelopment",
            "comment": """This incentive is currently being developed, and may become active/retired in the future.""",
            "label": "IncentiveStatusInDevelopment",
        },
        "IncentiveStatusOnHold": {
            "id": "schema:IncentiveStatusOnHold",
            "comment": """This incentive is currently active, but may not be accepting new applicants (e.g. max number of redemptions reached for a year)""",
            "label": "IncentiveStatusOnHold",
        },
        "IncentiveStatusRetired": {
            "id": "schema:IncentiveStatusRetired",
            "comment": """This incentive is not longer available.""",
            "label": "IncentiveStatusRetired",
        },
    }