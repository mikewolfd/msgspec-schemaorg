# Plan for msgspec-schemaorg Implementation

This document outlines the steps to create the `msgspec-schemaorg` tool, which generates `msgspec.Struct` definitions from the Schema.org vocabulary.

## Phase 1: Project Setup & Foundation

1.  **Initialize Project Structure:**
    *   Create directories: `msgspec_schemaorg/`, `msgspec_schemaorg/models/`, `scripts/`.
    *   Create empty files: `msgspec_schemaorg/__init__.py`, `msgspec_schemaorg/generate.py`, `msgspec_schemaorg/mapping.py`, `scripts/generate_models.py`.
2.  **Configure `pyproject.toml`:**
    *   Add project metadata (name, version, description).
    *   Define dependencies: `msgspec`, `requests`. Consider `rdflib` if advanced JSON-LD parsing is required, but start without it for simplicity.
    *   Configure build system (e.g., `hatchling`).
3.  **Create Initial `README.md`:**
    *   Add a brief description of the project's goal.
4.  **Create `plan.md` (This file).**

## Phase 2: Schema Acquisition & Mapping

1.  **Implement Schema Fetching:**
    *   In `scripts/generate_models.py` (or a utility function), add code using `requests` to download `schema.jsonld` (or the latest version) from `schema.org`.
    *   Store the downloaded schema temporarily or process it in memory.
2.  **Define Type Mapping:**
    *   In `msgspec_schemaorg/mapping.py`, create a dictionary or similar structure mapping Schema.org primitive types (e.g., `schema:Text`, `schema:Number`, `schema:Date`, `schema:URL`) to corresponding Python types (`str`, `int | float`, `datetime.date`, `str`). Include mappings for `Boolean`, `DateTime`, `Time`.

## Phase 3: Core Generation Logic

1.  **Implement Schema Parsing (`msgspec_schemaorg/generate.py`):**
    *   Load the downloaded JSON-LD data using Python's `json` module.
    *   Assume the main content is within a `@graph` array.
    *   Create helper functions or a class to easily look up entities (classes, properties) by their `@id`.
2.  **Implement Class & Property Processing (`msgspec_schemaorg/generate.py`):**
    *   Identify all entities with `@type` of `rdfs:Class`.
    *   Identify all entities with `@type` of `rdf:Property`.
    *   Process `schema:domainIncludes` and `schema:rangeIncludes` for each property to determine which classes it belongs to and what its possible types are. Use the type mapping defined in Phase 2. Handle multiple types using `|` (Union syntax). Map Schema.org class references (e.g., `schema:Person`) to the corresponding generated `Struct` name.
3.  **Implement Inheritance Handling (`msgspec_schemaorg/generate.py`):**
    *   Develop a function that, given a class ID, recursively finds all parent classes using `rdfs:subClassOf`.
    *   Modify the property processing to collect properties from the current class *and* all its ancestors. Ensure properties are not duplicated.
4.  **Implement Struct Code Generation (`msgspec_schemaorg/generate.py`):**
    *   For each Schema.org class, generate the Python code string for a `msgspec.Struct`.
    *   Include necessary imports (`msgspec`, `datetime`, `typing` for `Union` if needed, potentially forward references using `from __future__ import annotations`).
    *   Define fields based on the collected properties, using correct Python type hints (including `| None` for optional fields - assume optionality for now, refinement later).
    *   Add docstrings from `rdfs:comment`.
    *   Ensure correct formatting and syntax.
5.  **Implement File Writing (`msgspec_schemaorg/generate.py`):**
    *   Decide on a file organization strategy (e.g., one file per class, group by hierarchy, single large file). Start with a single file for simplicity (`msgspec_schemaorg/models/schema.py`).
    *   Write the generated Python code strings to the target `.py` file(s). Create `__init__.py` files as needed.

## Phase 4: Orchestration & Execution

1.  **Develop Runner Script (`scripts/generate_models.py`):**
    *   Add basic execution logic:
        *   Call the schema fetching function.
        *   Load/parse the schema data.
        *   Instantiate the generator logic from `msgspec_schemaorg/generate.py`.
        *   Run the generation process, passing the parsed schema data.
        *   Write the output to the designated file(s).
    *   Include basic error handling and print statements for progress indication.

## Phase 5: Testing & Documentation

1.  **Add Basic Tests (Manual for now):**
    *   After generation, manually create a small Python script that imports a few generated `Struct`s.
    *   Try instantiating them, encoding to JSON (`msgspec.json.encode`), and decoding valid/invalid JSON (`msgspec.json.decode`) to ensure basic functionality.
2.  **Update `README.md`:**
    *   Provide clear instructions on how to install dependencies (`pip install .` or `pip install -r requirements.txt` if created).
    *   Explain how to run the `scripts/generate_models.py` script.
    *   Show a basic example of importing and using a generated `Struct`.

## Phase 6: Refinement (Future Steps)

1.  **Improve Optionality:** Determine field optionality more accurately (Schema.org doesn't explicitly mark required fields, often requires interpretation or convention).
2.  **Add Command-Line Arguments:** Use `argparse` in `scripts/generate_models.py` for options like output directory, schema URL/file path.
3.  **Enhance File Organization:** Implement more sophisticated output file structures if needed.
4.  **Automated Testing:** Introduce `pytest` for automated testing of the generation process and the generated models.
5.  **Handle Deprecated Terms:** Add logic to optionally exclude or mark deprecated Schema.org terms.
6.  **Consider `rdflib`:** If simple JSON parsing proves insufficient for handling complex relationships or edge cases, integrate `rdflib` for more robust graph processing.

