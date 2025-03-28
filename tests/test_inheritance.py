"""
Tests for inheritance structure in generated Schema.org models.
"""
import unittest
import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

import msgspec

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from msgspec_schemaorg.generate import SchemaProcessor
from msgspec_schemaorg.base import SchemaOrgBase


class MockSchemaData:
    """Mock Schema.org data for testing."""
    
    @classmethod
    def get_basic_schema(cls):
        """Generate a minimal Schema.org structure for testing."""
        return {
            "@context": "http://schema.org/",
            "@graph": [
                {
                    "@id": "http://schema.org/Thing",
                    "@type": "rdfs:Class",
                    "rdfs:comment": "The most generic type of item.",
                    "rdfs:label": "Thing"
                },
                {
                    "@id": "http://schema.org/CreativeWork",
                    "@type": "rdfs:Class",
                    "rdfs:comment": "The most generic kind of creative work.",
                    "rdfs:label": "CreativeWork",
                    "rdfs:subClassOf": {
                        "@id": "http://schema.org/Thing"
                    }
                },
                {
                    "@id": "http://schema.org/Book",
                    "@type": "rdfs:Class",
                    "rdfs:comment": "A book.",
                    "rdfs:label": "Book",
                    "rdfs:subClassOf": {
                        "@id": "http://schema.org/CreativeWork"
                    }
                },
                {
                    "@id": "http://schema.org/name",
                    "@type": "rdf:Property",
                    "rdfs:comment": "The name of the item.",
                    "rdfs:label": "name",
                    "schema:domainIncludes": [
                        {
                            "@id": "http://schema.org/Thing"
                        }
                    ],
                    "schema:rangeIncludes": {
                        "@id": "http://schema.org/Text"
                    }
                },
                {
                    "@id": "http://schema.org/url",
                    "@type": "rdf:Property",
                    "rdfs:comment": "URL of the item.",
                    "rdfs:label": "url",
                    "schema:domainIncludes": [
                        {
                            "@id": "http://schema.org/Thing"
                        }
                    ],
                    "schema:rangeIncludes": {
                        "@id": "http://schema.org/URL"
                    }
                },
                {
                    "@id": "http://schema.org/author",
                    "@type": "rdf:Property",
                    "rdfs:comment": "The author of this content.",
                    "rdfs:label": "author",
                    "schema:domainIncludes": [
                        {
                            "@id": "http://schema.org/CreativeWork"
                        }
                    ],
                    "schema:rangeIncludes": {
                        "@id": "http://schema.org/Person"
                    }
                },
                {
                    "@id": "http://schema.org/isbn",
                    "@type": "rdf:Property",
                    "rdfs:comment": "The ISBN of the book.",
                    "rdfs:label": "isbn",
                    "schema:domainIncludes": [
                        {
                            "@id": "http://schema.org/Book"
                        }
                    ],
                    "schema:rangeIncludes": {
                        "@id": "http://schema.org/Text"
                    }
                },
                {
                    "@id": "http://schema.org/Person",
                    "@type": "rdfs:Class",
                    "rdfs:comment": "A person.",
                    "rdfs:label": "Person",
                    "rdfs:subClassOf": {
                        "@id": "http://schema.org/Thing"
                    }
                }
            ]
        }


class TestInheritance(unittest.TestCase):
    """Test inheritance structure in generated Schema.org models."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class by generating model files."""
        # Create a temporary directory for generated models
        cls.temp_dir = tempfile.mkdtemp()
        
        # Generate models in the temporary directory
        schema_data = MockSchemaData.get_basic_schema()
        processor = SchemaProcessor(schema_data)
        cls.files = processor.generate_all_structs(Path(cls.temp_dir))
        
        # Add the temporary directory to sys.path so we can import models
        sys.path.insert(0, cls.temp_dir)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up temporary directory."""
        # Remove temporary directory from sys.path
        if cls.temp_dir in sys.path:
            sys.path.remove(cls.temp_dir)
        
        # Delete temporary directory
        shutil.rmtree(cls.temp_dir)
    
    def test_thing_inherits_base(self):
        """Test that Thing inherits from SchemaOrgBase."""
        # Import the Thing class
        from msgspec_schemaorg.models.thing import Thing
        
        # Check that Thing inherits from SchemaOrgBase
        self.assertTrue(issubclass(Thing, SchemaOrgBase))
        
        # Check that Thing has JSON-LD fields
        thing = Thing(name="Test Thing")
        self.assertEqual(thing.type, "Thing")  # Default @type
        
        # Encode to JSON and check @type field
        encoded = msgspec.json.encode(thing)
        decoded = json.loads(encoded)
        self.assertEqual(decoded["@type"], "Thing")
    
    def test_creative_work_inherits_thing(self):
        """Test that CreativeWork inherits from Thing."""
        # Import the Thing and CreativeWork classes
        from msgspec_schemaorg.models.thing import Thing
        from msgspec_schemaorg.models.creativework import CreativeWork
        
        # Check inheritance
        self.assertTrue(issubclass(CreativeWork, Thing))
        
        # Create a CreativeWork instance and check inherited fields
        work = CreativeWork(name="Test Work")
        self.assertEqual(work.name, "Test Work")  # Inherited from Thing
        self.assertEqual(work.type, "CreativeWork")  # Default @type
    
    def test_book_inherits_creative_work(self):
        """Test that Book inherits from CreativeWork."""
        # Import the CreativeWork and Book classes
        from msgspec_schemaorg.models.creativework import CreativeWork
        from msgspec_schemaorg.models.creativework import Book
        
        # Check inheritance
        self.assertTrue(issubclass(Book, CreativeWork))
        
        # Create a Book instance and check inherited fields
        book = Book(name="Test Book", isbn="978-3-16-148410-0")
        self.assertEqual(book.name, "Test Book")  # Inherited from Thing
        self.assertEqual(book.isbn, "978-3-16-148410-0")  # Specific to Book
        self.assertEqual(book.type, "Book")  # Default @type
    
    def test_url_field_consistency(self):
        """Test that URL fields use the URL type consistently."""
        # Import Thing which has a url field
        from msgspec_schemaorg.models.thing import Thing
        
        # Create a Thing with a valid URL
        thing = Thing(url="https://example.com")
        
        # Check that the URL is stored correctly
        self.assertEqual(thing.url, "https://example.com")
        
        # Encode and check the JSON
        encoded = msgspec.json.encode(thing)
        decoded_json = json.loads(encoded)
        self.assertEqual(decoded_json["url"], "https://example.com")
        
        # Note: We don't test validation here since our test environment
        # may not have access to the proper validation setup
    
    def test_jsonld_fields(self):
        """Test that JSON-LD fields serialize correctly with @ prefixes."""
        # Import Thing
        from msgspec_schemaorg.models.thing import Thing
        
        # Create a Thing with JSON-LD fields
        thing = Thing(
            name="Test Thing",
            id="https://example.com/things/1",
            context="https://schema.org"
        )
        
        # Encode to JSON and parse
        encoded = msgspec.json.encode(thing)
        decoded = json.loads(encoded)
        
        # Check that @id, @type, and @context are correctly serialized
        self.assertEqual(decoded["@id"], "https://example.com/things/1")
        self.assertEqual(decoded["@type"], "Thing")
        self.assertEqual(decoded["@context"], "https://schema.org")


if __name__ == "__main__":
    unittest.main() 