import enum
from typing import ClassVar, Dict, Any

class UKNonprofitType(str, enum.Enum):
    """Schema.org enumeration values for UKNonprofitType."""

    CharitableIncorporatedOrganization = "CharitableIncorporatedOrganization"  # "CharitableIncorporatedOrganization: Non-profit type refer..."
    LimitedByGuaranteeCharity = "LimitedByGuaranteeCharity"  # "LimitedByGuaranteeCharity: Non-profit type referring to a..."
    UKTrust = "UKTrust"  # "UKTrust: Non-profit type referring to a UK trust."
    UnincorporatedAssociationCharity = "UnincorporatedAssociationCharity"  # "UnincorporatedAssociationCharity: Non-profit type referri..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CharitableIncorporatedOrganization": {
            "id": "schema:CharitableIncorporatedOrganization",
            "comment": """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK).""",
            "label": "CharitableIncorporatedOrganization",
        },
        "LimitedByGuaranteeCharity": {
            "id": "schema:LimitedByGuaranteeCharity",
            "comment": """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).""",
            "label": "LimitedByGuaranteeCharity",
        },
        "UKTrust": {
            "id": "schema:UKTrust",
            "comment": """UKTrust: Non-profit type referring to a UK trust.""",
            "label": "UKTrust",
        },
        "UnincorporatedAssociationCharity": {
            "id": "schema:UnincorporatedAssociationCharity",
            "comment": """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company that is not incorporated (UK).""",
            "label": "UnincorporatedAssociationCharity",
        },
    }