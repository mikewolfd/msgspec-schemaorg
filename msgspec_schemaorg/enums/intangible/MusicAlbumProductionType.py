import enum
from typing import ClassVar, Dict, Any

class MusicAlbumProductionType(str, enum.Enum):
    """Schema.org enumeration values for MusicAlbumProductionType."""

    CompilationAlbum = "CompilationAlbum"  # "CompilationAlbum."
    DJMixAlbum = "DJMixAlbum"  # "DJMixAlbum."
    DemoAlbum = "DemoAlbum"  # "DemoAlbum."
    LiveAlbum = "LiveAlbum"  # "LiveAlbum."
    MixtapeAlbum = "MixtapeAlbum"  # "MixtapeAlbum."
    RemixAlbum = "RemixAlbum"  # "RemixAlbum."
    SoundtrackAlbum = "SoundtrackAlbum"  # "SoundtrackAlbum."
    SpokenWordAlbum = "SpokenWordAlbum"  # "SpokenWordAlbum."
    StudioAlbum = "StudioAlbum"  # "StudioAlbum."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CompilationAlbum": {
            "id": "schema:CompilationAlbum",
            "comment": """CompilationAlbum.""",
            "label": "CompilationAlbum",
        },
        "DJMixAlbum": {
            "id": "schema:DJMixAlbum",
            "comment": """DJMixAlbum.""",
            "label": "DJMixAlbum",
        },
        "DemoAlbum": {
            "id": "schema:DemoAlbum",
            "comment": """DemoAlbum.""",
            "label": "DemoAlbum",
        },
        "LiveAlbum": {
            "id": "schema:LiveAlbum",
            "comment": """LiveAlbum.""",
            "label": "LiveAlbum",
        },
        "MixtapeAlbum": {
            "id": "schema:MixtapeAlbum",
            "comment": """MixtapeAlbum.""",
            "label": "MixtapeAlbum",
        },
        "RemixAlbum": {
            "id": "schema:RemixAlbum",
            "comment": """RemixAlbum.""",
            "label": "RemixAlbum",
        },
        "SoundtrackAlbum": {
            "id": "schema:SoundtrackAlbum",
            "comment": """SoundtrackAlbum.""",
            "label": "SoundtrackAlbum",
        },
        "SpokenWordAlbum": {
            "id": "schema:SpokenWordAlbum",
            "comment": """SpokenWordAlbum.""",
            "label": "SpokenWordAlbum",
        },
        "StudioAlbum": {
            "id": "schema:StudioAlbum",
            "comment": """StudioAlbum.""",
            "label": "StudioAlbum",
        },
    }