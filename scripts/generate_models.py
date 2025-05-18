#!/usr/bin/env python3
"""
Script to download the Schema.org JSON-LD data and generate Python msgspec.Struct classes.
"""

import os
import sys
import json
import argparse
import requests
from pathlib import Path

# Add parent directory to path to allow imports from msgspec_schemaorg
sys.path.insert(0, str(Path(__file__).parent.parent))
from msgspec_schemaorg.generate import fetch_and_generate

# Default Schema.org URL and output file
DEFAULT_SCHEMA_URL = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "msgspec_schemaorg" / "models"
ENUMS_DIR = Path(__file__).parent.parent / "msgspec_schemaorg" / "enums"


def ensure_dir_exists(directory: Path):
    """Ensure the specified directory exists."""
    if not directory.exists():
        directory.mkdir(parents=True)
        print(f"Created directory: {directory}")


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


def get_existing_enum_types():
    """
    Get a list of types that already have enum implementations.

    Returns:
        A set of type names (without namespace) that have enum implementations
    """
    enum_types = set()

    if not ENUMS_DIR.exists():
        return enum_types

    # Walk through the enums directory to find all enum files
    for root, _, files in os.walk(ENUMS_DIR):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # Remove the .py extension to get the type name
                enum_name = os.path.splitext(file)[0]
                enum_types.add(enum_name)

    return enum_types


def get_enum_categories():
    """
    Get a mapping of enum types to their categories.

    Returns:
        A dictionary mapping enum type names to their categories
    """
    enum_categories = {}

    if not ENUMS_DIR.exists():
        return enum_categories

    for root, _, files in os.walk(ENUMS_DIR):
        category = os.path.basename(root)
        if category == "enums":  # Skip the root enums directory
            continue

        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                enum_name = os.path.splitext(file)[0]
                enum_categories[enum_name] = category

    return enum_categories


def modify_imports_for_enums(files, enum_types):
    """
    Modify import statements in generated files to use enum types from the enums package.

    Args:
        files: Dictionary mapping file paths to generated code
        enum_types: Set of type names that have enum implementations
    """
    # Get enum categories
    enum_categories = get_enum_categories()

    # Now update imports in all files
    for file_path, content in files.items():
        if file_path.name == "__init__.py":
            continue

        modified_content = content

        # Look for import statements for enum types
        for enum_type in enum_types:
            if enum_type not in enum_categories:
                continue

            category = enum_categories[enum_type]

            # Patterns for imports from models (handle various potential patterns)
            old_import_patterns = [
                f"from msgspec_schemaorg.models.intangible.{enum_type} import {enum_type}",
                f"from msgspec_schemaorg.models.{category}.{enum_type} import {enum_type}",
                f"from .{enum_type} import {enum_type}",
                f"from ..{category}.{enum_type} import {enum_type}",
            ]

            # Pattern for corrected import from enums
            new_import = f"from msgspec_schemaorg.enums.{category}.{enum_type} import {enum_type}"

            # Replace the import statement
            for old_pattern in old_import_patterns:
                if old_pattern in modified_content:
                    modified_content = modified_content.replace(old_pattern, new_import)
                    print(f"Updated import for {enum_type} in {file_path}")

        # Update the content in the files dictionary
        files[file_path] = modified_content


