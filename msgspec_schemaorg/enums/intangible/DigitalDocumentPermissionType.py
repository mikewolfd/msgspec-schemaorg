import enum
from typing import ClassVar, Dict, Any

class DigitalDocumentPermissionType(str, enum.Enum):
    """Schema.org enumeration values for DigitalDocumentPermissionType."""

    CommentPermission = "CommentPermission"  # "Permission to add comments to the document."
    ReadPermission = "ReadPermission"  # "Permission to read or view the document."
    WritePermission = "WritePermission"  # "Permission to write or edit the document."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CommentPermission": {
            "id": "schema:CommentPermission",
            "comment": """Permission to add comments to the document.""",
            "label": "CommentPermission",
        },
        "ReadPermission": {
            "id": "schema:ReadPermission",
            "comment": """Permission to read or view the document.""",
            "label": "ReadPermission",
        },
        "WritePermission": {
            "id": "schema:WritePermission",
            "comment": """Permission to write or edit the document.""",
            "label": "WritePermission",
        },
    }