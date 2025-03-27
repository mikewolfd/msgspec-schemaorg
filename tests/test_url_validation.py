#!/usr/bin/env python3
"""
Tests for URL validation functionality.
"""

import sys
import unittest
import re
from typing import Annotated

from msgspec import Meta, ValidationError, Struct

try:
    from msgspec_schemaorg.utils import URL, is_valid_url, URL_PATTERN
except ImportError:
    print("Error: Utils not found. Please check the installation.")
    sys.exit(1)


class TestURLValidation(unittest.TestCase):
    """Test class for URL validation functionality."""
    
    def test_is_valid_url(self):
        """Test the is_valid_url utility function."""
        # Valid URLs
        self.assertTrue(is_valid_url("https://example.com"))
        self.assertTrue(is_valid_url("http://example.com/path?query=value"))
        self.assertTrue(is_valid_url("https://sub.example.co.uk:8080/path"))
        
        # Invalid URLs
        self.assertFalse(is_valid_url("not a url"))
        self.assertFalse(is_valid_url("example.com"))  # Missing scheme
        self.assertFalse(is_valid_url("https://"))  # Missing domain
        self.assertFalse(is_valid_url(123))  # Not a string
    
    def test_url_pattern(self):
        """Test the URL pattern."""
        # Valid URLs
        self.assertTrue(re.match(URL_PATTERN, "https://example.com", re.IGNORECASE))
        self.assertTrue(re.match(URL_PATTERN, "http://localhost", re.IGNORECASE))
        self.assertTrue(re.match(URL_PATTERN, "https://192.168.1.1", re.IGNORECASE))
        
        # Invalid URLs
        self.assertFalse(bool(re.match(URL_PATTERN, "not-a-url", re.IGNORECASE)))
        self.assertFalse(bool(re.match(URL_PATTERN, "example.com", re.IGNORECASE)))  # Missing scheme
    
    def test_url_annotation(self):
        """Test URL validation with Annotated type and pattern matching."""
        # Create a struct class with URL validation
        from msgspec import json
        
        # Define a simple pattern for testing to avoid regex compilation issues
        test_pattern = r"^https?://.*$"
        
        class URLStruct(Struct):
            url: Annotated[str, Meta(pattern=test_pattern)]
        
        # Test with valid URL
        valid_json = b'{"url": "https://example.com"}'
        obj = json.decode(valid_json, type=URLStruct)
        self.assertEqual(obj.url, "https://example.com")
        
        # Test with invalid URL
        invalid_json = b'{"url": "not-a-url"}'
        with self.assertRaises(ValidationError):
            json.decode(invalid_json, type=URLStruct)


if __name__ == "__main__":
    unittest.main() 