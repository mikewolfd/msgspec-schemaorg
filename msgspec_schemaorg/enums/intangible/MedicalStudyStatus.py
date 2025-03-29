import enum
from typing import ClassVar, Dict, Any

class MedicalStudyStatus(str, enum.Enum):
    """Schema.org enumeration values for MedicalStudyStatus."""

    ActiveNotRecruiting = "ActiveNotRecruiting"  # "Active, but not recruiting new participants."
    Completed = "Completed"  # "Completed."
    EnrollingByInvitation = "EnrollingByInvitation"  # "Enrolling participants by invitation only."
    NotYetRecruiting = "NotYetRecruiting"  # "Not yet recruiting."
    Recruiting = "Recruiting"  # "Recruiting participants."
    ResultsAvailable = "ResultsAvailable"  # "Results are available."
    ResultsNotAvailable = "ResultsNotAvailable"  # "Results are not available."
    Suspended = "Suspended"  # "Suspended."
    Terminated = "Terminated"  # "Terminated."
    Withdrawn = "Withdrawn"  # "Withdrawn."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ActiveNotRecruiting": {
            "id": "schema:ActiveNotRecruiting",
            "comment": """Active, but not recruiting new participants.""",
            "label": "ActiveNotRecruiting",
        },
        "Completed": {
            "id": "schema:Completed",
            "comment": """Completed.""",
            "label": "Completed",
        },
        "EnrollingByInvitation": {
            "id": "schema:EnrollingByInvitation",
            "comment": """Enrolling participants by invitation only.""",
            "label": "EnrollingByInvitation",
        },
        "NotYetRecruiting": {
            "id": "schema:NotYetRecruiting",
            "comment": """Not yet recruiting.""",
            "label": "NotYetRecruiting",
        },
        "Recruiting": {
            "id": "schema:Recruiting",
            "comment": """Recruiting participants.""",
            "label": "Recruiting",
        },
        "ResultsAvailable": {
            "id": "schema:ResultsAvailable",
            "comment": """Results are available.""",
            "label": "ResultsAvailable",
        },
        "ResultsNotAvailable": {
            "id": "schema:ResultsNotAvailable",
            "comment": """Results are not available.""",
            "label": "ResultsNotAvailable",
        },
        "Suspended": {
            "id": "schema:Suspended",
            "comment": """Suspended.""",
            "label": "Suspended",
        },
        "Terminated": {
            "id": "schema:Terminated",
            "comment": """Terminated.""",
            "label": "Terminated",
        },
        "Withdrawn": {
            "id": "schema:Withdrawn",
            "comment": """Withdrawn.""",
            "label": "Withdrawn",
        },
    }