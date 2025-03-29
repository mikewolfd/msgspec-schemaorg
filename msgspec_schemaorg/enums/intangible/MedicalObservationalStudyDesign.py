import enum
from typing import ClassVar, Dict, Any

class MedicalObservationalStudyDesign(str, enum.Enum):
    """Schema.org enumeration values for MedicalObservationalStudyDesign."""

    CaseSeries = "CaseSeries"  # "A case series (also known as a clinical series) is a medi..."
    CohortStudy = "CohortStudy"  # "Also known as a panel study. A cohort study is a form of ..."
    CrossSectional = "CrossSectional"  # "Studies carried out on pre-existing data (usually from 's..."
    Longitudinal = "Longitudinal"  # "Unlike cross-sectional studies, longitudinal studies trac..."
    Observational = "Observational"  # "An observational study design."
    Registry = "Registry"  # "A registry-based study design."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CaseSeries": {
            "id": "schema:CaseSeries",
            "comment": """A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.""",
            "label": "CaseSeries",
        },
        "CohortStudy": {
            "id": "schema:CohortStudy",
            "comment": """Also known as a panel study. A cohort study is a form of longitudinal study used in medicine and social science. It is one type of study design and should be compared with a cross-sectional study.  A cohort is a group of people who share a common characteristic or experience within a defined period (e.g., are born, leave school, lose their job, are exposed to a drug or a vaccine, etc.). The comparison group may be the general population from which the cohort is drawn, or it may be another cohort of persons thought to have had little or no exposure to the substance under investigation, but otherwise similar. Alternatively, subgroups within the cohort may be compared with each other.""",
            "label": "CohortStudy",
        },
        "CrossSectional": {
            "id": "schema:CrossSectional",
            "comment": """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.""",
            "label": "CrossSectional",
        },
        "Longitudinal": {
            "id": "schema:Longitudinal",
            "comment": """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.""",
            "label": "Longitudinal",
        },
        "Observational": {
            "id": "schema:Observational",
            "comment": """An observational study design.""",
            "label": "Observational",
        },
        "Registry": {
            "id": "schema:Registry",
            "comment": """A registry-based study design.""",
            "label": "Registry",
        },
    }