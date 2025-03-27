#!/usr/bin/env python3
"""
Test Schema.org models against real examples using pytest.
"""

import importlib
import json
import os
import re
import sys
from typing import Any, Dict, List, Union, Iterator

import pytest
import requests
import msgspec

# Ensure we can import from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try to import models
try:
    from msgspec_schemaorg.models import *
except ImportError:
    pytest.skip("Models not found. Please generate them first by running scripts/generate_models.py", allow_module_level=True)


def get_msgspec_classes() -> Iterator[Any]:
    """
    Get all msgspec Struct classes from the models package.
    
    Returns:
        An iterator of all classes in the package.
    """
    package = importlib.import_module("msgspec_schemaorg.models")
    
    # Get all the classes defined in __all__
    for attr_name in getattr(package, "__all__", []):
        try:
            cls = getattr(package, attr_name)
            if isinstance(cls, type) and issubclass(cls, msgspec.Struct):
                yield cls
        except (AttributeError, TypeError):
            continue


def get_schema_examples() -> List[Dict[str, Any]]:
    """
    Get examples from schema.org.
    
    Returns:
        A list of schema.org examples.
    """
    try:
        response = requests.get(
            "https://schema.org/version/latest/schemaorg-all-examples.txt",
            timeout=10
        )
        response.raise_for_status()
    except (requests.RequestException, requests.Timeout):
        return []  # Return empty list if request fails
    
    content = response.text
    examples = []
    
    matches = re.findall(
        r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>',
        content,
        flags=re.DOTALL | re.M,
    )
    
    for match in matches:
        cleaned_match = match.replace("\n", "")
        try:
            example = json.loads(cleaned_match)
            if isinstance(example, dict) and not isinstance(example.get("@type"), list):
                examples.append(example)
        except json.JSONDecodeError:
            continue
    
    return examples


def clean_json_ld(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean JSON-LD data for use with msgspec.
    
    Args:
        data: The data to clean.
        
    Returns:
        The cleaned data.
    """
    if not isinstance(data, dict):
        return data
        
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


@pytest.mark.parametrize("schema_class", get_msgspec_classes())
def test_class_instantiation(schema_class):
    """
    Test that all classes can be instantiated with default values.
    
    Args:
        schema_class: The class to test.
    """
    try:
        instance = schema_class()
        # Test encoding to JSON
        json_data = msgspec.json.encode(instance)
        assert json_data is not None
    except Exception as e:
        pytest.fail(f"Class {schema_class.__name__} failed instantiation test: {str(e)}")


@pytest.fixture(scope="module")
def schema_examples():
    """
    Fixture to load schema.org examples once for all tests.
    
    Returns:
        A list of (example, type_str) tuples.
    """
    examples = get_schema_examples()
    processed_examples = []
    
    for example in examples:
        type_str = example.get("@type", "")
        if ":" in type_str:
            type_str = type_str.split(":")[-1]
        if type_str:
            processed_examples.append((example, type_str))
    
    return processed_examples


@pytest.fixture(scope="module")
def class_map():
    """
    Fixture to create a map of class names to class objects.
    
    Returns:
        A dictionary mapping class names to class objects.
    """
    result = {}
    for cls in get_msgspec_classes():
        result[cls.__name__] = cls
    return result


def pytest_generate_tests(metafunc):
    """
    Dynamic test generation for schema examples.
    """
    if 'schema_example' in metafunc.fixturenames and 'type_str' in metafunc.fixturenames:
        examples = get_schema_examples()
        processed_examples = []
        
        for example in examples:
            type_str = example.get("@type", "")
            if ":" in type_str:
                type_str = type_str.split(":")[-1]
            if type_str:
                processed_examples.append((example, type_str))
        
        metafunc.parametrize("schema_example,type_str", processed_examples)


def test_schema_examples(schema_example, type_str, class_map):
    """
    Test that schema.org examples can be parsed using our models.
    
    Args:
        schema_example: The schema.org example.
        type_str: The type of the example.
        class_map: Map of class names to class objects.
    """
    # Skip if we don't have a model for this type
    if type_str not in class_map:
        pytest.skip(f"No model for type {type_str}")
    
    try:
        # Clean the example data
        clean_data = clean_json_ld(schema_example)
        
        # Create an instance of the model
        model_class = class_map[type_str]
        model = model_class(**clean_data)
        
        # Test encoding to JSON
        json_data = msgspec.json.encode(model)
        assert json_data is not None
    except Exception as e:
        pytest.fail(f"Failed to parse example of type {type_str}: {str(e)}") 