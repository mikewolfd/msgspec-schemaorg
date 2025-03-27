#!/usr/bin/env python3
"""
Helper script to generate models and run examples.

This script simplifies the process of working with msgspec-schemaorg
by providing a single command to:
1. Generate the Schema.org models
2. Run example scripts to demonstrate functionality

Usage:
    python run.py generate      - Generate models only
    python run.py example       - Run basic example (usage_example.py)
    python run.py advanced      - Run advanced example (advanced_example.py)
    python run.py test          - Run tests
    python run.py all           - Generate models and run examples
"""

import os
import sys
import subprocess


def run_command(cmd, capture=False):
    """Run a command and return the result."""
    if capture:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result
    else:
        print(f"Running: {cmd}")
        return subprocess.run(cmd, shell=True)


def generate_models():
    """Generate Schema.org models."""
    print("Generating Schema.org models...")
    result = run_command("python scripts/generate_models.py --clean")
    if result.returncode != 0:
        print("Error generating models")
        return False
    return True


def run_example(example_name="usage_example.py"):
    """Run an example script."""
    example_path = os.path.join("examples", example_name)
    if not os.path.exists(example_path):
        print(f"Example not found: {example_path}")
        return False
    
    print(f"Running example: {example_path}")
    result = run_command(f"python {example_path}")
    return result.returncode == 0


def run_tests():
    """Run tests."""
    print("Running tests...")
    result = run_command("python run_tests.py")
    return result.returncode == 0


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Please specify a command: generate, example, advanced, test, or all")
        return 1

    command = sys.argv[1].lower()
    
    if command == "generate":
        return 0 if generate_models() else 1
        
    elif command == "example":
        return 0 if run_example("usage_example.py") else 1
        
    elif command == "advanced":
        return 0 if run_example("advanced_example.py") else 1
        
    elif command == "test":
        return 0 if run_tests() else 1
        
    elif command == "all":
        if not generate_models():
            return 1
        if not run_example("usage_example.py"):
            return 1
        if not run_example("advanced_example.py"):
            return 1
        if not run_tests():
            return 1
        return 0
        
    else:
        print(f"Unknown command: {command}")
        print("Available commands: generate, example, advanced, test, all")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 