"""
msgspec_schemaorg - Schema.org models generated using msgspec.
"""

__version__ = "0.2.1"

from .base import SchemaOrgBase

# Import modules conditionally to avoid circular dependencies
__all__ = [
    "SchemaOrgBase",
    "models",
    "enums",
]


# These imports are deferred to avoid circular dependencies when using just one part
def __getattr__(name):
    if name == "models":
        from . import models as _models

        globals()["models"] = _models
        return _models
    elif name == "enums":
        from . import enums as _enums

        globals()["enums"] = _enums
        return _enums
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
