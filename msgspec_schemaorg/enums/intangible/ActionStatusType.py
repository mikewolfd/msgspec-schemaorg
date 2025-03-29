import enum
from typing import ClassVar, Dict, Any

class ActionStatusType(str, enum.Enum):
    """Schema.org enumeration values for ActionStatusType."""

    ActiveActionStatus = "ActiveActionStatus"  # "An in-progress action (e.g., while watching the movie, or..."
    CompletedActionStatus = "CompletedActionStatus"  # "An action that has already taken place."
    FailedActionStatus = "FailedActionStatus"  # "An action that failed to complete. The action's error pro..."
    PotentialActionStatus = "PotentialActionStatus"  # "A description of an action that is supported."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ActiveActionStatus": {
            "id": "schema:ActiveActionStatus",
            "comment": """An in-progress action (e.g., while watching the movie, or driving to a location).""",
            "label": "ActiveActionStatus",
        },
        "CompletedActionStatus": {
            "id": "schema:CompletedActionStatus",
            "comment": """An action that has already taken place.""",
            "label": "CompletedActionStatus",
        },
        "FailedActionStatus": {
            "id": "schema:FailedActionStatus",
            "comment": """An action that failed to complete. The action's error property and the HTTP return code contain more information about the failure.""",
            "label": "FailedActionStatus",
        },
        "PotentialActionStatus": {
            "id": "schema:PotentialActionStatus",
            "comment": """A description of an action that is supported.""",
            "label": "PotentialActionStatus",
        },
    }