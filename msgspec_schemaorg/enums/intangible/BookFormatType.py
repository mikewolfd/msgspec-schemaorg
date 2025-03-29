import enum
from typing import ClassVar, Dict, Any

class BookFormatType(str, enum.Enum):
    """Schema.org enumeration values for BookFormatType."""

    AudiobookFormat = "AudiobookFormat"  # "Book format: Audiobook. This is an enumerated value for u..."
    EBook = "EBook"  # "Book format: Ebook."
    GraphicNovel = "GraphicNovel"  # "Book format: GraphicNovel. May represent a bound collecti..."
    Hardcover = "Hardcover"  # "Book format: Hardcover."
    Paperback = "Paperback"  # "Book format: Paperback."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AudiobookFormat": {
            "id": "schema:AudiobookFormat",
            "comment": """Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties.""",
            "label": "AudiobookFormat",
        },
        "EBook": {
            "id": "schema:EBook",
            "comment": """Book format: Ebook.""",
            "label": "EBook",
        },
        "GraphicNovel": {
            "id": "schema:GraphicNovel",
            "comment": """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.""",
            "label": "GraphicNovel",
        },
        "Hardcover": {
            "id": "schema:Hardcover",
            "comment": """Book format: Hardcover.""",
            "label": "Hardcover",
        },
        "Paperback": {
            "id": "schema:Paperback",
            "comment": """Book format: Paperback.""",
            "label": "Paperback",
        },
    }