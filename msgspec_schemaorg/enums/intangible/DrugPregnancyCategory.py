import enum
from typing import ClassVar, Dict, Any

class DrugPregnancyCategory(str, enum.Enum):
    """Schema.org enumeration values for DrugPregnancyCategory."""

    FDAcategoryA = "FDAcategoryA"  # "A designation by the US FDA signifying that adequate and ..."
    FDAcategoryB = "FDAcategoryB"  # "A designation by the US FDA signifying that animal reprod..."
    FDAcategoryC = "FDAcategoryC"  # "A designation by the US FDA signifying that animal reprod..."
    FDAcategoryD = "FDAcategoryD"  # "A designation by the US FDA signifying that there is posi..."
    FDAcategoryX = "FDAcategoryX"  # "A designation by the US FDA signifying that studies in an..."
    FDAnotEvaluated = "FDAnotEvaluated"  # "A designation that the drug in question has not been assi..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "FDAcategoryA": {
            "id": "schema:FDAcategoryA",
            "comment": """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).""",
            "label": "FDAcategoryA",
        },
        "FDAcategoryB": {
            "id": "schema:FDAcategoryB",
            "comment": """A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.""",
            "label": "FDAcategoryB",
        },
        "FDAcategoryC": {
            "id": "schema:FDAcategoryC",
            "comment": """A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.""",
            "label": "FDAcategoryC",
        },
        "FDAcategoryD": {
            "id": "schema:FDAcategoryD",
            "comment": """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.""",
            "label": "FDAcategoryD",
        },
        "FDAcategoryX": {
            "id": "schema:FDAcategoryX",
            "comment": """A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.""",
            "label": "FDAcategoryX",
        },
        "FDAnotEvaluated": {
            "id": "schema:FDAnotEvaluated",
            "comment": """A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.""",
            "label": "FDAnotEvaluated",
        },
    }