def modify_init_files(files, enum_types):
    """
    Modify __init__.py files to remove imports of enum types.

    Args:
        files: Dictionary mapping file paths to generated code
        enum_types: Set of type names that have enum implementations
    """
    for file_path, content in files.items():
        if file_path.name != "__init__.py":
            continue

        modified_content = content
        modified = False

        # Remove imports for enum types
        for enum_type in enum_types:
            import_line = f"from .{enum_type} import {enum_type}\n"
            if import_line in modified_content:
                modified_content = modified_content.replace(import_line, "")
                modified = True
                print(f"Removed import for {enum_type} in {file_path}")

        # Update __all__ list if present
        if "__all__ = [" in modified_content:
            # Find __all__ list
            all_list_start = modified_content.find("__all__ = [")
            all_list_end = modified_content.find("]", all_list_start)
            if all_list_end > all_list_start:  # Ensure we found the end bracket
                all_list = modified_content[all_list_start : all_list_end + 1]
                original_all_list = all_list

                # Remove enum types from __all__ list
                for enum_type in enum_types:
                    # Look for different patterns in __all__ list
                    patterns = [
                        f"'{enum_type}',",
                        f"'{enum_type}'",
                        f'"{enum_type}",',
                        f'"{enum_type}"',
                    ]

                    for pattern in patterns:
                        if pattern in all_list:
                            # Replace with empty string
                            all_list = all_list.replace(pattern, "")
                            modified = True
                            print(
                                f"Removed {enum_type} from __all__ list in {file_path}"
                            )

                # Clean up any empty commas or double commas
                all_list = all_list.replace(",,", ",")
                all_list = all_list.replace(", ,", ",")
                all_list = all_list.replace("[,", "[")
                all_list = all_list.replace(",]", "]")

                # Replace the old __all__ list with the cleaned up one
                if all_list != original_all_list:
                    modified_content = modified_content.replace(
                        original_all_list, all_list
                    )

        # Update the content in the files dictionary if modified
        if modified:
            files[file_path] = modified_content

    # Also update the root models/__init__.py if it exists
    root_init_path = Path(DEFAULT_OUTPUT_DIR) / "__init__.py"
    if root_init_path.exists():
        try:
            with open(root_init_path, "r") as f:
                root_init_content = f.read()

            modified_root_init = root_init_content
            modified = False

            # Update __all__ list if present
            if "__all__ = [" in modified_root_init:
                # Find __all__ list
                all_list_start = modified_root_init.find("__all__ = [")
                all_list_end = modified_root_init.find("]", all_list_start)
                if all_list_end > all_list_start:  # Ensure we found the end bracket
                    all_list = modified_root_init[all_list_start : all_list_end + 1]
                    original_all_list = all_list

                    # Remove enum types from __all__ list
                    for enum_type in enum_types:
                        patterns = [
                            f"'{enum_type}',",
                            f"'{enum_type}'",
                            f'"{enum_type}",',
                            f'"{enum_type}"',
                        ]

                        for pattern in patterns:
                            if pattern in all_list:
                                # Replace with empty string
                                all_list = all_list.replace(pattern, "")
                                modified = True
                                print(
                                    f"Removed {enum_type} from __all__ list in root __init__.py"
                                )

                    # Clean up any empty commas or double commas
                    all_list = all_list.replace(",,", ",")
                    all_list = all_list.replace(", ,", ",")
                    all_list = all_list.replace("[,", "[")
                    all_list = all_list.replace(",]", "]")

                    # Replace the old __all__ list with the cleaned up one
                    if all_list != original_all_list:
                        modified_root_init = modified_root_init.replace(
                            original_all_list, all_list
                        )

                # Write the modified content back to the file if changed
                if modified:
                    with open(root_init_path, "w") as f:
                        f.write(modified_root_init)
        except Exception as e:
            print(f"Error updating root __init__.py: {e}")


def save_outputs(files: dict[Path, str], enum_types: set):
    """
    Save the generated Python code to multiple files.

    Args:
        files: Dictionary mapping file paths to generated code
        enum_types: Set of type names that already have enum implementations
    """
    # First, modify import statements to use enum types from enums package
    modify_imports_for_enums(files, enum_types)

    # Then remove enum imports from __init__.py files
    modify_init_files(files, enum_types)

    # Count files by type for summary
    categories = {}
    skipped_enums = 0

    for file_path, content in files.items():
        # Skip if this is an enum type that already has an implementation
        if file_path.name != "__init__.py" and file_path.stem in enum_types:
            print(f"Skipping {file_path.stem} as it already has an enum implementation")
            skipped_enums += 1
            continue

        ensure_dir_exists(file_path.parent)

        with open(file_path, "w") as f:
            f.write(content)

        # Count for summary
        if file_path.name != "__init__.py":
            category = file_path.parent.name
            if category not in categories:
                categories[category] = 0
            categories[category] += 1

    # Print summary
    total_files = sum(count for _, count in categories.items())
    print(f"Generated {total_files} class files across {len(categories)} categories:")
    for category, count in sorted(categories.items()):
        print(f"  - {category}: {count} classes")

    if skipped_enums > 0:
        print(f"Skipped {skipped_enums} classes that already have enum implementations")


def main():
    """Main function to run the generate_models script."""
    parser = argparse.ArgumentParser(
        description="Generate Python msgspec.Struct classes from Schema.org vocabulary."
    )
    parser.add_argument(
        "--schema-url",
        default=DEFAULT_SCHEMA_URL,
        help=f"URL to download the Schema.org data from (default: {DEFAULT_SCHEMA_URL})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to save the generated code to (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--save-schema",
        action="store_true",
        help="Save the downloaded Schema.org data to a JSON file",
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

    parser.add_argument(
        "--include-enums",
        action="store_true",
        help="Generate Struct classes even for types that have enum implementations",
    )

    args = parser.parse_args()

    try:  # Clean output directory if requested
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
        # Download schema
        schema_data = download_schema(args.schema_url)

        # Save schema data if requested
        if args.save_schema:
            schema_file = args.output_dir / "schema.json"
            ensure_dir_exists(args.output_dir)
            with open(schema_file, "w") as f:
                json.dump(schema_data, f, indent=2)
            print(f"Saved schema data to {schema_file}")

        # Get types that already have enum implementations
        enum_types = set() if args.include_enums else get_existing_enum_types()

        # Generate Python code
        print("Generating Python code...")
        generated_files = fetch_and_generate(schema_data, args.output_dir)

        # Save generated files
        save_outputs(generated_files, enum_types)

        print(f"Code generation completed successfully.")

    except requests.RequestException as e:
        print(f"Error downloading Schema.org data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
