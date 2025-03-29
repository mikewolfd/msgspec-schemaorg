import enum
from typing import ClassVar, Dict, Any

class LegalValueLevel(str, enum.Enum):
    """Schema.org enumeration values for LegalValueLevel."""

    AuthoritativeLegalValue = "AuthoritativeLegalValue"  # "Indicates that the publisher gives some special status to..."
    DefinitiveLegalValue = "DefinitiveLegalValue"  # "Indicates a document for which the text is conclusively w..."
    OfficialLegalValue = "OfficialLegalValue"  # "All the documents published by an official publisher shou..."
    UnofficialLegalValue = "UnofficialLegalValue"  # "Indicates that a document has no particular or special st..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AuthoritativeLegalValue": {
            "id": "schema:AuthoritativeLegalValue",
            "comment": """Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications). Something "Authoritative" is considered to be also [[OfficialLegalValue]]".""",
            "label": "AuthoritativeLegalValue",
        },
        "DefinitiveLegalValue": {
            "id": "schema:DefinitiveLegalValue",
            "comment": """Indicates a document for which the text is conclusively what the law says and is legally binding. (e.g. The digitally signed version of an Official Journal.)
  Something "Definitive" is considered to be also [[AuthoritativeLegalValue]].""",
            "label": "DefinitiveLegalValue",
        },
        "OfficialLegalValue": {
            "id": "schema:OfficialLegalValue",
            "comment": """All the documents published by an official publisher should have at least the legal value level "OfficialLegalValue". This indicates that the document was published by an organisation with the public task of making it available (e.g. a consolidated version of a EU directive published by the EU Office of Publications).""",
            "label": "OfficialLegalValue",
        },
        "UnofficialLegalValue": {
            "id": "schema:UnofficialLegalValue",
            "comment": """Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher).""",
            "label": "UnofficialLegalValue",
        },
    }