import enum
from typing import ClassVar, Dict, Any

class DigitalPlatformEnumeration(str, enum.Enum):
    """Schema.org enumeration values for DigitalPlatformEnumeration."""

    AndroidPlatform = "AndroidPlatform"  # "Represents the broad notion of Android-based operating sy..."
    DesktopWebPlatform = "DesktopWebPlatform"  # "Represents the broad notion of 'desktop' browsers as a We..."
    GenericWebPlatform = "GenericWebPlatform"  # "Represents the generic notion of the Web Platform. More s..."
    IOSPlatform = "IOSPlatform"  # "Represents the broad notion of iOS-based operating systems."
    MobileWebPlatform = "MobileWebPlatform"  # "Represents the broad notion of 'mobile' browsers as a Web..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AndroidPlatform": {
            "id": "schema:AndroidPlatform",
            "comment": """Represents the broad notion of Android-based operating systems.""",
            "label": "AndroidPlatform",
        },
        "DesktopWebPlatform": {
            "id": "schema:DesktopWebPlatform",
            "comment": """Represents the broad notion of 'desktop' browsers as a Web Platform.""",
            "label": "DesktopWebPlatform",
        },
        "GenericWebPlatform": {
            "id": "schema:GenericWebPlatform",
            "comment": """Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and [[DesktopWebPlatform]], as an incomplete list. """,
            "label": "GenericWebPlatform",
        },
        "IOSPlatform": {
            "id": "schema:IOSPlatform",
            "comment": """Represents the broad notion of iOS-based operating systems.""",
            "label": "IOSPlatform",
        },
        "MobileWebPlatform": {
            "id": "schema:MobileWebPlatform",
            "comment": """Represents the broad notion of 'mobile' browsers as a Web Platform.""",
            "label": "MobileWebPlatform",
        },
    }