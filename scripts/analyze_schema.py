#!/usr/bin/env python3
"""
Script to analyze the raw Schema.org data structure.
This helps understand what entities are available and their counts.
"""

import sys
import json
import argparse
import requests
from pathlib import Path
from collections import defaultdict, Counter

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


def analyze_schema(schema_data: dict):
    """
    Analyze the Schema.org data structure and print statistics.
    
    Args:
        schema_data: The loaded JSON-LD Schema.org data
    """
    graph = schema_data.get('@graph', [])
    
    # Count entities by type
    entity_types = Counter()
    
    # Count various properties and relationships
    has_comment = 0
    has_subclass = 0
    has_parent = 0
    has_domain = 0
    has_range = 0
    
    # Count classes by category
    top_level_categories = {
        'schema:CreativeWork': 'creativework', 
        'schema:Event': 'event',
        'schema:Organization': 'organization',
        'schema:Person': 'person',
        'schema:Place': 'place',
        'schema:Product': 'product',
        'schema:Intangible': 'intangible',
        'schema:Action': 'action',
        'schema:Thing': 'thing'
    }
    
    class_by_category = defaultdict(list)
    
    # Analyze entire graph
    for entity in graph:
        # Count entity types
        entity_type = entity.get('@type', 'Unknown')
        # Make entity_type hashable (convert list to tuple if needed)
        if isinstance(entity_type, list):
            entity_types[str(entity_type)] += 1
        else:
            entity_types[entity_type] += 1
        
        # Count entities with comments
        if 'rdfs:comment' in entity:
            has_comment += 1
            
            # Check for non-string comments
            if not isinstance(entity['rdfs:comment'], str):
                print(f"Warning: Non-string comment found: {type(entity['rdfs:comment'])}")
                
        # Count classes with subclasses
        if entity_type == 'rdfs:Class':
            entity_id = entity.get('@id', '')
            
            # Check for subclass relationship
            if 'rdfs:subClassOf' in entity:
                has_parent += 1
                
                # Determine category based on ancestry
                parent = entity['rdfs:subClassOf']
                if isinstance(parent, list):
                    for p in parent:
                        if isinstance(p, dict) and '@id' in p:
                            parent_id = p['@id']
                            if parent_id in top_level_categories:
                                class_by_category[top_level_categories[parent_id]].append(entity_id)
                                break
                elif isinstance(parent, dict) and '@id' in parent:
                    parent_id = parent['@id']
                    if parent_id in top_level_categories:
                        class_by_category[top_level_categories[parent_id]].append(entity_id)
            
            # If direct top-level class
            if entity_id in top_level_categories:
                class_by_category[top_level_categories[entity_id]].append(entity_id)
        
        # Count property domains and ranges
        if entity_type == 'rdf:Property':
            if 'schema:domainIncludes' in entity:
                has_domain += 1
            if 'schema:rangeIncludes' in entity:
                has_range += 1
    
    # Count datatype and enumeration entities
    datatypes = [e for e in graph if e.get('@type') == 'rdfs:Class' and 
                 any(p.get('@id') == 'schema:DataType' for p in e.get('rdfs:subClassOf', []) 
                     if isinstance(p, dict) and '@id' in p)]
    
    enumerations = [e for e in graph if e.get('@type') == 'rdfs:Class' and 
                    any(p.get('@id') == 'schema:Enumeration' for p in e.get('rdfs:subClassOf', []) 
                        if isinstance(p, dict) and '@id' in p)]
    
    # Print summary
    print("\n=== Schema.org Entity Analysis ===\n")
    print(f"Total entities in graph: {len(graph)}")
    
    print("\n=== Entity Types ===\n")
    for entity_type, count in entity_types.most_common():
        print(f"{entity_type}: {count}")
    
    print("\n=== Class Categories ===\n")
    print("Category       | Count")
    print("---------------|------")
    total_categorized = 0
    for category, classes in sorted(class_by_category.items()):
        print(f"{category:14} | {len(classes)}")
        total_categorized += len(classes)
    
    uncategorized = entity_types.get('rdfs:Class', 0) - total_categorized
    print(f"{'uncategorized':14} | {uncategorized}")
    
    print("\n=== Special Types ===\n")
    print(f"DataType classes: {len(datatypes)}")
    print(f"Enumeration classes: {len(enumerations)}")
    
    print("\n=== Property Statistics ===\n")
    print(f"Total properties: {entity_types.get('rdf:Property', 0)}")
    print(f"Properties with domain: {has_domain}")
    print(f"Properties with range: {has_range}")
    
    print("\n=== Documentation ===\n")
    print(f"Entities with comments: {has_comment} ({has_comment/len(graph):.1%} of total)")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Analyze the raw Schema.org data structure.')
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
        
        # Analyze schema data
        analyze_schema(schema_data)
        
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