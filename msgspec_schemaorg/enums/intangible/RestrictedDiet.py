import enum
from typing import ClassVar, Dict, Any

class RestrictedDiet(str, enum.Enum):
    """Schema.org enumeration values for RestrictedDiet."""

    DiabeticDiet = "DiabeticDiet"  # "A diet appropriate for people with diabetes."
    GlutenFreeDiet = "GlutenFreeDiet"  # "A diet exclusive of gluten."
    HalalDiet = "HalalDiet"  # "A diet conforming to Islamic dietary practices."
    HinduDiet = "HinduDiet"  # "A diet conforming to Hindu dietary practices, in particul..."
    KosherDiet = "KosherDiet"  # "A diet conforming to Jewish dietary practices."
    LowCalorieDiet = "LowCalorieDiet"  # "A diet focused on reduced calorie intake."
    LowFatDiet = "LowFatDiet"  # "A diet focused on reduced fat and cholesterol intake."
    LowLactoseDiet = "LowLactoseDiet"  # "A diet appropriate for people with lactose intolerance."
    LowSaltDiet = "LowSaltDiet"  # "A diet focused on reduced sodium intake."
    VeganDiet = "VeganDiet"  # "A diet exclusive of all animal products."
    VegetarianDiet = "VegetarianDiet"  # "A diet exclusive of animal meat."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "DiabeticDiet": {
            "id": "schema:DiabeticDiet",
            "comment": """A diet appropriate for people with diabetes.""",
            "label": "DiabeticDiet",
        },
        "GlutenFreeDiet": {
            "id": "schema:GlutenFreeDiet",
            "comment": """A diet exclusive of gluten.""",
            "label": "GlutenFreeDiet",
        },
        "HalalDiet": {
            "id": "schema:HalalDiet",
            "comment": """A diet conforming to Islamic dietary practices.""",
            "label": "HalalDiet",
        },
        "HinduDiet": {
            "id": "schema:HinduDiet",
            "comment": """A diet conforming to Hindu dietary practices, in particular, beef-free.""",
            "label": "HinduDiet",
        },
        "KosherDiet": {
            "id": "schema:KosherDiet",
            "comment": """A diet conforming to Jewish dietary practices.""",
            "label": "KosherDiet",
        },
        "LowCalorieDiet": {
            "id": "schema:LowCalorieDiet",
            "comment": """A diet focused on reduced calorie intake.""",
            "label": "LowCalorieDiet",
        },
        "LowFatDiet": {
            "id": "schema:LowFatDiet",
            "comment": """A diet focused on reduced fat and cholesterol intake.""",
            "label": "LowFatDiet",
        },
        "LowLactoseDiet": {
            "id": "schema:LowLactoseDiet",
            "comment": """A diet appropriate for people with lactose intolerance.""",
            "label": "LowLactoseDiet",
        },
        "LowSaltDiet": {
            "id": "schema:LowSaltDiet",
            "comment": """A diet focused on reduced sodium intake.""",
            "label": "LowSaltDiet",
        },
        "VeganDiet": {
            "id": "schema:VeganDiet",
            "comment": """A diet exclusive of all animal products.""",
            "label": "VeganDiet",
        },
        "VegetarianDiet": {
            "id": "schema:VegetarianDiet",
            "comment": """A diet exclusive of animal meat.""",
            "label": "VegetarianDiet",
        },
    }