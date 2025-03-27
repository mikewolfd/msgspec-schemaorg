"""
Utility functions for msgspec-schemaorg.
"""
from datetime import date, datetime


def parse_iso8601(value):
    """
    Parse ISO8601 date/datetime string to Python objects.
    
    Args:
        value: A string value in ISO8601 format, or any other value.
        
    Returns:
        Parsed date/datetime object if value is a string in ISO8601 format,
        otherwise returns the original value.
    """
    if not value or not isinstance(value, str):
        return value
    
    try:
        # Try parsing as date first (YYYY-MM-DD)
        if "T" not in value and len(value.split("-")) == 3:
            return date.fromisoformat(value)
        
        # Handle UTC timezone indicator "Z"
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
            
        # Try as datetime
        return datetime.fromisoformat(value)
    except ValueError:
        # If parsing fails, return the original string
        return value 