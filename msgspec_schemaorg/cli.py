#!/usr/bin/env python3
"""
Command-line interface for msgspec-schemaorg.

This module provides CLI commands for generating Schema.org models
and other utilities.
"""

import sys
import argparse
from pathlib import Path

from .generate import SchemaProcessor

def generate_models_command():
    """
    Command-line entry point for generating Schema.org models.
    
    This function parses command-line arguments and runs the model generation process.
    """
    parser = argparse.ArgumentParser(
        description="Generate msgspec.Struct models from Schema.org vocabulary."
    )
    
    parser.add_argument(
        "--schema-url",
        default="https://schema.org/version/latest/schemaorg-current-https.jsonld",
        help="URL to download Schema.org data (default: %(default)s)",
    )
    
    parser.add_argument(
        "--output-dir",
        default="msgspec_schemaorg/models",
        help="Directory to save generated code (default: %(default)s)",
    )
    
    parser.add_argument(
        "--save-schema",
        action="store_true",
        help="Save the downloaded Schema.org data to a JSON file",
    )
    
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean the output directory before generating new files",
    )
    
    parser.add_argument(
        "--categories",
        nargs="+",
        help="Specific categories to generate (e.g., person organization)",
    )
    
    args = parser.parse_args()
    
    try:
        processor = SchemaProcessor(
            schema_url=args.schema_url,
            output_dir=args.output_dir,
            save_schema=args.save_schema,
        )
        
        if args.clean:
            print(f"Cleaning output directory: {args.output_dir}")
            processor.clean_output_dir()
            
        processor.generate_code(categories=args.categories)
        print("Code generation completed successfully!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    generate_models_command() 