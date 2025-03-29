import enum
from typing import ClassVar, Dict, Any

class MedicalTrialDesign(str, enum.Enum):
    """Schema.org enumeration values for MedicalTrialDesign."""

    DoubleBlindedTrial = "DoubleBlindedTrial"  # "A trial design in which neither the researcher nor the pa..."
    InternationalTrial = "InternationalTrial"  # "An international trial."
    MultiCenterTrial = "MultiCenterTrial"  # "A trial that takes place at multiple centers."
    OpenTrial = "OpenTrial"  # "A trial design in which the researcher knows the full det..."
    PlaceboControlledTrial = "PlaceboControlledTrial"  # "A placebo-controlled trial design."
    RandomizedTrial = "RandomizedTrial"  # "A randomized trial design."
    SingleBlindedTrial = "SingleBlindedTrial"  # "A trial design in which the researcher knows which treatm..."
    SingleCenterTrial = "SingleCenterTrial"  # "A trial that takes place at a single center."
    TripleBlindedTrial = "TripleBlindedTrial"  # "A trial design in which neither the researcher, the perso..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "DoubleBlindedTrial": {
            "id": "schema:DoubleBlindedTrial",
            "comment": """A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.""",
            "label": "DoubleBlindedTrial",
        },
        "InternationalTrial": {
            "id": "schema:InternationalTrial",
            "comment": """An international trial.""",
            "label": "InternationalTrial",
        },
        "MultiCenterTrial": {
            "id": "schema:MultiCenterTrial",
            "comment": """A trial that takes place at multiple centers.""",
            "label": "MultiCenterTrial",
        },
        "OpenTrial": {
            "id": "schema:OpenTrial",
            "comment": """A trial design in which the researcher knows the full details of the treatment, and so does the patient.""",
            "label": "OpenTrial",
        },
        "PlaceboControlledTrial": {
            "id": "schema:PlaceboControlledTrial",
            "comment": """A placebo-controlled trial design.""",
            "label": "PlaceboControlledTrial",
        },
        "RandomizedTrial": {
            "id": "schema:RandomizedTrial",
            "comment": """A randomized trial design.""",
            "label": "RandomizedTrial",
        },
        "SingleBlindedTrial": {
            "id": "schema:SingleBlindedTrial",
            "comment": """A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.""",
            "label": "SingleBlindedTrial",
        },
        "SingleCenterTrial": {
            "id": "schema:SingleCenterTrial",
            "comment": """A trial that takes place at a single center.""",
            "label": "SingleCenterTrial",
        },
        "TripleBlindedTrial": {
            "id": "schema:TripleBlindedTrial",
            "comment": """A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.""",
            "label": "TripleBlindedTrial",
        },
    }