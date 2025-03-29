import enum
from typing import ClassVar, Dict, Any

class MedicalSpecialty(str, enum.Enum):
    """Schema.org enumeration values for MedicalSpecialty."""

    Anesthesia = "Anesthesia"  # "A specific branch of medical science that pertains to stu..."
    Cardiovascular = "Cardiovascular"  # "A specific branch of medical science that pertains to dia..."
    CommunityHealth = "CommunityHealth"  # "A field of public health focusing on improving health cha..."
    Dentistry = "Dentistry"  # "A branch of medicine that is involved in the dental care."
    Dermatologic = "Dermatologic"  # "Something relating to or practicing dermatology."
    Dermatology = "Dermatology"  # "A specific branch of medical science that pertains to dia..."
    DietNutrition = "DietNutrition"  # "Dietetics and nutrition as a medical specialty."
    Emergency = "Emergency"  # "A specific branch of medical science that deals with the ..."
    Endocrine = "Endocrine"  # "A specific branch of medical science that pertains to dia..."
    Gastroenterologic = "Gastroenterologic"  # "A specific branch of medical science that pertains to dia..."
    Genetic = "Genetic"  # "A specific branch of medical science that pertains to her..."
    Geriatric = "Geriatric"  # "A specific branch of medical science that is concerned wi..."
    Gynecologic = "Gynecologic"  # "A specific branch of medical science that pertains to the..."
    Hematologic = "Hematologic"  # "A specific branch of medical science that pertains to dia..."
    Infectious = "Infectious"  # "Something in medical science that pertains to infectious ..."
    LaboratoryScience = "LaboratoryScience"  # "A medical science pertaining to chemical, hematological, ..."
    Midwifery = "Midwifery"  # "A nurse-like health profession that deals with pregnancy,..."
    Musculoskeletal = "Musculoskeletal"  # "A specific branch of medical science that pertains to dia..."
    Neurologic = "Neurologic"  # "A specific branch of medical science that studies the ner..."
    Nursing = "Nursing"  # "A health profession of a person formally educated and tra..."
    Obstetric = "Obstetric"  # "A specific branch of medical science that specializes in ..."
    Oncologic = "Oncologic"  # "A specific branch of medical science that deals with beni..."
    Optometric = "Optometric"  # "The science or practice of testing visual acuity and pres..."
    Otolaryngologic = "Otolaryngologic"  # "A specific branch of medical science that is concerned wi..."
    Pathology = "Pathology"  # "A specific branch of medical science that is concerned wi..."
    Pediatric = "Pediatric"  # "A specific branch of medical science that specializes in ..."
    PharmacySpecialty = "PharmacySpecialty"  # "The practice or art and science of preparing and dispensi..."
    Physiotherapy = "Physiotherapy"  # "The practice of treatment of disease, injury, or deformit..."
    PlasticSurgery = "PlasticSurgery"  # "A specific branch of medical science that pertains to the..."
    Podiatric = "Podiatric"  # "Podiatry is the care of the human foot, especially the di..."
    PrimaryCare = "PrimaryCare"  # "The medical care by a physician, or other health-care pro..."
    Psychiatric = "Psychiatric"  # "A specific branch of medical science that is concerned wi..."
    PublicHealth = "PublicHealth"  # "Branch of medicine that pertains to the health services t..."
    Pulmonary = "Pulmonary"  # "A specific branch of medical science that pertains to the..."
    Radiography = "Radiography"  # "Radiography is an imaging technique that uses electromagn..."
    Renal = "Renal"  # "A specific branch of medical science that pertains to the..."
    RespiratoryTherapy = "RespiratoryTherapy"  # "The therapy that is concerned with the maintenance or imp..."
    Rheumatologic = "Rheumatologic"  # "A specific branch of medical science that deals with the ..."
    SpeechPathology = "SpeechPathology"  # "The scientific study and treatment of defects, disorders,..."
    Surgical = "Surgical"  # "A specific branch of medical science that pertains to tre..."
    Toxicologic = "Toxicologic"  # "A specific branch of medical science that is concerned wi..."
    Urologic = "Urologic"  # "A specific branch of medical science that is concerned wi..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "Anesthesia": {
            "id": "schema:Anesthesia",
            "comment": """A specific branch of medical science that pertains to study of anesthetics and their application.""",
            "label": "Anesthesia",
        },
        "Cardiovascular": {
            "id": "schema:Cardiovascular",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.""",
            "label": "Cardiovascular",
        },
        "CommunityHealth": {
            "id": "schema:CommunityHealth",
            "comment": """A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas.""",
            "label": "CommunityHealth",
        },
        "Dentistry": {
            "id": "schema:Dentistry",
            "comment": """A branch of medicine that is involved in the dental care.""",
            "label": "Dentistry",
        },
        "Dermatologic": {
            "id": "schema:Dermatologic",
            "comment": """Something relating to or practicing dermatology.""",
            "label": "Dermatologic",
        },
        "Dermatology": {
            "id": "schema:Dermatology",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.""",
            "label": "Dermatology",
        },
        "DietNutrition": {
            "id": "schema:DietNutrition",
            "comment": """Dietetics and nutrition as a medical specialty.""",
            "label": "DietNutrition",
        },
        "Emergency": {
            "id": "schema:Emergency",
            "comment": """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.""",
            "label": "Emergency",
        },
        "Endocrine": {
            "id": "schema:Endocrine",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.""",
            "label": "Endocrine",
        },
        "Gastroenterologic": {
            "id": "schema:Gastroenterologic",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.""",
            "label": "Gastroenterologic",
        },
        "Genetic": {
            "id": "schema:Genetic",
            "comment": """A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.""",
            "label": "Genetic",
        },
        "Geriatric": {
            "id": "schema:Geriatric",
            "comment": """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.""",
            "label": "Geriatric",
        },
        "Gynecologic": {
            "id": "schema:Gynecologic",
            "comment": """A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.""",
            "label": "Gynecologic",
        },
        "Hematologic": {
            "id": "schema:Hematologic",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.""",
            "label": "Hematologic",
        },
        "Infectious": {
            "id": "schema:Infectious",
            "comment": """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.""",
            "label": "Infectious",
        },
        "LaboratoryScience": {
            "id": "schema:LaboratoryScience",
            "comment": """A medical science pertaining to chemical, hematological, immunologic, microscopic, or bacteriological diagnostic analyses or research.""",
            "label": "LaboratoryScience",
        },
        "Midwifery": {
            "id": "schema:Midwifery",
            "comment": """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.""",
            "label": "Midwifery",
        },
        "Musculoskeletal": {
            "id": "schema:Musculoskeletal",
            "comment": """A specific branch of medical science that pertains to diagnosis and treatment of disorders of muscles, ligaments and skeletal system.""",
            "label": "Musculoskeletal",
        },
        "Neurologic": {
            "id": "schema:Neurologic",
            "comment": """A specific branch of medical science that studies the nerves and nervous system and its respective disease states.""",
            "label": "Neurologic",
        },
        "Nursing": {
            "id": "schema:Nursing",
            "comment": """A health profession of a person formally educated and trained in the care of the sick or infirm person.""",
            "label": "Nursing",
        },
        "Obstetric": {
            "id": "schema:Obstetric",
            "comment": """A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.""",
            "label": "Obstetric",
        },
        "Oncologic": {
            "id": "schema:Oncologic",
            "comment": """A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.""",
            "label": "Oncologic",
        },
        "Optometric": {
            "id": "schema:Optometric",
            "comment": """The science or practice of testing visual acuity and prescribing corrective lenses.""",
            "label": "Optometric",
        },
        "Otolaryngologic": {
            "id": "schema:Otolaryngologic",
            "comment": """A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.""",
            "label": "Otolaryngologic",
        },
        "Pathology": {
            "id": "schema:Pathology",
            "comment": """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.""",
            "label": "Pathology",
        },
        "Pediatric": {
            "id": "schema:Pediatric",
            "comment": """A specific branch of medical science that specializes in the care of infants, children and adolescents.""",
            "label": "Pediatric",
        },
        "PharmacySpecialty": {
            "id": "schema:PharmacySpecialty",
            "comment": """The practice or art and science of preparing and dispensing drugs and medicines.""",
            "label": "PharmacySpecialty",
        },
        "Physiotherapy": {
            "id": "schema:Physiotherapy",
            "comment": """The practice of treatment of disease, injury, or deformity by physical methods such as massage, heat treatment, and exercise rather than by drugs or surgery.""",
            "label": "Physiotherapy",
        },
        "PlasticSurgery": {
            "id": "schema:PlasticSurgery",
            "comment": """A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.""",
            "label": "PlasticSurgery",
        },
        "Podiatric": {
            "id": "schema:Podiatric",
            "comment": """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.""",
            "label": "Podiatric",
        },
        "PrimaryCare": {
            "id": "schema:PrimaryCare",
            "comment": """The medical care by a physician, or other health-care professional, who is the patient's first contact with the health-care system and who may recommend a specialist if necessary.""",
            "label": "PrimaryCare",
        },
        "Psychiatric": {
            "id": "schema:Psychiatric",
            "comment": """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.""",
            "label": "Psychiatric",
        },
        "PublicHealth": {
            "id": "schema:PublicHealth",
            "comment": """Branch of medicine that pertains to the health services to improve and protect community health, especially epidemiology, sanitation, immunization, and preventive medicine.""",
            "label": "PublicHealth",
        },
        "Pulmonary": {
            "id": "schema:Pulmonary",
            "comment": """A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.""",
            "label": "Pulmonary",
        },
        "Radiography": {
            "id": "schema:Radiography",
            "comment": """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.""",
            "label": "Radiography",
        },
        "Renal": {
            "id": "schema:Renal",
            "comment": """A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.""",
            "label": "Renal",
        },
        "RespiratoryTherapy": {
            "id": "schema:RespiratoryTherapy",
            "comment": """The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease).""",
            "label": "RespiratoryTherapy",
        },
        "Rheumatologic": {
            "id": "schema:Rheumatologic",
            "comment": """A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.""",
            "label": "Rheumatologic",
        },
        "SpeechPathology": {
            "id": "schema:SpeechPathology",
            "comment": """The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition.""",
            "label": "SpeechPathology",
        },
        "Surgical": {
            "id": "schema:Surgical",
            "comment": """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.""",
            "label": "Surgical",
        },
        "Toxicologic": {
            "id": "schema:Toxicologic",
            "comment": """A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.""",
            "label": "Toxicologic",
        },
        "Urologic": {
            "id": "schema:Urologic",
            "comment": """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.""",
            "label": "Urologic",
        },
    }