# msgspec-schemaorg

[![PyPI version](https://badge.fury.io/py/msgspec-schemaorg.svg)](https://badge.fury.io/py/msgspec-schemaorg) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build and Publish](https://github.com/mikewolfd/msgspec-schemaorg/actions/workflows/python-publish.yml/badge.svg)](https://github.com/mikewolfd/msgspec-schemaorg/actions/workflows/python-publish.yml)

Generate Python `msgspec.Struct` classes from the Schema.org vocabulary.

## Goal

This project provides a tool to automatically generate efficient Python data structures based on the [Schema.org](https://schema.org/) vocabulary, using the high-performance [`msgspec`](https://github.com/jcrist/msgspec) library. This allows for easy serialization, deserialization, and validation of Schema.org structured data within Python applications.

## Development Process

This project was developed using a combination of  AI tools:

### AI-Assisted Development

- **Cursor IDE**: The primary development environment
- **Claude 3.7 Sonnet**: Used as the primary AI coding agent
- **Gemini 2.5**: Was used for brainstorming and architecture planning

The entire project was developed using this AI-assisted workflow, from initial concept to final implementation.

While AI assisted in development, all code was reviewed and tested.

## Project Status

The project has successfully completed all core implementation phases:

- ✅ Basic project setup and structure
- ✅ Schema.org data acquisition and type mapping 
- ✅ Code generation for `msgspec.Struct` classes
- ✅ Inheritance and property handling
- ✅ Multi-file organization by category
- ✅ Circular dependency resolution
- ✅ Python compatibility (reserved keywords)
- ✅ ISO8601 date parsing
- ✅ Comprehensive test suite
- ✅ Runner scripts for simplified usage
- ✅ CLI support with command-line arguments
- ✅ Basic and advanced usage examples

## Features

* **Schema Acquisition:** Downloads the latest Schema.org vocabulary definition (JSON-LD format).
* **Type Mapping:** Maps Schema.org primitive types (like `Text`, `Number`, `Date`, `URL`, `Boolean`) to appropriate Python types (`str`, `int | float`, `datetime.date`, `str`, `bool`).
* **Class & Property Parsing:** Identifies Schema.org classes (`rdfs:Class`) and properties (`rdf:Property`).
* **Inheritance Handling:** Resolves the class hierarchy (`rdfs:subClassOf`) to include properties from parent classes.
* **Code Generation:** Generates Python files containing `msgspec.Struct` definitions corresponding to Schema.org types, including type hints and docstrings derived from `rdfs:comment`.
* **Category Organization:** Organizes the generated classes into subdirectories based on their categories (CreativeWork, Person, Organization, etc.) for better maintainability.
* **Circular Dependency Resolution:** Handles circular dependencies between classes using string literal type annotations and proper import management.
* **Python Compatibility:** Handles Python reserved keywords and ensures valid identifiers for all generated classes and properties.
* **Convenient Imports:** All generated classes can be imported directly from the main package.
* **ISO8601 Date Handling:** Provides utility functions for parsing ISO8601 date and datetime strings.
* **Comprehensive Testing:** Includes test suites that validate the generated models against real Schema.org examples.

## Installation

*(Once packaged)*

```bash
pip install msgspec-schemaorg
```

*(From source, for development)*

```bash
# Clone the repository
git clone https://github.com/username/msgspec-schemaorg.git
cd msgspec-schemaorg

# Install in development mode
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
    address=address
)

# Encode to JSON
json_bytes = msgspec.json.encode(person)
print(json_bytes.decode())
```

### Simplified Workflow with run.py

For a quick start, use the included `run.py` script:

```bash
# Generate the models and run all examples
python run.py all

# Or run individual steps
python run.py generate       # Generate only the models
python run.py example        # Run basic example
python run.py advanced       # Run advanced example with nested objects
python run.py test           # Run all tests
```

## Usage

1. **Generate the Models:**
    Run the generation script. This will fetch the schema and create the Python model files in `msgspec_schemaorg/models/`.

    ```bash
    python scripts/generate_models.py
    ```

    Options:

    ```
    --schema-url URL    URL to download the Schema.org data from
    --output-dir DIR    Directory to save the generated code to
    --save-schema       Save the downloaded Schema.org data to a JSON file
    --clean             Clean the output directory before generating new files
    ```

2. **Use the Generated Models:**
    Import and use the generated `Struct` classes in your Python code as shown in the Quick Start section above.

3. **Advanced Usage:**
    The package supports complex nested structures, as shown in the advanced example:

    ```python
    from msgspec_schemaorg.models import (
        BlogPosting, 
        Person, 
        Organization, 
        ImageObject
    )
    
    # Create a blog post with nested objects
    blog_post = BlogPosting(
        name="Understanding Schema.org with Python",
        headline="How to Use Schema.org Types in Python",
        author=Person(name="Jane Author"),
        publisher=Organization(name="TechMedia Inc."),
        image=ImageObject(url="https://example.com/images/header.jpg"),
        datePublished="2023-09-15"  # ISO8601 date string
    )
    ```

    ### Handling ISO8601 Dates

    When working with Schema.org JSON data that contains ISO8601 date and datetime strings, you can use the provided `parse_iso8601` utility function:

    ```python
    from msgspec_schemaorg.utils import parse_iso8601

    # Parse ISO8601 strings to Python date/datetime objects
    published_date = parse_iso8601("2023-09-15")            # Returns a date object
    modified_date = parse_iso8601("2023-09-20T14:30:00Z")   # Returns a datetime object

    # Create object with parsed dates
    blog_post = BlogPosting(
        name="My Blog Post",
        datePublished=published_date,
        dateModified=modified_date
    )

    # Now you can work with actual date/datetime objects
    year = blog_post.datePublished.year                     # 2023
    time = f"{blog_post.dateModified.hour}:{blog_post.dateModified.minute}"  # 14:30
    ```

    The `parse_iso8601` function automatically determines whether the string represents a date or a datetime and returns the appropriate Python object.

    See `examples/advanced_example.py` for a more detailed example.

## Generated Structure

The generated models are organized in a hierarchical structure:

```
msgspec_schemaorg/models/
├── __init__.py             # Imports and exports all classes
├── action/                 # Action-related classes
│   ├── __init__.py
│   ├── AcceptAction.py
│   └── ...
├── creativework/           # CreativeWork-related classes
│   ├── __init__.py
│   ├── Article.py
│   └── ...
├── person/                 # Person-related classes
│   ├── __init__.py
│   ├── Person.py
│   └── ...
└── ...                     # Other category directories
```

You can import classes in two ways:

1. Directly from the models package (recommended):

   ```python
   from msgspec_schemaorg.models import Person, CreativeWork
   ```

2. From their specific category module:

   ```python
   from msgspec_schemaorg.models.person import Person
   from msgspec_schemaorg.models.creativework import CreativeWork
   ```

## Testing

The package includes a comprehensive test suite that validates the generated models against real Schema.org examples. Run the tests with:

```bash
# Run all tests
python run_tests.py

# Run specific test groups
python run_tests.py examples    # Run only example scripts
python run_tests.py unittest    # Run only unit tests
python run_tests.py imports     # Test only model imports
```

The tests verify that:

1. All classes can be properly imported directly from the package
2. Classes can be instantiated with default values and nested structures
3. Date/datetime parsing works correctly with ISO8601 strings
4. Example scripts run without errors

Our test system successfully validates the library's functionality including circular dependency resolution, import structure, and ISO8601 date handling.

## Current Limitations

* **Core Schema Only:** Currently only supports the core Schema.org vocabulary. Extensions (like health/medical terms) are not included.
* **Optional Properties:** All properties are marked as optional (`| None`), as Schema.org doesn't strictly define required vs. optional properties.
* **Docstring Format:** Some docstrings contain non-string data in the source Schema.org data, which are converted to strings but may not be perfectly formatted.
* **Extra Properties Validation:** The generated models strictly validate against the schema definition. Extra properties in input data (that aren't defined in the schema) will cause validation errors.

## Future Work

Based on our original project plan and completed items, these are the remaining areas for improvement:

* **Package Distribution:** Finalize setup.py and publish the package to PyPI with proper metadata.
* **Schema Extensions:** Add support for Schema.org extensions to cover specialized domains.
* **Optional/Required Fields:** Improve handling of optional vs. required fields based on common usage patterns.
* **Lenient Mode:** Add an option for lenient parsing that allows extra fields in input data.
* **Enhanced JSON-LD Support:** Consider using `rdflib` for more robust JSON-LD graph processing if the current approach proves insufficient.
* **CI/CD Integration:** Set up GitHub Actions for automated testing and deployment.
* **External Data Processing:** Add helpers for processing external Schema.org JSON-LD data directly from websites.
* **Documentation:** Create more detailed documentation with usage examples, API references, and advanced customization guidance.

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

### Automated Testing

Every push to the main branch and pull request triggers automated tests that:
- Run on multiple Python versions (3.10, 3.11, 3.12)
- Generate the Schema.org models
- Run the comprehensive test suite

### Automated Deployment

The package is automatically published to PyPI when:
1. A tag with format `v*` (e.g., `v0.1.0`) is pushed → Published to TestPyPI
2. A GitHub Release is created → Published to the main PyPI repository

For more details on the CI/CD process, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Implementation Notes

### Circular Dependency Management

Schema.org contains numerous circular dependencies between classes. For example, `Person` may have properties that are of type `Organization`, while `Organization` may have properties of type `Person`.

To resolve these circular dependencies, this package uses:

1. **Forward References**: For classes that are involved in circular dependencies, the package uses string literal type annotations (`"Person"` instead of `Person`) to prevent import issues.

2. **TYPE_CHECKING Imports**: Imports for circularity-involved classes are placed inside `if TYPE_CHECKING` blocks to prevent runtime circular import errors.

3. **Automatic Detection**: The code generator automatically detects circular dependencies in the class hierarchy and adjusts imports accordingly.

These techniques ensure that the generated code is both type-checker compatible and runtime-safe.

### Performance Considerations

The generated models use `msgspec.Struct` as their base class, which offers significant performance advantages over traditional dataclasses or Pydantic models:

- Up to 30x faster JSON serialization/deserialization
- Lower memory usage
- Strict validation while maintaining performance

### Customizability

The generator is designed to be customizable. If you need to modify the output:

1. The `--schema-url` parameter can be used to point to a different Schema.org definition.
2. The code in `msgspec_schemaorg/generate.py` can be extended to add custom handling for specific classes.
3. The `SchemaProcessor` class can be subclassed to override specific methods like `generate_struct_code()`.

### Type Conversions

Schema.org types are mapped to Python types as follows:

| Schema.org Type | Python Type |
|-----------------|-------------|
| Text, URL | str |
| Number | int | float |
| Integer | int |
| Float | float |
| Boolean | bool |
| Date | datetime.date |
| DateTime | datetime.datetime |
| Time | datetime.time |
| Any combination | Union types |
