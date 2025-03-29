import enum
from typing import ClassVar, Dict, Any

class BodyMeasurementTypeEnumeration(str, enum.Enum):
    """Schema.org enumeration values for BodyMeasurementTypeEnumeration."""

    BodyMeasurementArm = "BodyMeasurementArm"  # "Arm length (measured between arms/shoulder line intersect..."
    BodyMeasurementBust = "BodyMeasurementBust"  # "Maximum girth of bust. Used, for example, to fit women's ..."
    BodyMeasurementChest = "BodyMeasurementChest"  # "Maximum girth of chest. Used, for example, to fit men's s..."
    BodyMeasurementFoot = "BodyMeasurementFoot"  # "Foot length (measured between end of the most prominent t..."
    BodyMeasurementHand = "BodyMeasurementHand"  # "Maximum hand girth (measured over the knuckles of the ope..."
    BodyMeasurementHead = "BodyMeasurementHead"  # "Maximum girth of head above the ears. Used, for example, ..."
    BodyMeasurementHeight = "BodyMeasurementHeight"  # "Body height (measured between crown of head and soles of ..."
    BodyMeasurementHips = "BodyMeasurementHips"  # "Girth of hips (measured around the buttocks). Used, for e..."
    BodyMeasurementInsideLeg = "BodyMeasurementInsideLeg"  # "Inside leg (measured between crotch and soles of feet). U..."
    BodyMeasurementNeck = "BodyMeasurementNeck"  # "Girth of neck. Used, for example, to fit shirts."
    BodyMeasurementUnderbust = "BodyMeasurementUnderbust"  # "Girth of body just below the bust. Used, for example, to ..."
    BodyMeasurementWaist = "BodyMeasurementWaist"  # "Girth of natural waistline (between hip bones and lower r..."
    BodyMeasurementWeight = "BodyMeasurementWeight"  # "Body weight. Used, for example, to measure pantyhose."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "BodyMeasurementArm": {
            "id": "schema:BodyMeasurementArm",
            "comment": """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.""",
            "label": "BodyMeasurementArm",
        },
        "BodyMeasurementBust": {
            "id": "schema:BodyMeasurementBust",
            "comment": """Maximum girth of bust. Used, for example, to fit women's suits.""",
            "label": "BodyMeasurementBust",
        },
        "BodyMeasurementChest": {
            "id": "schema:BodyMeasurementChest",
            "comment": """Maximum girth of chest. Used, for example, to fit men's suits.""",
            "label": "BodyMeasurementChest",
        },
        "BodyMeasurementFoot": {
            "id": "schema:BodyMeasurementFoot",
            "comment": """Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks.""",
            "label": "BodyMeasurementFoot",
        },
        "BodyMeasurementHand": {
            "id": "schema:BodyMeasurementHand",
            "comment": """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves.""",
            "label": "BodyMeasurementHand",
        },
        "BodyMeasurementHead": {
            "id": "schema:BodyMeasurementHead",
            "comment": """Maximum girth of head above the ears. Used, for example, to fit hats.""",
            "label": "BodyMeasurementHead",
        },
        "BodyMeasurementHeight": {
            "id": "schema:BodyMeasurementHeight",
            "comment": """Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.""",
            "label": "BodyMeasurementHeight",
        },
        "BodyMeasurementHips": {
            "id": "schema:BodyMeasurementHips",
            "comment": """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.""",
            "label": "BodyMeasurementHips",
        },
        "BodyMeasurementInsideLeg": {
            "id": "schema:BodyMeasurementInsideLeg",
            "comment": """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.""",
            "label": "BodyMeasurementInsideLeg",
        },
        "BodyMeasurementNeck": {
            "id": "schema:BodyMeasurementNeck",
            "comment": """Girth of neck. Used, for example, to fit shirts.""",
            "label": "BodyMeasurementNeck",
        },
        "BodyMeasurementUnderbust": {
            "id": "schema:BodyMeasurementUnderbust",
            "comment": """Girth of body just below the bust. Used, for example, to fit women's swimwear.""",
            "label": "BodyMeasurementUnderbust",
        },
        "BodyMeasurementWaist": {
            "id": "schema:BodyMeasurementWaist",
            "comment": """Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.""",
            "label": "BodyMeasurementWaist",
        },
        "BodyMeasurementWeight": {
            "id": "schema:BodyMeasurementWeight",
            "comment": """Body weight. Used, for example, to measure pantyhose.""",
            "label": "BodyMeasurementWeight",
        },
    }