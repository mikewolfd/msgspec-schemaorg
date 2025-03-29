import enum
from typing import ClassVar, Dict, Any

class MusicAlbumReleaseType(str, enum.Enum):
    """Schema.org enumeration values for MusicAlbumReleaseType."""

    AlbumRelease = "AlbumRelease"  # "AlbumRelease."
    BroadcastRelease = "BroadcastRelease"  # "BroadcastRelease."
    EPRelease = "EPRelease"  # "EPRelease."
    SingleRelease = "SingleRelease"  # "SingleRelease."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AlbumRelease": {
            "id": "schema:AlbumRelease",
            "comment": """AlbumRelease.""",
            "label": "AlbumRelease",
        },
        "BroadcastRelease": {
            "id": "schema:BroadcastRelease",
            "comment": """BroadcastRelease.""",
            "label": "BroadcastRelease",
        },
        "EPRelease": {
            "id": "schema:EPRelease",
            "comment": """EPRelease.""",
            "label": "EPRelease",
        },
        "SingleRelease": {
            "id": "schema:SingleRelease",
            "comment": """SingleRelease.""",
            "label": "SingleRelease",
        },
    }