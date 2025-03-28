"""
msgspec-schemaorg: Generate Python msgspec.Struct classes from the Schema.org vocabulary.

This package provides tools to generate efficient Python data structures based
on the Schema.org vocabulary, using the high-performance msgspec library.

Features:
- Generates msgspec.Struct classes from Schema.org
- Auto-converts ISO8601 date/datetime strings
- Handles circular dependencies
- Maintains type safety with modern Python type annotations
"""

__version__ = "0.1.3"

# Import the key functions and classes to expose at the package level
from .generate import fetch_and_generate, SchemaProcessor
from .utils import parse_iso8601

# Optional: Import any generated models if they exist
try:
    from . import models
except ImportError:
    # Models haven't been generated yet or couldn't be imported
    pass
