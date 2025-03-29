import enum
from typing import ClassVar, Dict, Any

class GamePlayMode(str, enum.Enum):
    """Schema.org enumeration values for GamePlayMode."""

    CoOp = "CoOp"  # "Play mode: CoOp. Co-operative games, where you play on th..."
    MultiPlayer = "MultiPlayer"  # "Play mode: MultiPlayer. Requiring or allowing multiple hu..."
    SinglePlayer = "SinglePlayer"  # "Play mode: SinglePlayer. Which is played by a lone player."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "CoOp": {
            "id": "schema:CoOp",
            "comment": """Play mode: CoOp. Co-operative games, where you play on the same team with friends.""",
            "label": "CoOp",
        },
        "MultiPlayer": {
            "id": "schema:MultiPlayer",
            "comment": """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.""",
            "label": "MultiPlayer",
        },
        "SinglePlayer": {
            "id": "schema:SinglePlayer",
            "comment": """Play mode: SinglePlayer. Which is played by a lone player.""",
            "label": "SinglePlayer",
        },
    }