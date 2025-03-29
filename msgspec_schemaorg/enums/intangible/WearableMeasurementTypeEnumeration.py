import enum
from typing import ClassVar, Dict, Any

class WearableMeasurementTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for WearableMeasurementTypeEnumeration."""

    WearableMeasurementBack = "WearableMeasurementBack"  # "Measurement of the back section, for example of a jacket."
    WearableMeasurementChestOrBust = "WearableMeasurementChestOrBust"  # "Measurement of the chest/bust section, for example of a s..."
    WearableMeasurementCollar = "WearableMeasurementCollar"  # "Measurement of the collar, for example of a shirt."
    WearableMeasurementCup = "WearableMeasurementCup"  # "Measurement of the cup, for example of a bra."
    WearableMeasurementHeight = "WearableMeasurementHeight"  # "Measurement of the height, for example the heel height of..."
    WearableMeasurementHips = "WearableMeasurementHips"  # "Measurement of the hip section, for example of a skirt."
    WearableMeasurementInseam = "WearableMeasurementInseam"  # "Measurement of the inseam, for example of pants."
    WearableMeasurementLength = "WearableMeasurementLength"  # "Represents the length, for example of a dress."
    WearableMeasurementOutsideLeg = "WearableMeasurementOutsideLeg"  # "Measurement of the outside leg, for example of pants."
    WearableMeasurementSleeve = "WearableMeasurementSleeve"  # "Measurement of the sleeve length, for example of a shirt."
    WearableMeasurementWaist = "WearableMeasurementWaist"  # "Measurement of the waist section, for example of pants."
    WearableMeasurementWidth = "WearableMeasurementWidth"  # "Measurement of the width, for example of shoes."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "WearableMeasurementBack": {
            "id": "schema:WearableMeasurementBack",
            "comment": """Measurement of the back section, for example of a jacket.""",
            "label": "WearableMeasurementBack",
        },
        "WearableMeasurementChestOrBust": {
            "id": "schema:WearableMeasurementChestOrBust",
            "comment": """Measurement of the chest/bust section, for example of a suit.""",
            "label": "WearableMeasurementChestOrBust",
        },
        "WearableMeasurementCollar": {
            "id": "schema:WearableMeasurementCollar",
            "comment": """Measurement of the collar, for example of a shirt.""",
            "label": "WearableMeasurementCollar",
        },
        "WearableMeasurementCup": {
            "id": "schema:WearableMeasurementCup",
            "comment": """Measurement of the cup, for example of a bra.""",
            "label": "WearableMeasurementCup",
        },
        "WearableMeasurementHeight": {
            "id": "schema:WearableMeasurementHeight",
            "comment": """Measurement of the height, for example the heel height of a shoe.""",
            "label": "WearableMeasurementHeight",
        },
        "WearableMeasurementHips": {
            "id": "schema:WearableMeasurementHips",
            "comment": """Measurement of the hip section, for example of a skirt.""",
            "label": "WearableMeasurementHips",
        },
        "WearableMeasurementInseam": {
            "id": "schema:WearableMeasurementInseam",
            "comment": """Measurement of the inseam, for example of pants.""",
            "label": "WearableMeasurementInseam",
        },
        "WearableMeasurementLength": {
            "id": "schema:WearableMeasurementLength",
            "comment": """Represents the length, for example of a dress.""",
            "label": "WearableMeasurementLength",
        },
        "WearableMeasurementOutsideLeg": {
            "id": "schema:WearableMeasurementOutsideLeg",
            "comment": """Measurement of the outside leg, for example of pants.""",
            "label": "WearableMeasurementOutsideLeg",
        },
        "WearableMeasurementSleeve": {
            "id": "schema:WearableMeasurementSleeve",
            "comment": """Measurement of the sleeve length, for example of a shirt.""",
            "label": "WearableMeasurementSleeve",
        },
        "WearableMeasurementWaist": {
            "id": "schema:WearableMeasurementWaist",
            "comment": """Measurement of the waist section, for example of pants.""",
            "label": "WearableMeasurementWaist",
        },
        "WearableMeasurementWidth": {
            "id": "schema:WearableMeasurementWidth",
            "comment": """Measurement of the width, for example of shoes.""",
            "label": "WearableMeasurementWidth",
        },
    }