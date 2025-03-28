#!/usr/bin/env python3
"""
Script to find Schema.org types that weren't generated as model classes.
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
DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "msgspec_schemaorg" / "models"


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


def find_missing_types(schema_data: dict, output_dir: Path):
    """
    Find Schema.org types that weren't generated as model classes.
    
    Args:
        schema_data: The loaded JSON-LD Schema.org data
        output_dir: Directory where model files are saved
    """
    # Initialize SchemaProcessor to get all class information
    processor = SchemaProcessor(schema_data)
    
    # Get all classes from the schema
    all_schema_classes = set(processor.classes.keys())
    
    # Get all classes that were successfully normalized
    normalized_classes = {
        class_id for class_id, class_name in processor.normalized_class_names.items()
        if class_name != "Unknown"
    }
    
    # Identify classes that were skipped during normalization
    skipped_during_normalization = all_schema_classes - normalized_classes
    
    # Find all generated Python files
    generated_files = set()
    for category_dir in output_dir.glob('*'):
        if category_dir.is_dir() and not category_dir.name.startswith('__'):
            for py_file in category_dir.glob('*.py'):
                if py_file.name != '__init__.py':
                    generated_files.add(py_file.stem)
    
    # Identify classes that were normalized but not generated
    normalized_class_names = set(processor.normalized_class_names.values())
    generated_class_names = generated_files
    not_generated = normalized_class_names - generated_class_names - {'Unknown'}
    
    # Count by category
    category_counts = defaultdict(lambda: {"total": 0, "missing": 0})
    for class_id in all_schema_classes:
        category = processor.class_categories.get(class_id, 'misc')
        category_counts[category]["total"] += 1
        
        class_name = processor.normalized_class_names.get(class_id)
        if class_name not in generated_class_names and class_name != 'Unknown':
            category_counts[category]["missing"] += 1
    
    # Print results
    print("\n=== Missing Types Analysis ===\n")
    
    print(f"Total Schema.org classes found: {len(all_schema_classes)}")
    print(f"Classes successfully normalized: {len(normalized_classes)} ({len(normalized_classes)/len(all_schema_classes):.1%})")
    print(f"Classes skipped during normalization: {len(skipped_during_normalization)} ({len(skipped_during_normalization)/len(all_schema_classes):.1%})")
    print(f"Classes generated to Python files: {len(generated_class_names)}")
    print(f"Normalized classes that weren't generated: {len(not_generated)} ({len(not_generated)/len(normalized_classes):.1%} of normalized)")
    
    # Print details by category
    print("\n=== Missing Types by Category ===\n")
    print(f"{'Category':<15} {'Total':<10} {'Generated':<10} {'Missing':<10} {'Coverage':<10}")
    print(f"{'-'*15} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")
    
    for category, counts in sorted(category_counts.items()):
        total = counts["total"]
        missing = counts["missing"]
        generated = total - missing
        coverage = (generated / total) if total > 0 else 0
        print(f"{category:<15} {total:<10} {generated:<10} {missing:<10} {coverage:.1%}")
    
    # Print details of missing classes if requested
    if skipped_during_normalization:
        print("\n=== Classes Skipped During Normalization ===\n")
        for class_id in sorted(skipped_during_normalization):
            print(f"  {class_id}")
    
    if not_generated:
        print("\n=== Normalized Classes That Weren't Generated ===\n")
        for class_name in sorted(not_generated):
            # Find original class_id
            original_id = None
            for class_id, norm_name in processor.normalized_class_names.items():
                if norm_name == class_name:
                    original_id = class_id
                    break
            
            if original_id:
                print(f"  {class_name} (from {original_id})")
            else:
                print(f"  {class_name}")
            

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Find Schema.org types that weren\'t generated as model classes.')
    parser.add_argument('--schema-url', default=DEFAULT_SCHEMA_URL,
                       help=f'URL to download the Schema.org data from (default: {DEFAULT_SCHEMA_URL})')
    parser.add_argument('--schema-file', type=str,
                       help='Path to a local Schema.org JSON-LD file (overrides --schema-url if specified)')
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT_DIR,
                       help=f'Directory where model files are saved (default: {DEFAULT_OUTPUT_DIR})')
    
    args = parser.parse_args()
    
    try:
        # Load schema data from file or download it
        if args.schema_file:
            with open(args.schema_file, 'r') as f:
                schema_data = json.load(f)
            print(f"Loaded Schema.org data from {args.schema_file}")
        else:
            schema_data = download_schema(args.schema_url)
        
        # Find missing types
        find_missing_types(schema_data, args.output_dir)
        
    except requests.RequestException as e:
        print(f"Error downloading Schema.org data: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing Schema.org data: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 