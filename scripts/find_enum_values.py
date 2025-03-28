#!/usr/bin/env python3
"""
Script to find enumeration values in the Schema.org data.
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


def find_enum_types_and_values(schema_data: dict):
    """
    Find enumeration types and their values in the Schema.org data.
    
    Args:
        schema_data: The loaded JSON-LD Schema.org data
    """
    graph = schema_data.get('@graph', [])
    
    # Create SchemaProcessor to get class information
    processor = SchemaProcessor(schema_data)
    
    # Find all Enumeration types
    enumeration_types = set()
    
    for class_id, class_info in processor.classes.items():
        # Check if this class inherits from Enumeration directly or indirectly
        parent_ids = processor._get_parent_classes(class_id)
        if 'schema:Enumeration' in parent_ids or 'http://schema.org/Enumeration' in parent_ids:
            enumeration_types.add(class_id)
            class_name = processor.normalized_class_names.get(class_id, "Unknown")
            print(f"Found enumeration type: {class_id} -> {class_name}")
    
    print(f"\nFound {len(enumeration_types)} enumeration types\n")
    
    # Find all enumeration values
    enum_values = defaultdict(list)
    
    for entity in graph:
        entity_type = entity.get('@type', None)
        
        # Skip if not a type we're interested in
        if not entity_type:
            continue
            
        # Convert to list if it's not already
        if not isinstance(entity_type, list):
            entity_type = [entity_type]
        
        # Check if this entity is an instance of any enumeration type
        for enum_type in enumeration_types:
            enum_type_short = enum_type.split('/')[-1]
            if isinstance(enum_type_short, str) and ':' in enum_type_short:
                enum_type_short = enum_type_short.split(':')[-1]
                
            for t in entity_type:
                if isinstance(t, str) and (t == enum_type_short or t == enum_type):
                    # This is a value of an enumeration type
                    entity_id = entity.get('@id', '')
                    entity_label = entity.get('rdfs:label', '')
                    entity_comment = entity.get('rdfs:comment', '')
                    
                    if entity_id:
                        enum_values[enum_type].append({
                            'id': entity_id,
                            'label': entity_label,
                            'comment': entity_comment
                        })
                    break
    
    # Print found enumeration values
    print("\n=== Enumeration Values ===\n")
    
    total_values = 0
    for enum_type, values in sorted(enum_values.items()):
        enum_name = processor.normalized_class_names.get(enum_type, "Unknown")
        print(f"{enum_name} ({enum_type}):")
        for value in values:
            total_values += 1
            value_id = value['id'].split('/')[-1]
            if ':' in value_id:
                value_id = value_id.split(':')[-1]
            print(f"  - {value_id}: {value['comment']}")
        print()
    
    print(f"Found {total_values} enumeration values for {len(enum_values)} enumeration types")
    
    # Check for enumeration types with no values
    enum_types_with_no_values = enumeration_types - set(enum_values.keys())
    if enum_types_with_no_values:
        print("\n=== Enumeration Types with No Values ===\n")
        for enum_type in sorted(enum_types_with_no_values):
            enum_name = processor.normalized_class_names.get(enum_type, "Unknown")
            print(f"{enum_name} ({enum_type})")
        
        print(f"\nFound {len(enum_types_with_no_values)} enumeration types with no values")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Find enumeration values in the Schema.org data.')
    parser.add_argument('--schema-url', default=DEFAULT_SCHEMA_URL,
                       help=f'URL to download the Schema.org data from (default: {DEFAULT_SCHEMA_URL})')
    parser.add_argument('--schema-file', type=str,
                       help='Path to a local Schema.org JSON-LD file (overrides --schema-url if specified)')
    
    args = parser.parse_args()
    
    try:
        # Load schema data from file or download it
        if args.schema_file:
            with open(args.schema_file, 'r') as f:
                schema_data = json.load(f)
            print(f"Loaded Schema.org data from {args.schema_file}")
        else:
            schema_data = download_schema(args.schema_url)
        
        # Find enumeration types and values
        find_enum_types_and_values(schema_data)
        
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