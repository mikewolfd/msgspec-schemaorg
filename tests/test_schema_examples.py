#!/usr/bin/env python3
"""
Test Schema.org models against real examples from schema.org.
"""

import importlib
import inspect
import json
import os
import re
import sys
from collections.abc import Iterator
from typing import Union, Any, Dict, List, Optional

import requests
from requests import Response
import msgspec
import pytest

# Ensure we can import from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try to import models
try:
    from msgspec_schemaorg.models import *
except ImportError:
    print("Models not found. Please generate them first by running scripts/generate_models.py")
    sys.exit(1)


def get_modules_in_package(package_name: str) -> Iterator[Any]:
    """
    Get all classes from a package.
    
    Args:
        package_name: The name of the package to get modules from.
        
    Returns:
        An iterator of all classes in the package.
    """
    package = importlib.import_module(package_name)
    
    # Get all the classes defined in __all__
    for attr_name in getattr(package, "__all__", []):
        try:
            cls = getattr(package, attr_name)
            if isinstance(cls, type) and issubclass(cls, msgspec.Struct):
                yield cls
        except (AttributeError, TypeError):
            continue


def get_all_examples() -> Iterator[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    """
    Get all examples from schema.org.
    
    Returns:
        An iterator of all examples from schema.org.
    """
    schema_org_request: Response = requests.get(
        "https://schema.org/version/latest/schemaorg-all-examples.txt"
    )
    content = schema_org_request.text
    matches = re.findall(
        r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>',
        content,
        flags=re.DOTALL | re.M,
    )
    for match in matches:
        m = match
        m = m.replace("\n", "")
        try:
            b = json.loads(m)
            yield b
        except json.JSONDecodeError:
            print(f"Failed to decode JSON: {m[:100]}...")
            continue


def clean_json_ld(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean JSON-LD data for use with msgspec.
    
    Args:
        data: The data to clean.
        
    Returns:
        The cleaned data.
    """
    result = {}
    for key, value in data.items():
        # Skip JSON-LD specific fields
        if key.startswith('@'):
            continue
        
        # Handle nested objects
        if isinstance(value, dict):
            value = clean_json_ld(value)
        elif isinstance(value, list):
            value = [clean_json_ld(item) if isinstance(item, dict) else item for item in value]
        
        # Convert snake_case to camelCase for property names
        if '_' in key:
            camel_key = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(key.split('_')))
        else:
            camel_key = key
            
        result[camel_key] = value
    
    return result


def test_examples():
    """
    Test all examples from schema.org.
    """
    # Map of class names to class objects
    class_map = {}
    for cls in get_modules_in_package("msgspec_schemaorg.models"):
        class_map[cls.__name__] = cls
    
    success_count = 0
    failure_count = 0
    skipped_count = 0
    
    for example in get_all_examples():
        if isinstance(example, dict) and not isinstance(example.get("@type"), list):
            type_str = example.get("@type", "")
            # Handle potential namespace prefixes like schema:Person
            if ":" in type_str:
                type_str = type_str.split(":")[-1]
            if not type_str:
                print(f"Skipping example with no @type field: {example.get('@id', 'unknown')}")
                skipped_count += 1
                continue
            
            # Check if we have a model for this type
            if type_str not in class_map:
                print(f"Skipping example with unknown type: {type_str}")
                skipped_count += 1
                continue
            
            try:
                # Clean the example data
                clean_data = clean_json_ld(example)
                
                # Create an instance of the model
                model_class = class_map[type_str]
                model = model_class(**clean_data)
                
                # Test encoding to JSON
                json_data = msgspec.json.encode(model)
                
                print(f"✓ Success for {type_str}")
                success_count += 1
            except Exception as e:
                print(f"✗ Exception for type {type_str}: {str(e)}")
                failure_count += 1
    
    print(f"\nSummary: {success_count} successes, {failure_count} failures, {skipped_count} skipped")


def test_all_classes():
    """
    Test that all classes can be instantiated with default values.
    """
    success_count = 0
    failure_count = 0
    
    for cls in get_modules_in_package("msgspec_schemaorg.models"):
        try:
            instance = cls()
            # Test encoding to JSON
            json_data = msgspec.json.encode(instance)
            print(f"✓ Class {cls.__name__} passed instantiation test")
            success_count += 1
        except Exception as e:
            print(f"✗ Class {cls.__name__} failed instantiation test: {str(e)}")
            failure_count += 1
    
    print(f"\nSummary: {success_count} successes, {failure_count} failures")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--all-classes":
        test_all_classes()
    else:
        test_examples() 