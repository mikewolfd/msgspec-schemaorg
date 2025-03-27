#!/usr/bin/env python3
"""
Tests for verifying proper imports and date handling functionality.
"""

import sys
import unittest
from datetime import date, datetime

try:
    from msgspec_schemaorg.models import (
        Person, 
        Organization, 
        PostalAddress, 
        BlogPosting
    )
    from msgspec_schemaorg.utils import parse_iso8601
except ImportError:
    print("Error: Models not found. Please generate them first by running scripts/generate_models.py")
    sys.exit(1)


class TestImportsAndDates(unittest.TestCase):
    """Test class for imports and dates functionality."""
    
    def test_imports(self):
        """Test that we can import different classes from the root package."""
        # Basic instantiation tests
        person = Person(name="Test Person")
        self.assertEqual(person.name, "Test Person")
        
        org = Organization(name="Test Organization")
        self.assertEqual(org.name, "Test Organization")
        
        address = PostalAddress(streetAddress="123 Test St")
        self.assertEqual(address.streetAddress, "123 Test St")
        
        blog = BlogPosting(headline="Test Headline")
        self.assertEqual(blog.headline, "Test Headline")
        
    def test_nested_objects(self):
        """Test nested object creation and access."""
        # Create a hierarchy of objects
        address = PostalAddress(
            streetAddress="123 Main St",
            addressLocality="Testville",
            postalCode="12345"
        )
        
        person = Person(
            name="John Tester",
            address=address,
            email="john@example.com"
        )
        
        # Test access to nested properties
        self.assertEqual(person.name, "John Tester")
        self.assertEqual(person.address.streetAddress, "123 Main St")
        self.assertEqual(person.address.addressLocality, "Testville")
        
    def test_date_parsing(self):
        """Test ISO8601 date parsing functionality."""
        # Test date parsing
        date_str = "2023-05-15"
        parsed_date = parse_iso8601(date_str)
        self.assertIsInstance(parsed_date, date)
        self.assertEqual(parsed_date.year, 2023)
        self.assertEqual(parsed_date.month, 5)
        self.assertEqual(parsed_date.day, 15)
        
        # Test datetime parsing
        datetime_str = "2023-05-15T14:30:45Z"
        parsed_datetime = parse_iso8601(datetime_str)
        self.assertIsInstance(parsed_datetime, datetime)
        self.assertEqual(parsed_datetime.year, 2023)
        self.assertEqual(parsed_datetime.month, 5)
        self.assertEqual(parsed_datetime.day, 15)
        self.assertEqual(parsed_datetime.hour, 14)
        self.assertEqual(parsed_datetime.minute, 30)
        self.assertEqual(parsed_datetime.second, 45)
        
        # Test with timezone offset
        datetime_tz_str = "2023-05-15T14:30:45+02:00"
        parsed_datetime_tz = parse_iso8601(datetime_tz_str)
        self.assertIsInstance(parsed_datetime_tz, datetime)
        # Timezone offset is retained, but we don't test specifics as that depends on system timezone
        
    def test_date_in_object(self):
        """Test using parsed dates in Schema.org objects."""
        # Parse dates
        published = parse_iso8601("2023-05-15")
        modified = parse_iso8601("2023-05-20T14:30:00Z")
        
        # Create blog post with dates
        blog = BlogPosting(
            headline="Test Blog",
            datePublished=published,
            dateModified=modified
        )
        
        # Test date properties
        self.assertEqual(blog.headline, "Test Blog")
        self.assertIsInstance(blog.datePublished, date)
        self.assertEqual(blog.datePublished.year, 2023)
        self.assertEqual(blog.datePublished.month, 5)
        
        self.assertIsInstance(blog.dateModified, datetime)
        self.assertEqual(blog.dateModified.hour, 14)
        self.assertEqual(blog.dateModified.minute, 30)


if __name__ == "__main__":
    unittest.main() 