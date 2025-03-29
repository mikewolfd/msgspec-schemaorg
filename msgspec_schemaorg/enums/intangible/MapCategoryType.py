import enum
from typing import ClassVar, Dict, Any

class MapCategoryType(str, enum.Enum):
    """Schema.org enumeration values for MapCategoryType."""

    ParkingMap = "ParkingMap"  # "A parking map."
    SeatingMap = "SeatingMap"  # "A seating map."
    TransitMap = "TransitMap"  # "A transit map."
    VenueMap = "VenueMap"  # "A venue map (e.g. for malls, auditoriums, museums, etc.)."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "ParkingMap": {
            "id": "schema:ParkingMap",
            "comment": """A parking map.""",
            "label": "ParkingMap",
        },
        "SeatingMap": {
            "id": "schema:SeatingMap",
            "comment": """A seating map.""",
            "label": "SeatingMap",
        },
        "TransitMap": {
            "id": "schema:TransitMap",
            "comment": """A transit map.""",
            "label": "TransitMap",
        },
        "VenueMap": {
            "id": "schema:VenueMap",
            "comment": """A venue map (e.g. for malls, auditoriums, museums, etc.).""",
            "label": "VenueMap",
        },
    }