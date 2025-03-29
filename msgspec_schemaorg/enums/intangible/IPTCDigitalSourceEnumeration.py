import enum
from typing import ClassVar, Dict, Any

class IPTCDigitalSourceEnumeration(str, enum.Enum):
    """Schema.org enumeration values for IPTCDigitalSourceEnumeration."""

    AlgorithmicMediaDigitalSource = "AlgorithmicMediaDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    AlgorithmicallyEnhancedDigitalSource = "AlgorithmicallyEnhancedDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    CompositeCaptureDigitalSource = "CompositeCaptureDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    CompositeDigitalSource = "CompositeDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    CompositeSyntheticDigitalSource = "CompositeSyntheticDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    CompositeWithTrainedAlgorithmicMediaDigitalSource = "CompositeWithTrainedAlgorithmicMediaDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    DataDrivenMediaDigitalSource = "DataDrivenMediaDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    DigitalArtDigitalSource = "DigitalArtDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    DigitalCaptureDigitalSource = "DigitalCaptureDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    MinorHumanEditsDigitalSource = "MinorHumanEditsDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    MultiFrameComputationalCaptureDigitalSource = "MultiFrameComputationalCaptureDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    NegativeFilmDigitalSource = "NegativeFilmDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    PositiveFilmDigitalSource = "PositiveFilmDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    PrintDigitalSource = "PrintDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    ScreenCaptureDigitalSource = "ScreenCaptureDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    TrainedAlgorithmicMediaDigitalSource = "TrainedAlgorithmicMediaDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."
    VirtualRecordingDigitalSource = "VirtualRecordingDigitalSource"  # "Content coded as '<a href=\"https://cv.iptc.org/newscodes/..."

    # Metadata for each enum value
    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {
        "AlgorithmicMediaDigitalSource": {
            "id": "schema:AlgorithmicMediaDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "AlgorithmicMediaDigitalSource",
        },
        "AlgorithmicallyEnhancedDigitalSource": {
            "id": "schema:AlgorithmicallyEnhancedDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicallyEnhanced">algorithmically enhanced</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "AlgorithmicallyEnhancedDigitalSource",
        },
        "CompositeCaptureDigitalSource": {
            "id": "schema:CompositeCaptureDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeCapture">composite capture</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "CompositeCaptureDigitalSource",
        },
        "CompositeDigitalSource": {
            "id": "schema:CompositeDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "CompositeDigitalSource",
        },
        "CompositeSyntheticDigitalSource": {
            "id": "schema:CompositeSyntheticDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeSynthetic">composite synthetic</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "CompositeSyntheticDigitalSource",
        },
        "CompositeWithTrainedAlgorithmicMediaDigitalSource": {
            "id": "schema:CompositeWithTrainedAlgorithmicMediaDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/compositeWithTrainedAlgorithmicMedia">composite with trained algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "CompositeWithTrainedAlgorithmicMediaDigitalSource",
        },
        "DataDrivenMediaDigitalSource": {
            "id": "schema:DataDrivenMediaDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/dataDrivenMedia">data driven media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "DataDrivenMediaDigitalSource",
        },
        "DigitalArtDigitalSource": {
            "id": "schema:DigitalArtDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalArt">digital art</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "DigitalArtDigitalSource",
        },
        "DigitalCaptureDigitalSource": {
            "id": "schema:DigitalCaptureDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture">digital capture</a></a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "DigitalCaptureDigitalSource",
        },
        "MinorHumanEditsDigitalSource": {
            "id": "schema:MinorHumanEditsDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/minorHumanEdits">minor human edits</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "MinorHumanEditsDigitalSource",
        },
        "MultiFrameComputationalCaptureDigitalSource": {
            "id": "schema:MultiFrameComputationalCaptureDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "MultiFrameComputationalCaptureDigitalSource",
        },
        "NegativeFilmDigitalSource": {
            "id": "schema:NegativeFilmDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/negativeFilm">negative film</a></a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "NegativeFilmDigitalSource",
        },
        "PositiveFilmDigitalSource": {
            "id": "schema:PositiveFilmDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/positiveFilm">positive film</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "PositiveFilmDigitalSource",
        },
        "PrintDigitalSource": {
            "id": "schema:PrintDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/print">print</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "PrintDigitalSource",
        },
        "ScreenCaptureDigitalSource": {
            "id": "schema:ScreenCaptureDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicMedia">algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "ScreenCaptureDigitalSource",
        },
        "TrainedAlgorithmicMediaDigitalSource": {
            "id": "schema:TrainedAlgorithmicMediaDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia">trained algorithmic media</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "TrainedAlgorithmicMediaDigitalSource",
        },
        "VirtualRecordingDigitalSource": {
            "id": "schema:VirtualRecordingDigitalSource",
            "comment": """Content coded as '<a href="https://cv.iptc.org/newscodes/digitalsourcetype/virtualRecording">virtual recording</a>' using the IPTC <a href="https://cv.iptc.org/newscodes/digitalsourcetype/">digital source type</a> vocabulary.""",
            "label": "VirtualRecordingDigitalSource",
        },
    }