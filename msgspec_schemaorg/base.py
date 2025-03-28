"""
Base classes for Schema.org models with JSON-LD compatibility.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Union
import msgspec
from msgspec import field


class SchemaOrgBase(msgspec.Struct, frozen=True, omit_defaults=True):
    """
    Base class for all Schema.org models with JSON-LD fields.
    
    This class provides the standard JSON-LD fields (@id, @type, @context, etc.)
    that are used to represent linked data. All Schema.org model classes
    inherit from this base.
    
    JSON-LD fields are aliased using msgspec's field renaming to ensure
    that the serialized output uses the @ prefix.
    """
    id: Optional[str] = field(default=None, name="@id")
    context: Optional[Union[str, Dict[str, Any]]] = field(default=None, name="@context")
    # Note: type field is intentionally omitted since it will be provided by each class
    graph: Optional[List[Dict[str, Any]]] = field(default=None, name="@graph")
    reverse: Optional[Dict[str, Any]] = field(default=None, name="@reverse") 