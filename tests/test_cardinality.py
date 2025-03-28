"""
Test that Schema.org properties correctly support multiple values (cardinality).
"""
import json
import unittest
import msgspec
from pathlib import Path

# This will only work after models are regenerated
from msgspec_schemaorg.models import Book, Person, CreativeWork


class TestCardinality(unittest.TestCase):
    """Test case for Schema.org property cardinality."""

    def test_single_value(self):
        """Test that properties work with single values."""
        # Create a book with a single author
        author = Person(name="Jane Doe")
        book = Book(
            name="The Example",
            author=author,
            isbn="123456789X"
        )
        
        # Serialize and deserialize
        json_data = msgspec.json.encode(book)
        # Load as dict for checking values
        data = json.loads(json_data)
        
        # Check values
        self.assertEqual(data["name"], "The Example")
        self.assertEqual(data["author"]["name"], "Jane Doe")
        self.assertEqual(data["isbn"], "123456789X")
    
    def test_multiple_values(self):
        """Test that properties work with multiple values (list)."""
        # Create a book with multiple authors
        authors = [
            Person(name="Jane Doe"),
            Person(name="John Smith")
        ]
        
        book = Book(
            name="The Co-Authored Example",
            author=authors,
            isbn="987654321X"
        )
        
        # Serialize and check the JSON
        json_data = msgspec.json.encode(book)
        data = json.loads(json_data)
        
        # Check values
        self.assertEqual(data["name"], "The Co-Authored Example")
        self.assertEqual(len(data["author"]), 2)
        self.assertEqual(data["author"][0]["name"], "Jane Doe")
        self.assertEqual(data["author"][1]["name"], "John Smith")
        self.assertEqual(data["isbn"], "987654321X")
    
    def test_mixed_property_types(self):
        """Test properties that accept multiple types."""
        # CreativeWork.about can be any Thing
        work1 = CreativeWork(name="About a Person", about=Person(name="Subject Person"))
        work2 = CreativeWork(name="About a Book", about=Book(name="Subject Book"))
        
        # Serialize and check
        json_data1 = msgspec.json.encode(work1)
        json_data2 = msgspec.json.encode(work2)
        
        data1 = json.loads(json_data1)
        data2 = json.loads(json_data2)
        
        # Check values
        self.assertEqual(data1["about"]["name"], "Subject Person")
        self.assertEqual(data2["about"]["name"], "Subject Book")
    
    def test_mixed_cardinality_and_types(self):
        """Test properties with both multiple types and multiple values."""
        # Book can have multiple authors that can be either Person or Organization
        from msgspec_schemaorg.models import Organization
        
        book = Book(
            name="Complex Example",
            author=[
                Person(name="First Author"),
                Organization(name="Publishing Group"),
                Person(name="Second Author")
            ],
            isbn="555555555X"
        )
        
        # Serialize and check
        json_data = msgspec.json.encode(book)
        data = json.loads(json_data)
        
        # Check values
        self.assertEqual(data["name"], "Complex Example")
        self.assertEqual(len(data["author"]), 3)
        self.assertEqual(data["author"][0]["name"], "First Author")
        self.assertEqual(data["author"][1]["name"], "Publishing Group")
        self.assertEqual(data["author"][2]["name"], "Second Author")
        self.assertEqual(data["isbn"], "555555555X")


if __name__ == "__main__":
    unittest.main() 