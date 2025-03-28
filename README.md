# msgspec-schemaorg

[![PyPI version](https://badge.fury.io/py/msgspec-schemaorg.svg)](https://badge.fury.io/py/msgspec-schemaorg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build and Publish](https://github.com/mikewolfd/msgspec-schemaorg/actions/workflows/python-publish.yml/badge.svg)](https://github.com/mikewolfd/msgspec-schemaorg/actions/workflows/python-publish.yml)

Generate Python `msgspec.Struct` classes from the Schema.org vocabulary for high-performance data validation and serialization.

Inspired by [pydantic_schemaorg](https://github.com/lexiq-legal/pydantic_schemaorg).

## Goal

Provide a tool to automatically generate efficient Python data structures based on [Schema.org](https://schema.org/), using the [`msgspec`](https://github.com/jcrist/msgspec) library. This enables fast serialization, deserialization, and validation of Schema.org structured data.

## Development Process

This project was developed using a combination of  AI tools:

- **Cursor IDE**: The primary development environment
- **Claude 3.7 Sonnet**: Used as the primary AI coding agent
- **Gemini 2.5**: Was used for brainstorming and architecture planning

The entire project was developed using this AI-assisted workflow, from initial concept to final implementation.

While AI assisted in development, all code was reviewed and tested.

## Features

*   **Schema Acquisition:** Downloads the latest Schema.org vocabulary (JSON-LD).
*   **Type Mapping:** Maps Schema.org types (Text, Number, Date, URL, etc.) to Python types (`str`, `int | float`, `datetime.date`, `URL`, `bool`).
*   **Code Generation:** Creates `msgspec.Struct` definitions from Schema.org types, including type hints and docstrings.
*   **Proper Inheritance:** Preserves the Schema.org class hierarchy using Python inheritance (`Book` inherits from `CreativeWork`, which inherits from `Thing`).
*   **JSON-LD Compatibility:** All models support JSON-LD fields (`@id`, `@type`, `@context`) that serialize correctly.
*   **Category Organization:** Organizes generated classes into subdirectories (CreativeWork, Person, etc.).
*   **Circular Dependency Resolution:** Uses forward references (`"TypeName"`) and `TYPE_CHECKING` imports.
*   **Python Compatibility:** Handles reserved keywords.
*   **Convenient Imports:** All generated classes are importable from `msgspec_schemaorg.models`.
*   **ISO8601 Date Handling:** Utility function `parse_iso8601` for date/datetime strings.
*   **Type Specificity:** Sorts type unions to prioritize more specific types (e.g., `Integer` before `Number`).
*   **URL Validation:** Validates URL fields using a centralized `URL` type with pattern validation.
*   **Comprehensive Testing:** Includes tests for model generation, validation, inheritance, and usage.

## Installation

```bash
pip install msgspec-schemaorg
```

Or install from source for development:

```bash
git clone https://github.com/mikewolfd/msgspec-schemaorg.git
cd msgspec-schemaorg
pip install -e .
```

## Quick Start

```python
import msgspec
from msgspec_schemaorg.models import Person, PostalAddress

# Create Struct instances
address = PostalAddress(
    streetAddress="123 Main St",
    addressLocality="Anytown",
    postalCode="12345",
    addressCountry="US"
)

person = Person(
    name="Jane Doe",
    jobTitle="Software Engineer",
    address=address,
    # JSON-LD fields
    id="https://example.com/people/jane",
    context="https://schema.org"
)

# Encode to JSON
json_bytes = msgspec.json.encode(person)
print(json_bytes.decode())
# Output: {"name":"Jane Doe","jobTitle":"Software Engineer","address":{"streetAddress":"123 Main St","addressLocality":"Anytown","postalCode":"12345","addressCountry":"US"},"@id":"https://example.com/people/jane","@context":"https://schema.org","@type":"Person"}
```

## Usage

### 1. Generate Models

Run the generation script. This fetches the schema and creates Python models in `msgspec_schemaorg/models/`.

```bash
python scripts/generate_models.py
```

**Options:**

*   `--schema-url URL`: Specify Schema.org data URL.
*   `--output-dir DIR`: Set output directory for generated code.
*   `--save-schema`: Save the downloaded schema JSON locally.
*   `--clean`: Clean the output directory before generation.

### 2. Use Models

Import and use the generated `Struct` classes as shown in the Quick Start. All models are available under `msgspec_schemaorg.models`.

```python
from msgspec_schemaorg.models import BlogPosting, Person, Organization, ImageObject

# Create nested objects
blog_post = BlogPosting(
    name="Understanding Schema.org with Python",
    headline="How to Use Schema.org Types in Python",
    author=Person(name="Jane Author"),
    publisher=Organization(name="TechMedia Inc."),
    image=ImageObject(url="https://example.com/images/header.jpg"),
    datePublished="2023-09-15",  # ISO8601 date string
    # JSON-LD fields
    id="https://example.com/blog/schema-org-python",
    context="https://schema.org"
)
```

### Inheritance Structure

All Schema.org models preserve the original class hierarchy:

```python
from msgspec_schemaorg.models import Thing, CreativeWork, Book

# All Schema.org types inherit ultimately from Thing
isinstance(Book(), Thing)  # True
isinstance(Book(), CreativeWork)  # True

# Properties are inherited
book = Book(name="The Great Gatsby")
print(book.name)  # Inherited from Thing
```

### JSON-LD Compatibility

All models have JSON-LD fields for linked data integration:

```python
from msgspec_schemaorg.models import Product
import msgspec
import json

# Create a product with JSON-LD fields
product = Product(
    name="Smartphone",
    id="https://example.com/products/123",  # Maps to @id
    context="https://schema.org",  # Maps to @context  
    type="Product"  # Maps to @type (usually has default value)
)

# Encode to JSON
json_bytes = msgspec.json.encode(product)
data = json.loads(json_bytes)

# JSON-LD fields are properly serialized with @ prefix
print(data["@id"])  # https://example.com/products/123
print(data["@context"])  # https://schema.org
print(data["@type"])  # Product
```

### Handling Dates

Use the `parse_iso8601` utility for date strings:

```python
from msgspec_schemaorg.utils import parse_iso8601
from msgspec_schemaorg.models import BlogPosting

published_date = parse_iso8601("2023-09-15") # -> datetime.date
modified_time = parse_iso8601("2023-09-20T14:30:00Z") # -> datetime.datetime

post = BlogPosting(datePublished=published_date, dateModified=modified_time)
print(post.datePublished.year) # 2023
```

### URL Validation

URL fields are automatically validated using a centralized URL type:

```python
import msgspec
from msgspec_schemaorg.models import WebSite

# Valid URL
website = WebSite(name="My Website", url="https://example.com")

# Invalid URL during decoding raises ValidationError
try:
    msgspec.json.decode(
        b'{"name":"Invalid Site", "url":"not-a-valid-url"}',
        type=WebSite
    )
except msgspec.ValidationError as e:
    print(f"Validation Error: {e}")
```

### Simplified Workflow (`run.py`)

Use `run.py` for common tasks:

```bash
python run.py generate  # Generate models
python run.py test      # Run all tests
python run.py example   # Run basic example
python run.py all       # Generate models and run tests/examples
```

## Testing

Run the test suite:

```bash
python run_tests.py
```

Or run specific test groups:

```bash
python run_tests.py unittest
python run_tests.py examples
python run_tests.py imports
python run_tests.py inheritance  # Test the inheritance structure
```

The tests cover model generation, imports, date parsing, URL validation, inheritance, and example script execution.

## Type System

*   **Primitives:** Schema.org types like `Text`, `Number`, `Date`, `URL` are mapped to Python types (`str`, `int | float`, `datetime.date`, `URL`, `bool`).
*   **Specificity:** Type unions are sorted (e.g., `Integer` before `Number`).
*   **Literals:** `Boolean` constants use `Literal[True]` / `Literal[False]`.
*   **URLs:** Validated using a consistent `URL` type with pattern validation.
*   **Inheritance:** Schema.org hierarchy is preserved through Python class inheritance.
*   **JSON-LD:** All models support standard JSON-LD fields (`@id`, `@type`, `@context`).

## Limitations

*   **Core Schema Only:** Extensions (e.g., health/medical) are not included.
*   **Optional Properties:** All properties are generated as optional (`| None`).
*   **Extra Fields Ignored by Default:** By default, `msgspec` ignores fields present in the input data but not defined in the `Struct`. To raise an error for unknown fields, `Struct`s must be defined with `forbid_unknown_fields=True`.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
