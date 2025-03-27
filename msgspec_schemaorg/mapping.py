"""
Type mapping between Schema.org data types and Python types.
"""
from datetime import date, datetime, time
from typing import Union, Dict, Any, Type, TypeVar, get_origin, get_args, Literal, Annotated

from msgspec_schemaorg.utils import URL

# Mapping of Schema.org primitive types to Python types
SCHEMA_TO_PYTHON_TYPE_MAPPING = {
    # Core primitive types
    "schema:Text": str,
    "schema:String": str,
    "schema:Number": "int | float",  # Using string representation instead of Union
    "schema:Integer": int,
    "schema:Float": float,
    "schema:Boolean": bool,
    "schema:Date": date,
    "schema:DateTime": datetime,
    "schema:Time": time,
    "schema:URL": URL,  # Now use our annotated URL type for validation
    
    # Other common types
    "schema:True": "Literal[True]",  # Using Literal for more specific type checking
    "schema:False": "Literal[False]",  # Using Literal for more specific type checking
    "schema:XPathType": str,
    "schema:CssSelectorType": str,
    "schema:PronounceableText": str,
}

# Type specificity ranking to handle conflicts when multiple types are available
# Higher number = more specific type that should be preferred
TYPE_SPECIFICITY = {
    "Boolean": 1,
    "False": 2,  # More specific than Boolean
    "True": 2,   # More specific than Boolean
    "Date": 4,
    "DateTime": 5,
    "Time": 4,
    "Number": 3,
    "Float": 4,  # More specific than Number
    "Integer": 5,  # More specific than Number
    "Text": 1,
    "CssSelectorType": 2,  # More specific than Text
    "PronounceableText": 2,  # More specific than Text
    "URL": 3,  # More specific than Text, and now it's validated
    "XPathType": 2,  # More specific than Text
}

# Short aliases without the schema: prefix
SCHEMA_TO_PYTHON_TYPE_MAPPING.update({
    k.replace("schema:", ""): v for k, v in SCHEMA_TO_PYTHON_TYPE_MAPPING.items()
})

# Similar mapping for handling ranges in property definitions
def resolve_type_reference(type_ref: str) -> Type:
    """
    Resolves a Schema.org type reference to a Python type.
    
    If the type_ref is a primitive type like Text, Number, etc., returns the appropriate Python type.
    If the type_ref is a class (like schema:Person), assumes it will be a forward reference to a
    generated Struct class, so returns a string representation to be used in annotations.
    
    Args:
        type_ref: A Schema.org type reference (e.g., "schema:Text", "schema:Person")
        
    Returns:
        A Python type or string representation of a type for forward references
    """
    # Validate input
    if not isinstance(type_ref, str):
        print(f"Warning: type_ref is not a string but {type(type_ref)}: {type_ref}")
        if isinstance(type_ref, dict) and '@id' in type_ref:
            # If it's a dict with @id, extract the ID
            type_ref = type_ref['@id']
        else:
            # Default to string type
            return str
    
    # Remove the schema: prefix if present
    clean_ref = type_ref.replace("schema:", "").replace("http://schema.org/", "")
    
    # If it's a primitive type, return the mapped Python type
    if clean_ref in SCHEMA_TO_PYTHON_TYPE_MAPPING:
        return SCHEMA_TO_PYTHON_TYPE_MAPPING[clean_ref]
    
    # Otherwise, assume it's a reference to another Schema.org class
    # and return the class name as a string (for forward reference)
    return clean_ref

def get_type_specificity(type_name: str) -> int:
    """
    Get the specificity ranking for a type name.
    Higher values indicate more specific types that should be preferred.
    
    Args:
        type_name: A Schema.org type name without the schema: prefix
        
    Returns:
        Integer specificity ranking (higher = more specific)
    """
    # Remove schema: prefix if present
    clean_name = type_name.replace("schema:", "").replace("http://schema.org/", "")
    return TYPE_SPECIFICITY.get(clean_name, 0)
