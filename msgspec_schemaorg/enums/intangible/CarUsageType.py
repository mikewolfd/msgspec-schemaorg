import enum
from typing import ClassVar, Dict, Any

class CarUsageType(str, enum.Enum):
    """Schema.org enumeration values for CarUsageType."""

    DrivingSchoolVehicleUsage = "DrivingSchoolVehicleUsage"  # "Indicates the usage of the vehicle for driving school."
    RentalVehicleUsage = "RentalVehicleUsage"  # "Indicates the usage of the vehicle as a rental car."
    TaxiVehicleUsage = "TaxiVehicleUsage"  # "Indicates the usage of the car as a taxi."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "DrivingSchoolVehicleUsage": {
            "id": "schema:DrivingSchoolVehicleUsage",
            "comment": """Indicates the usage of the vehicle for driving school.""",
            "label": "DrivingSchoolVehicleUsage",
        },
        "RentalVehicleUsage": {
            "id": "schema:RentalVehicleUsage",
            "comment": """Indicates the usage of the vehicle as a rental car.""",
            "label": "RentalVehicleUsage",
        },
        "TaxiVehicleUsage": {
            "id": "schema:TaxiVehicleUsage",
            "comment": """Indicates the usage of the car as a taxi.""",
            "label": "TaxiVehicleUsage",
        },
    }