"""
Utility functions for msgspec-schemaorg.
"""
from datetime import date, datetime
import re
from urllib.parse import urlparse
from typing import Any, Optional, Union, Annotated
from msgspec import Struct, field, Meta


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


# URL regex pattern - matches valid URLs with scheme and domain
URL_PATTERN = r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/?|[/?]\S+)$"

# Define URL as an Annotated str with a pattern constraint
URL = Annotated[str, Meta(pattern=URL_PATTERN)]


def is_valid_url(value: str) -> bool:
    """
    Check if a string is a valid URL.
    
    Args:
        value: The string to validate
        
    Returns:
        True if the string is a valid URL, False otherwise
    """
    if not isinstance(value, str):
        return False
    
    # Check URL format with regex
    if not re.match(URL_PATTERN, value, re.IGNORECASE):
        return False
    
    # More thorough check using urlparse
    try:
        result = urlparse(value)
        return all([result.scheme, result.netloc])
    except Exception:
        return False 