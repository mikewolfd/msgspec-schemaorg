# msgspec-schemaorg

[![PyPI version](https://badge.fury.io/py/msgspec-schemaorg.svg)](https://badge.fury.io/py/msgspec-schemaorg) <!-- Placeholder: Add actual badge once published -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Placeholder: Confirm license -->

Generate Python `msgspec.Struct` classes from the Schema.org vocabulary.

## Goal

This project provides a tool to automatically generate efficient Python data structures based on the [Schema.org](https://schema.org/) vocabulary, using the high-performance [`msgspec`](https://github.com/jcrist/msgspec) library. This allows for easy serialization, deserialization, and validation of Schema.org structured data within Python applications.

## Features (Planned)

*   **Schema Acquisition:** Downloads the latest Schema.org vocabulary definition (JSON-LD format).
*   **Type Mapping:** Maps Schema.org primitive types (like `Text`, `Number`, `Date`, `URL`, `Boolean`) to appropriate Python types (`str`, `int | float`, `datetime.date`, `str`, `bool`).
*   **Class & Property Parsing:** Identifies Schema.org classes (`rdfs:Class`) and properties (`rdf:Property`).
*   **Inheritance Handling:** Resolves the class hierarchy (`rdfs:subClassOf`) to include properties from parent classes.
*   **Code Generation:** Generates Python files containing `msgspec.Struct` definitions corresponding to Schema.org types, including type hints and docstrings derived from `rdfs:comment`.

## Installation

*(Once packaged)*

```bash
pip install msgspec-schemaorg
```

*(From source, for development)*

```bash
# Clone the repository (if you haven't already)
# git clone <repository-url>
# cd msgspec-schemaorg

# Install dependencies (adjust based on final setup, e.g., using hatch, poetry, or requirements.txt)
pip install .
# or potentially:
# pip install -r requirements.txt
```

## Usage

1.  **Generate the Models:**
    Run the generation script. This will fetch the schema and create the Python model files (e.g., in `msgspec_schemaorg/models/`).

    ```bash
    python scripts/generate_models.py
    ```

2.  **Use the Generated Models:**
    Import and use the generated `Struct` classes in your Python code.

    ```python
    from msgspec import json
    # Assuming models are generated into msgspec_schemaorg.models.schema
    from msgspec_schemaorg.models.schema import Person, PostalAddress

    # Example data (as Python dict)
    person_data = {
        "@type": "Person",
        "name": "Jane Doe",
        "jobTitle": "Software Engineer",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "123 Main St",
            "addressLocality": "Anytown",
            "postalCode": "12345",
            "addressCountry": "US"
        }
    }

    # Decode JSON or dict data into msgspec Structs
    # Using msgspec.convert for dict -> Struct
    try:
        person_struct = json.decode(json.encode(person_data), type=Person)
        # Or directly from a dict if you trust the source structure:
        # from msgspec import convert
        # person_struct = convert(person_data, Person)

        print(f"Decoded Person: {person_struct.name}")
        print(f"Address: {person_struct.address.streetAddress}")

        # Encode Struct back to JSON (bytes)
        encoded_json = json.encode(person_struct)
        print(f"Encoded JSON: {encoded_json.decode()}")

    except Exception as e:
        print(f"Error processing data: {e}")

    ```

## Future Work

*   Improve handling of optional vs. required fields.
*   Add command-line arguments for customization (output directory, schema source).
*   Implement more sophisticated output file organization options.
*   Add comprehensive automated tests using `pytest`.
*   Optionally exclude or mark deprecated Schema.org terms.
*   Consider using `rdflib` for more robust JSON-LD graph processing if needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request. (Further details TBD)

## License

This project is licensed under the MIT License - see the LICENSE file for details. (Placeholder: Add LICENSE file)