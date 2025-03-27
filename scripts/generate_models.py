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


def save_outputs(files: dict[Path, str]):
    """
    Save the generated Python code to multiple files.
    
    Args:
        files: Dictionary mapping file paths to generated code
    """
    # Count files by type for summary
    categories = {}
    
    for file_path, content in files.items():
        ensure_dir_exists(file_path.parent)
        
        with open(file_path, 'w') as f:
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


def main():
    """Main function to run the generate_models script."""
    parser = argparse.ArgumentParser(description='Generate Python msgspec.Struct classes from Schema.org vocabulary.')
    parser.add_argument('--schema-url', default=DEFAULT_SCHEMA_URL,
                       help=f'URL to download the Schema.org data from (default: {DEFAULT_SCHEMA_URL})')
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT_DIR,
                       help=f'Directory to save the generated code to (default: {DEFAULT_OUTPUT_DIR})')
    parser.add_argument('--save-schema', action='store_true',
                       help='Save the downloaded Schema.org data to a JSON file')
    parser.add_argument('--clean', action='store_true',
                       help='Clean output directory before generating files')
    
    args = parser.parse_args()
    
    try:
        # Clean output directory if requested
        if args.clean and args.output_dir.exists():
            import shutil
            print(f"Cleaning output directory: {args.output_dir}")
            for item in args.output_dir.glob('*'):
                if item.is_dir() and not item.name.startswith('__'):
                    shutil.rmtree(item)
                elif item.is_file() and not item.name.startswith('__'):
                    item.unlink()
        
        # Download schema
        schema_data = download_schema(args.schema_url)
        
        # Save schema data if requested
        if args.save_schema:
            schema_file = args.output_dir / "schema.json"
            ensure_dir_exists(args.output_dir)
            with open(schema_file, 'w') as f:
                json.dump(schema_data, f, indent=2)
            print(f"Saved schema data to {schema_file}")
        
        # Generate Python code
        print("Generating Python code...")
        generated_files = fetch_and_generate(schema_data, args.output_dir)
        
        # Save generated files
        save_outputs(generated_files)
        
        print(f"Code generation completed successfully.")
        
    except requests.RequestException as e:
        print(f"Error downloading Schema.org data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
