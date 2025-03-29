import enum
from typing import ClassVar, Dict, Any

class HealthAspectEnumeration(str, enum.Enum):
    """Schema.org enumeration values for HealthAspectEnumeration."""

    AllergiesHealthAspect = "AllergiesHealthAspect"  # "Content about the allergy-related aspects of a health topic."
    BenefitsHealthAspect = "BenefitsHealthAspect"  # "Content about the benefits and advantages of usage or uti..."
    CausesHealthAspect = "CausesHealthAspect"  # "Information about the causes and main actions that gave r..."
    ContagiousnessHealthAspect = "ContagiousnessHealthAspect"  # "Content about contagion mechanisms and contagiousness inf..."
    EffectivenessHealthAspect = "EffectivenessHealthAspect"  # "Content about the effectiveness-related aspects of a heal..."
    GettingAccessHealthAspect = "GettingAccessHealthAspect"  # "Content that discusses practical and policy aspects for g..."
    HowItWorksHealthAspect = "HowItWorksHealthAspect"  # "Content that discusses and explains how a particular heal..."
    HowOrWhereHealthAspect = "HowOrWhereHealthAspect"  # "Information about how or where to find a topic. Also may ..."
    IngredientsHealthAspect = "IngredientsHealthAspect"  # "Content discussing ingredients-related aspects of a healt..."
    LivingWithHealthAspect = "LivingWithHealthAspect"  # "Information about coping or life related to the topic."
    MayTreatHealthAspect = "MayTreatHealthAspect"  # "Related topics may be treated by a Topic."
    MisconceptionsHealthAspect = "MisconceptionsHealthAspect"  # "Content about common misconceptions and myths that are re..."
    OverviewHealthAspect = "OverviewHealthAspect"  # "Overview of the content. Contains a summarized view of th..."
    PatientExperienceHealthAspect = "PatientExperienceHealthAspect"  # "Content about the real life experience of patients or peo..."
    PregnancyHealthAspect = "PregnancyHealthAspect"  # "Content discussing pregnancy-related aspects of a health ..."
    PreventionHealthAspect = "PreventionHealthAspect"  # "Information about actions or measures that can be taken t..."
    PrognosisHealthAspect = "PrognosisHealthAspect"  # "Typical progression and happenings of life course of the ..."
    RelatedTopicsHealthAspect = "RelatedTopicsHealthAspect"  # "Other prominent or relevant topics tied to the main topic."
    RisksOrComplicationsHealthAspect = "RisksOrComplicationsHealthAspect"  # "Information about the risk factors and possible complicat..."
    SafetyHealthAspect = "SafetyHealthAspect"  # "Content about the safety-related aspects of a health topic."
    ScreeningHealthAspect = "ScreeningHealthAspect"  # "Content about how to screen or further filter a topic."
    SeeDoctorHealthAspect = "SeeDoctorHealthAspect"  # "Information about questions that may be asked, when to se..."
    SelfCareHealthAspect = "SelfCareHealthAspect"  # "Self care actions or measures that can be taken to sooth,..."
    SideEffectsHealthAspect = "SideEffectsHealthAspect"  # "Side effects that can be observed from the usage of the t..."
    StagesHealthAspect = "StagesHealthAspect"  # "Stages that can be observed from a topic."
    SymptomsHealthAspect = "SymptomsHealthAspect"  # "Symptoms or related symptoms of a Topic."
    TreatmentsHealthAspect = "TreatmentsHealthAspect"  # "Treatments or related therapies for a Topic."
    TypesHealthAspect = "TypesHealthAspect"  # "Categorization and other types related to a topic."
    UsageOrScheduleHealthAspect = "UsageOrScheduleHealthAspect"  # "Content about how, when, frequency and dosage of a topic."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AllergiesHealthAspect": {
            "id": "schema:AllergiesHealthAspect",
            "comment": """Content about the allergy-related aspects of a health topic.""",
            "label": "AllergiesHealthAspect",
        },
        "BenefitsHealthAspect": {
            "id": "schema:BenefitsHealthAspect",
            "comment": """Content about the benefits and advantages of usage or utilization of topic.""",
            "label": "BenefitsHealthAspect",
        },
        "CausesHealthAspect": {
            "id": "schema:CausesHealthAspect",
            "comment": """Information about the causes and main actions that gave rise to the topic.""",
            "label": "CausesHealthAspect",
        },
        "ContagiousnessHealthAspect": {
            "id": "schema:ContagiousnessHealthAspect",
            "comment": """Content about contagion mechanisms and contagiousness information over the topic.""",
            "label": "ContagiousnessHealthAspect",
        },
        "EffectivenessHealthAspect": {
            "id": "schema:EffectivenessHealthAspect",
            "comment": """Content about the effectiveness-related aspects of a health topic.""",
            "label": "EffectivenessHealthAspect",
        },
        "GettingAccessHealthAspect": {
            "id": "schema:GettingAccessHealthAspect",
            "comment": """Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines).""",
            "label": "GettingAccessHealthAspect",
        },
        "HowItWorksHealthAspect": {
            "id": "schema:HowItWorksHealthAspect",
            "comment": """Content that discusses and explains how a particular health-related topic works, e.g. in terms of mechanisms and underlying science.""",
            "label": "HowItWorksHealthAspect",
        },
        "HowOrWhereHealthAspect": {
            "id": "schema:HowOrWhereHealthAspect",
            "comment": """Information about how or where to find a topic. Also may contain location data that can be used for where to look for help if the topic is observed.""",
            "label": "HowOrWhereHealthAspect",
        },
        "IngredientsHealthAspect": {
            "id": "schema:IngredientsHealthAspect",
            "comment": """Content discussing ingredients-related aspects of a health topic.""",
            "label": "IngredientsHealthAspect",
        },
        "LivingWithHealthAspect": {
            "id": "schema:LivingWithHealthAspect",
            "comment": """Information about coping or life related to the topic.""",
            "label": "LivingWithHealthAspect",
        },
        "MayTreatHealthAspect": {
            "id": "schema:MayTreatHealthAspect",
            "comment": """Related topics may be treated by a Topic.""",
            "label": "MayTreatHealthAspect",
        },
        "MisconceptionsHealthAspect": {
            "id": "schema:MisconceptionsHealthAspect",
            "comment": """Content about common misconceptions and myths that are related to a topic.""",
            "label": "MisconceptionsHealthAspect",
        },
        "OverviewHealthAspect": {
            "id": "schema:OverviewHealthAspect",
            "comment": """Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction.""",
            "label": "OverviewHealthAspect",
        },
        "PatientExperienceHealthAspect": {
            "id": "schema:PatientExperienceHealthAspect",
            "comment": """Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.""",
            "label": "PatientExperienceHealthAspect",
        },
        "PregnancyHealthAspect": {
            "id": "schema:PregnancyHealthAspect",
            "comment": """Content discussing pregnancy-related aspects of a health topic.""",
            "label": "PregnancyHealthAspect",
        },
        "PreventionHealthAspect": {
            "id": "schema:PreventionHealthAspect",
            "comment": """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.""",
            "label": "PreventionHealthAspect",
        },
        "PrognosisHealthAspect": {
            "id": "schema:PrognosisHealthAspect",
            "comment": """Typical progression and happenings of life course of the topic.""",
            "label": "PrognosisHealthAspect",
        },
        "RelatedTopicsHealthAspect": {
            "id": "schema:RelatedTopicsHealthAspect",
            "comment": """Other prominent or relevant topics tied to the main topic.""",
            "label": "RelatedTopicsHealthAspect",
        },
        "RisksOrComplicationsHealthAspect": {
            "id": "schema:RisksOrComplicationsHealthAspect",
            "comment": """Information about the risk factors and possible complications that may follow a topic.""",
            "label": "RisksOrComplicationsHealthAspect",
        },
        "SafetyHealthAspect": {
            "id": "schema:SafetyHealthAspect",
            "comment": """Content about the safety-related aspects of a health topic.""",
            "label": "SafetyHealthAspect",
        },
        "ScreeningHealthAspect": {
            "id": "schema:ScreeningHealthAspect",
            "comment": """Content about how to screen or further filter a topic.""",
            "label": "ScreeningHealthAspect",
        },
        "SeeDoctorHealthAspect": {
            "id": "schema:SeeDoctorHealthAspect",
            "comment": """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.""",
            "label": "SeeDoctorHealthAspect",
        },
        "SelfCareHealthAspect": {
            "id": "schema:SelfCareHealthAspect",
            "comment": """Self care actions or measures that can be taken to sooth, health or avoid a topic. This may be carried at home and can be carried/managed by the person itself.""",
            "label": "SelfCareHealthAspect",
        },
        "SideEffectsHealthAspect": {
            "id": "schema:SideEffectsHealthAspect",
            "comment": """Side effects that can be observed from the usage of the topic.""",
            "label": "SideEffectsHealthAspect",
        },
        "StagesHealthAspect": {
            "id": "schema:StagesHealthAspect",
            "comment": """Stages that can be observed from a topic.""",
            "label": "StagesHealthAspect",
        },
        "SymptomsHealthAspect": {
            "id": "schema:SymptomsHealthAspect",
            "comment": """Symptoms or related symptoms of a Topic.""",
            "label": "SymptomsHealthAspect",
        },
        "TreatmentsHealthAspect": {
            "id": "schema:TreatmentsHealthAspect",
            "comment": """Treatments or related therapies for a Topic.""",
            "label": "TreatmentsHealthAspect",
        },
        "TypesHealthAspect": {
            "id": "schema:TypesHealthAspect",
            "comment": """Categorization and other types related to a topic.""",
            "label": "TypesHealthAspect",
        },
        "UsageOrScheduleHealthAspect": {
            "id": "schema:UsageOrScheduleHealthAspect",
            "comment": """Content about how, when, frequency and dosage of a topic.""",
            "label": "UsageOrScheduleHealthAspect",
        },
    }