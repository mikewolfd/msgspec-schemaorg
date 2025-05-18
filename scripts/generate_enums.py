#!/usr/bin/env python3
"""
Script to generate Python enum classes for Schema.org enumeration types.
"""

import sys
import json
import argparse
import requests
from pathlib import Path
from collections import defaultdict

# Add parent directory to path to allow imports from msgspec_schemaorg
sys.path.insert(0, str(Path(__file__).parent.parent))
from msgspec_schemaorg.generate import SchemaProcessor

# Default Schema.org URL
DEFAULT_SCHEMA_URL = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "msgspec_schemaorg" / "enums"


def download_schema(url: str = DEFAULT_SCHEMA_URL) -> dict:
    """
    Download the Schema.org JSON-LD data.

    Args:
        url: URL to download the Schema.org data from

    Returns:
        Parsed JSON data
    """
    print(f"Downloading Schema.org data from {url}...")
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    print("Schema.org data downloaded successfully.")
    return response.json()


def ensure_dir_exists(directory: Path):
    """Ensure the specified directory exists."""
    if not directory.exists():
        directory.mkdir(parents=True)
        print(f"Created directory: {directory}")


def generate_enum_code(enum_type: str, values: list, category: str = None):
    """
    Generate Python enum class code for a Schema.org enumeration type.

    Args:
        enum_type: The name of the enumeration type
        values: List of enumeration values with their metadata
        category: Optional category for organizing imports

    Returns:
        Generated Python code for the enum class
    """
    # Sort values by ID for consistent ordering
    values = sorted(values, key=lambda x: x["id"])

    # Prepare the enum class code
    code = [
        "import enum",
        "from typing import ClassVar, Dict, Any\n",
        f"class {enum_type}(str, enum.Enum):",
        f'    """Schema.org enumeration values for {enum_type}."""\n',
    ]

    # Add enum values
    for value in values:
        value_id = value["id"].split("/")[-1]
        if ":" in value_id:
            value_id = value_id.split(":")[-1]

        # Clean up the comment if present
        comment = value.get("comment", "")
        if comment and isinstance(comment, str):
            # Truncate long comments and escape quotes
            if len(comment) > 60:
                comment = comment[:57] + "..."
            comment = comment.replace('"', '\\"')
            comment_str = f'  # "{comment}"'
        else:
            comment_str = ""

        # Add the enum value
        code.append(f'    {value_id} = "{value_id}"{comment_str}')

    # Add metadata dictionary
    code.append("\n    # Metadata for each enum value")
    code.append("    metadata: ClassVar[Dict[str, Dict[str, Any]]] = {")

    for value in values:
        value_id = value["id"].split("/")[-1]
        if ":" in value_id:
            value_id = value_id.split(":")[-1]

        # Get comment and ensure it's a string
        comment = value.get("comment", "")
        if not isinstance(comment, str):
            comment = str(comment)

        # Use triple quotes for comment to properly handle multi-line text
        code.append(f'        "{value_id}": {{')
        code.append(f'            "id": "{value["id"]}",')
        code.append(f'            "comment": """{comment}""",')
        if value.get("label"):
            label = str(value["label"]).replace('"', '\\"')
            code.append(f'            "label": "{label}",')
        code.append("        },")

    code.append("    }")

    return "\n".join(code)


