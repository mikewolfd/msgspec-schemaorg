import enum
from typing import ClassVar, Dict, Any

class MusicReleaseFormatType(str, enum.Enum):
    """Schema.org enumeration values for MusicReleaseFormatType."""

    CDFormat = "CDFormat"  # "CDFormat."
    CassetteFormat = "CassetteFormat"  # "CassetteFormat."
    DVDFormat = "DVDFormat"  # "DVDFormat."
    DigitalAudioTapeFormat = "DigitalAudioTapeFormat"  # "DigitalAudioTapeFormat."
    DigitalFormat = "DigitalFormat"  # "DigitalFormat."
    LaserDiscFormat = "LaserDiscFormat"  # "LaserDiscFormat."
    VinylFormat = "VinylFormat"  # "VinylFormat."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CDFormat": {
            "id": "schema:CDFormat",
            "comment": """CDFormat.""",
            "label": "CDFormat",
        },
        "CassetteFormat": {
            "id": "schema:CassetteFormat",
            "comment": """CassetteFormat.""",
            "label": "CassetteFormat",
        },
        "DVDFormat": {
            "id": "schema:DVDFormat",
            "comment": """DVDFormat.""",
            "label": "DVDFormat",
        },
        "DigitalAudioTapeFormat": {
            "id": "schema:DigitalAudioTapeFormat",
            "comment": """DigitalAudioTapeFormat.""",
            "label": "DigitalAudioTapeFormat",
        },
        "DigitalFormat": {
            "id": "schema:DigitalFormat",
            "comment": """DigitalFormat.""",
            "label": "DigitalFormat",
        },
        "LaserDiscFormat": {
            "id": "schema:LaserDiscFormat",
            "comment": """LaserDiscFormat.""",
            "label": "LaserDiscFormat",
        },
        "VinylFormat": {
            "id": "schema:VinylFormat",
            "comment": """VinylFormat.""",
            "label": "VinylFormat",
        },
    }