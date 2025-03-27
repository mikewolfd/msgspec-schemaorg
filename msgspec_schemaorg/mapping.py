"""
Type mapping between Schema.org data types and Python types.
"""
from datetime import date, datetime, time
from typing import Union, Dict, Any, Type, TypeVar, get_origin, get_args

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
    "schema:URL": str,
    
    # Other common types
    "schema:True": bool,
    "schema:False": bool,
    "schema:XPathType": str,
    "schema:CssSelectorType": str,
    "schema:PronounceableText": str,
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
