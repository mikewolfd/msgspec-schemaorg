import enum
from typing import ClassVar, Dict, Any

class EventStatusType(str, enum.Enum):
    """Schema.org enumeration values for EventStatusType."""

    EventCancelled = "EventCancelled"  # "The event has been cancelled. If the event has multiple s..."
    EventMovedOnline = "EventMovedOnline"  # "Indicates that the event was changed to allow online part..."
    EventPostponed = "EventPostponed"  # "The event has been postponed and no new date has been set..."
    EventRescheduled = "EventRescheduled"  # "The event has been rescheduled. The event's previousStart..."
    EventScheduled = "EventScheduled"  # "The event is taking place or has taken place on the start..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "EventCancelled": {
            "id": "schema:EventCancelled",
            "comment": """The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s).""",
            "label": "EventCancelled",
        },
        "EventMovedOnline": {
            "id": "schema:EventMovedOnline",
            "comment": """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.""",
            "label": "EventMovedOnline",
        },
        "EventPostponed": {
            "id": "schema:EventPostponed",
            "comment": """The event has been postponed and no new date has been set. The event's previousStartDate should be set.""",
            "label": "EventPostponed",
        },
        "EventRescheduled": {
            "id": "schema:EventRescheduled",
            "comment": """The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)""",
            "label": "EventRescheduled",
        },
        "EventScheduled": {
            "id": "schema:EventScheduled",
            "comment": """The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.""",
            "label": "EventScheduled",
        },
    }