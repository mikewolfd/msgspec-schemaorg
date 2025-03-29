import enum
from typing import ClassVar, Dict, Any

class AdultOrientedEnumeration(str, enum.Enum):
    """Schema.org enumeration values for AdultOrientedEnumeration."""

    AlcoholConsideration = "AlcoholConsideration"  # "Item contains alcohol or promotes alcohol consumption."
    DangerousGoodConsideration = "DangerousGoodConsideration"  # "The item is dangerous and requires careful handling and/o..."
    HealthcareConsideration = "HealthcareConsideration"  # "Item is a pharmaceutical (e.g., a prescription or OTC dru..."
    NarcoticConsideration = "NarcoticConsideration"  # "Item is a narcotic as defined by the [1961 UN convention]..."
    ReducedRelevanceForChildrenConsideration = "ReducedRelevanceForChildrenConsideration"  # "A general code for cases where relevance to children is r..."
    SexualContentConsideration = "SexualContentConsideration"  # "The item contains sexually oriented content such as nudit..."
    TobaccoNicotineConsideration = "TobaccoNicotineConsideration"  # "Item contains tobacco and/or nicotine, for example cigars..."
    UnclassifiedAdultConsideration = "UnclassifiedAdultConsideration"  # "The item is suitable only for adults, without indicating ..."
    ViolenceConsideration = "ViolenceConsideration"  # "Item shows or promotes violence."
    WeaponConsideration = "WeaponConsideration"  # "The item is intended to induce bodily harm, for example g..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AlcoholConsideration": {
            "id": "schema:AlcoholConsideration",
            "comment": """Item contains alcohol or promotes alcohol consumption.""",
            "label": "AlcoholConsideration",
        },
        "DangerousGoodConsideration": {
            "id": "schema:DangerousGoodConsideration",
            "comment": """The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf) defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more.""",
            "label": "DangerousGoodConsideration",
        },
        "HealthcareConsideration": {
            "id": "schema:HealthcareConsideration",
            "comment": """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.""",
            "label": "HealthcareConsideration",
        },
        "NarcoticConsideration": {
            "id": "schema:NarcoticConsideration",
            "comment": """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.""",
            "label": "NarcoticConsideration",
        },
        "ReducedRelevanceForChildrenConsideration": {
            "id": "schema:ReducedRelevanceForChildrenConsideration",
            "comment": """A general code for cases where relevance to children is reduced, e.g. adult education, mortgages, retirement-related products, etc.""",
            "label": "ReducedRelevanceForChildrenConsideration",
        },
        "SexualContentConsideration": {
            "id": "schema:SexualContentConsideration",
            "comment": """The item contains sexually oriented content such as nudity, suggestive or explicit material, or related online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual enhancement devices, sex toys.""",
            "label": "SexualContentConsideration",
        },
        "TobaccoNicotineConsideration": {
            "id": "schema:TobaccoNicotineConsideration",
            "comment": """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco, e-cigarettes, or hookahs.""",
            "label": "TobaccoNicotineConsideration",
        },
        "UnclassifiedAdultConsideration": {
            "id": "schema:UnclassifiedAdultConsideration",
            "comment": """The item is suitable only for adults, without indicating why. Due to widespread use of "adult" as a euphemism for "sexual", many such items are likely suited also for the SexualContentConsideration code.""",
            "label": "UnclassifiedAdultConsideration",
        },
        "ViolenceConsideration": {
            "id": "schema:ViolenceConsideration",
            "comment": """Item shows or promotes violence.""",
            "label": "ViolenceConsideration",
        },
        "WeaponConsideration": {
            "id": "schema:WeaponConsideration",
            "comment": """The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or other bombs, and spears.""",
            "label": "WeaponConsideration",
        },
    }