import enum
from typing import ClassVar, Dict, Any

class EventAttendanceModeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for EventAttendanceModeEnumeration."""

    MixedEventAttendanceMode = "MixedEventAttendanceMode"  # "MixedEventAttendanceMode - an event that is conducted as ..."
    OfflineEventAttendanceMode = "OfflineEventAttendanceMode"  # "OfflineEventAttendanceMode - an event that is primarily c..."
    OnlineEventAttendanceMode = "OnlineEventAttendanceMode"  # "OnlineEventAttendanceMode - an event that is primarily co..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "MixedEventAttendanceMode": {
            "id": "schema:MixedEventAttendanceMode",
            "comment": """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.""",
            "label": "MixedEventAttendanceMode",
        },
        "OfflineEventAttendanceMode": {
            "id": "schema:OfflineEventAttendanceMode",
            "comment": """OfflineEventAttendanceMode - an event that is primarily conducted offline. """,
            "label": "OfflineEventAttendanceMode",
        },
        "OnlineEventAttendanceMode": {
            "id": "schema:OnlineEventAttendanceMode",
            "comment": """OnlineEventAttendanceMode - an event that is primarily conducted online. """,
            "label": "OnlineEventAttendanceMode",
        },
    }