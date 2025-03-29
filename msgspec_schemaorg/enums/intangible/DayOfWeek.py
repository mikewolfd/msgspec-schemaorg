import enum
from typing import ClassVar, Dict, Any

class DayOfWeek(str, enum.Enum):
    """Schema.org enumeration values for DayOfWeek."""

    Friday = "Friday"  # "The day of the week between Thursday and Saturday."
    Monday = "Monday"  # "The day of the week between Sunday and Tuesday."
    PublicHolidays = "PublicHolidays"  # "This stands for any day that is a public holiday; it is a..."
    Saturday = "Saturday"  # "The day of the week between Friday and Sunday."
    Sunday = "Sunday"  # "The day of the week between Saturday and Monday."
    Thursday = "Thursday"  # "The day of the week between Wednesday and Friday."
    Tuesday = "Tuesday"  # "The day of the week between Monday and Wednesday."
    Wednesday = "Wednesday"  # "The day of the week between Tuesday and Thursday."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Friday": {
            "id": "schema:Friday",
            "comment": """The day of the week between Thursday and Saturday.""",
            "label": "Friday",
        },
        "Monday": {
            "id": "schema:Monday",
            "comment": """The day of the week between Sunday and Tuesday.""",
            "label": "Monday",
        },
        "PublicHolidays": {
            "id": "schema:PublicHolidays",
            "comment": """This stands for any day that is a public holiday; it is a placeholder for all official public holidays in some particular location. While not technically a "day of the week", it can be used with [[OpeningHoursSpecification]]. In the context of an opening hours specification it can be used to indicate opening hours on public holidays, overriding general opening hours for the day of the week on which a public holiday occurs.""",
            "label": "PublicHolidays",
        },
        "Saturday": {
            "id": "schema:Saturday",
            "comment": """The day of the week between Friday and Sunday.""",
            "label": "Saturday",
        },
        "Sunday": {
            "id": "schema:Sunday",
            "comment": """The day of the week between Saturday and Monday.""",
            "label": "Sunday",
        },
        "Thursday": {
            "id": "schema:Thursday",
            "comment": """The day of the week between Wednesday and Friday.""",
            "label": "Thursday",
        },
        "Tuesday": {
            "id": "schema:Tuesday",
            "comment": """The day of the week between Monday and Wednesday.""",
            "label": "Tuesday",
        },
        "Wednesday": {
            "id": "schema:Wednesday",
            "comment": """The day of the week between Tuesday and Thursday.""",
            "label": "Wednesday",
        },
    }