import enum
from typing import ClassVar, Dict, Any

class GameServerStatus(str, enum.Enum):
    """Schema.org enumeration values for GameServerStatus."""

    OfflinePermanently = "OfflinePermanently"  # "Game server status: OfflinePermanently. Server is offline..."
    OfflineTemporarily = "OfflineTemporarily"  # "Game server status: OfflineTemporarily. Server is offline..."
    Online = "Online"  # "Game server status: Online. Server is available."
    OnlineFull = "OnlineFull"  # "Game server status: OnlineFull. Server is online but unav..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "OfflinePermanently": {
            "id": "schema:OfflinePermanently",
            "comment": """Game server status: OfflinePermanently. Server is offline and not available.""",
            "label": "OfflinePermanently",
        },
        "OfflineTemporarily": {
            "id": "schema:OfflineTemporarily",
            "comment": """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.""",
            "label": "OfflineTemporarily",
        },
        "Online": {
            "id": "schema:Online",
            "comment": """Game server status: Online. Server is available.""",
            "label": "Online",
        },
        "OnlineFull": {
            "id": "schema:OnlineFull",
            "comment": """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.""",
            "label": "OnlineFull",
        },
    }