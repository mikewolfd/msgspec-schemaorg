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
import argparse
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent


def run_command(cmd, cwd=None):
    """Run a command and stream output."""
    print(f"Running: {' '.join(cmd)}")
    process = subprocess.Popen(
        cmd,
        cwd=cwd or PROJECT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,  # Line buffered
    )

    # Stream output
    for line in process.stdout:
        print(line, end="")

    # Wait for process to complete
    process.wait()

    if process.returncode != 0:
        print(f"Command failed with return code {process.returncode}")
        sys.exit(process.returncode)


def generate_models():
    """Generate Schema.org models."""
    run_command(["python", "scripts/generate_models.py", "--clean"])


def generate_enums():
    """Generate Schema.org enum classes."""
    run_command(["python", "scripts/generate_enums.py"])


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
    """Run unit tests."""
    run_command(["pytest", "tests/"])


def run_all():
    """Run all tasks: generate models, generate enums, and run tests."""
    generate_models()
    generate_enums()
    generate_models()
    run_tests()


def main():
    """Main function to parse arguments and execute commands."""
    parser = argparse.ArgumentParser(
        description="Run common tasks for msgspec-schemaorg."
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Generate models command
    subparsers.add_parser("generate_models", help="Generate Schema.org models")

    # Generate enums command
    subparsers.add_parser("generate_enums", help="Generate Schema.org enum classes")

    # Test command
    subparsers.add_parser("test", help="Run unit tests")

    # All command
    subparsers.add_parser("all", help="Generate models, generate enums, and run tests")

    args = parser.parse_args()

    if args.command == "generate_models":
        generate_models()
    elif args.command == "generate_enums":
        generate_enums()
    elif args.command == "test":
        run_tests()
    elif args.command == "all":
        run_all()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
