import enum
from typing import ClassVar, Dict, Any

class PhysicalActivityCategory(str, enum.Enum):
    """Schema.org enumeration values for PhysicalActivityCategory."""

    AerobicActivity = "AerobicActivity"  # "Physical activity of relatively low intensity that depend..."
    AnaerobicActivity = "AnaerobicActivity"  # "Physical activity that is of high-intensity which utilize..."
    Balance = "Balance"  # "Physical activity that is engaged to help maintain postur..."
    Flexibility = "Flexibility"  # "Physical activity that is engaged in to improve joint and..."
    LeisureTimeActivity = "LeisureTimeActivity"  # "Any physical activity engaged in for recreational purpose..."
    OccupationalActivity = "OccupationalActivity"  # "Any physical activity engaged in for job-related purposes..."
    StrengthTraining = "StrengthTraining"  # "Physical activity that is engaged in to improve muscle an..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AerobicActivity": {
            "id": "schema:AerobicActivity",
            "comment": """Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.""",
            "label": "AerobicActivity",
        },
        "AnaerobicActivity": {
            "id": "schema:AnaerobicActivity",
            "comment": """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.""",
            "label": "AnaerobicActivity",
        },
        "Balance": {
            "id": "schema:Balance",
            "comment": """Physical activity that is engaged to help maintain posture and balance.""",
            "label": "Balance",
        },
        "Flexibility": {
            "id": "schema:Flexibility",
            "comment": """Physical activity that is engaged in to improve joint and muscle flexibility.""",
            "label": "Flexibility",
        },
        "LeisureTimeActivity": {
            "id": "schema:LeisureTimeActivity",
            "comment": """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.""",
            "label": "LeisureTimeActivity",
        },
        "OccupationalActivity": {
            "id": "schema:OccupationalActivity",
            "comment": """Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.""",
            "label": "OccupationalActivity",
        },
        "StrengthTraining": {
            "id": "schema:StrengthTraining",
            "comment": """Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.""",
            "label": "StrengthTraining",
        },
    }