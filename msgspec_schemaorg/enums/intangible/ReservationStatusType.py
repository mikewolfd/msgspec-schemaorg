import enum
from typing import ClassVar, Dict, Any

class ReservationStatusType(str, enum.Enum):
    """Schema.org enumeration values for ReservationStatusType."""

    ReservationCancelled = "ReservationCancelled"  # "The status for a previously confirmed reservation that is..."
    ReservationConfirmed = "ReservationConfirmed"  # "The status of a confirmed reservation."
    ReservationHold = "ReservationHold"  # "The status of a reservation on hold pending an update lik..."
    ReservationPending = "ReservationPending"  # "The status of a reservation when a request has been sent,..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ReservationCancelled": {
            "id": "schema:ReservationCancelled",
            "comment": """The status for a previously confirmed reservation that is now cancelled.""",
            "label": "ReservationCancelled",
        },
        "ReservationConfirmed": {
            "id": "schema:ReservationConfirmed",
            "comment": """The status of a confirmed reservation.""",
            "label": "ReservationConfirmed",
        },
        "ReservationHold": {
            "id": "schema:ReservationHold",
            "comment": """The status of a reservation on hold pending an update like credit card number or flight changes.""",
            "label": "ReservationHold",
        },
        "ReservationPending": {
            "id": "schema:ReservationPending",
            "comment": """The status of a reservation when a request has been sent, but not confirmed.""",
            "label": "ReservationPending",
        },
    }