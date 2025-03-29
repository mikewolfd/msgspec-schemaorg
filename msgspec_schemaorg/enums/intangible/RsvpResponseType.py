import enum
from typing import ClassVar, Dict, Any

class RsvpResponseType(str, enum.Enum):
    """Schema.org enumeration values for RsvpResponseType."""

    RsvpResponseMaybe = "RsvpResponseMaybe"  # "The invitee may or may not attend."
    RsvpResponseNo = "RsvpResponseNo"  # "The invitee will not attend."
    RsvpResponseYes = "RsvpResponseYes"  # "The invitee will attend."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "RsvpResponseMaybe": {
            "id": "schema:RsvpResponseMaybe",
            "comment": """The invitee may or may not attend.""",
            "label": "RsvpResponseMaybe",
        },
        "RsvpResponseNo": {
            "id": "schema:RsvpResponseNo",
            "comment": """The invitee will not attend.""",
            "label": "RsvpResponseNo",
        },
        "RsvpResponseYes": {
            "id": "schema:RsvpResponseYes",
            "comment": """The invitee will attend.""",
            "label": "RsvpResponseYes",
        },
    }