def generate_enums(schema_data: dict, output_dir: Path):
    """
    Generate Python enum classes for Schema.org enumeration types.

    Args:
        schema_data: The loaded JSON-LD Schema.org data
        output_dir: Directory to save the generated enum classes
    """
    graph = schema_data.get("@graph", [])

    # Create SchemaProcessor to get class information
    processor = SchemaProcessor(schema_data)

    # Find all Enumeration types
    enumeration_types = set()

    for class_id, class_info in processor.classes.items():
        # Check if this class inherits from Enumeration directly or indirectly
        parent_ids = processor._get_parent_classes(class_id)
        if (
            "schema:Enumeration" in parent_ids
            or "http://schema.org/Enumeration" in parent_ids
        ):
            enumeration_types.add(class_id)

    print(f"Found {len(enumeration_types)} enumeration types")

    # Find all enumeration values
    enum_values = defaultdict(list)

    for entity in graph:
        entity_type = entity.get("@type", None)

        # Skip if not a type we're interested in
        if not entity_type:
            continue

        # Convert to list if it's not already
        if not isinstance(entity_type, list):
            entity_type = [entity_type]

        # Check if this entity is an instance of any enumeration type
        for enum_type in enumeration_types:
            enum_type_short = enum_type.split("/")[-1]
            if isinstance(enum_type_short, str) and ":" in enum_type_short:
                enum_type_short = enum_type_short.split(":")[-1]

            for t in entity_type:
                if isinstance(t, str) and (t == enum_type_short or t == enum_type):
                    # This is a value of an enumeration type
                    entity_id = entity.get("@id", "")
                    entity_label = entity.get("rdfs:label", "")
                    entity_comment = entity.get("rdfs:comment", "")

                    if entity_id:
                        enum_values[enum_type].append(
                            {
                                "id": entity_id,
                                "label": entity_label,
                                "comment": entity_comment,
                            }
                        )
                    break

    # Determine organization by category
    enum_categories = {}
    for enum_type in enum_values:
        category = processor.class_categories.get(enum_type, "misc")
        enum_categories[enum_type] = category

    # Create directory structure for enum modules
    for category in set(enum_categories.values()):
        category_dir = output_dir / category
        ensure_dir_exists(category_dir)

        # Create __init__.py for each category
        with open(category_dir / "__init__.py", "w") as f:
            f.write(f'"""Schema.org {category} enumeration types."""\n\n')

    # Generate enum modules for each enumeration type with values
    enum_modules = {}

    for enum_type, values in enum_values.items():
        if not values:
            continue  # Skip enums with no values

        # Get normalized class name
        enum_name = processor.normalized_class_names.get(enum_type, "Unknown")
        if enum_name == "Unknown":
            continue

        # Get category for this enum
        category = enum_categories.get(enum_type, "misc")

        # Generate enum code
        enum_code = generate_enum_code(enum_name, values, category)

        # Save enum module
        category_dir = output_dir / category
        enum_file = category_dir / f"{enum_name}.py"

        with open(enum_file, "w") as f:
            f.write(enum_code)

        # Update __init__.py for this category to import the enum
        with open(category_dir / "__init__.py", "a") as f:
            f.write(f"from .{enum_name} import {enum_name}\n")

        # Track generated modules
        enum_modules[enum_type] = (enum_name, category)

        print(f"Generated enum class for {enum_name} with {len(values)} values")

    # Create main __init__.py
    with open(output_dir / "__init__.py", "w") as f:
        f.write('"""Schema.org enumeration types."""\n\n')

        # Import enums from each category
        for category in sorted(set(enum_categories.values())):
            f.write(f"from . import {category}\n")

        f.write("\n# Import all enum classes directly\n")
        for category in sorted(set(enum_categories.values())):
            f.write(f"from .{category} import *\n")

        # Add __all__ list
        f.write("\n__all__ = [\n")

        # Add categories
        for category in sorted(set(enum_categories.values())):
            f.write(f"    '{category}',\n")

        # Add enum classes
        for enum_type, (enum_name, _) in sorted(enum_modules.items()):
            f.write(f"    '{enum_name}',\n")

        f.write("]\n")

    print(
        f"\nGenerated {len(enum_modules)} enum classes across {len(set(enum_categories.values()))} categories"
    )


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Generate Python enum classes for Schema.org enumeration types."
    )
    parser.add_argument(
        "--schema-url",
        default=DEFAULT_SCHEMA_URL,
        help=f"URL to download the Schema.org data from (default: {DEFAULT_SCHEMA_URL})",
    )
    parser.add_argument(
        "--schema-file",
        type=str,
        help="Path to a local Schema.org JSON-LD file (overrides --schema-url if specified)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to save the generated enum classes (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean output directory before generating files",
    )
    parser.add_argument(
        "--no-generate",
        action="store_true",
        help="Do not generate any code",
    )

    args = parser.parse_args()

    try:
        if args.clean and args.output_dir.exists():
            import shutil

            print(f"Cleaning output directory: {args.output_dir}")
            for item in args.output_dir.glob("*"):
                if item.is_dir() and not item.name.startswith("__"):
                    shutil.rmtree(item)
                elif item.is_file() and not item.name.startswith("__"):
                    item.unlink()
        if args.no_generate:
            print("No code generated")
            return
        # Load schema data from file or download it
        if args.schema_file:
            with open(args.schema_file, "r") as f:
                schema_data = json.load(f)
            print(f"Loaded Schema.org data from {args.schema_file}")
        else:
            schema_data = download_schema(args.schema_url)

        # Create output directory if it doesn't exist
        ensure_dir_exists(args.output_dir)

        # Generate enum classes
        generate_enums(schema_data, args.output_dir)

    except requests.RequestException as e:
        print(f"Error downloading Schema.org data: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing Schema.org data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
