#!/usr/bin/env python3
"""
Test runner for msgspec-schemaorg.

This script runs various tests for the msgspec-schemaorg package:
- Unit tests (with unittest)
- Example scripts
- Import validation

Usage:
    python run_tests.py             # Run all tests
    python run_tests.py examples    # Only run examples
    python run_tests.py unittest    # Only run unit tests
    python run_tests.py imports     # Only test imports
"""

import os
import sys
import unittest
import subprocess
from pathlib import Path


def run_unittest_tests():
    """Run the unittest test suite."""
    print("\n=== Running unittest tests ===")
    
    # Discover and run tests using unittest
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    if result.errors or result.failures:
        print("❌ Unittest tests failed")
        return False
    
    print("✅ All unittest tests passed!")
    return True


def run_example_scripts():
    """Run example scripts to ensure they work correctly."""
    print("\n=== Running example scripts ===")
    
    examples_dir = Path('examples')
    examples = list(examples_dir.glob('*.py'))
    
    if not examples:
        print("No example scripts found in the 'examples' directory")
        return True  # Not a failure, just no examples
    
    all_passed = True
    
    for example in examples:
        print(f"Running example: {example}")
        result = subprocess.run([sys.executable, str(example)], 
                               capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Example {example} failed with exit code {result.returncode}")
            print("--- Error output ---")
            print(result.stderr)
            all_passed = False
        else:
            print(f"✅ Example {example} ran successfully")
    
    if all_passed:
        print("✅ All examples ran successfully!")
    else:
        print("❌ Some examples failed")
    
    return all_passed


def test_imports():
    """Test that all expected models can be imported."""
    print("\n=== Testing model imports ===")
    
    # Script that tests importing a variety of models
    import_test_code = """
try:
    import msgspec
    from msgspec_schemaorg.models import (
        Person, 
        Organization, 
        CreativeWork, 
        BlogPosting, 
        PostalAddress, 
        ImageObject, 
        Place,
        Event,
        Product,
        Action
    )
    print("✅ Successfully imported all test models")
    exit(0)
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)
"""
    
    # Write the test code to a temporary file
    with open('_temp_import_test.py', 'w') as f:
        f.write(import_test_code)
    
    # Run the test
    try:
        result = subprocess.run([sys.executable, '_temp_import_test.py'], 
                               capture_output=True, text=True)
        
        print(result.stdout)
        
        if result.returncode != 0:
            print(f"❌ Import test failed: {result.stderr}")
            return False
        
        return True
    finally:
        # Clean up the temporary file
        if os.path.exists('_temp_import_test.py'):
            os.unlink('_temp_import_test.py')


def main():
    """Main function that runs requested tests."""
    test_types = sys.argv[1:] if len(sys.argv) > 1 else ['all']
    
    if 'all' in test_types or 'unittest' in test_types:
        unittest_success = run_unittest_tests()
    else:
        unittest_success = True  # Skip this test
    
    if 'all' in test_types or 'examples' in test_types:
        examples_success = run_example_scripts()
    else:
        examples_success = True  # Skip this test
    
    if 'all' in test_types or 'imports' in test_types:
        imports_success = test_imports()
    else:
        imports_success = True  # Skip this test
    
    # Print summary
    print("\n=== Test Summary ===")
    if 'all' in test_types or 'unittest' in test_types:
        print(f"Unit Tests: {'✅ PASSED' if unittest_success else '❌ FAILED'}")
    if 'all' in test_types or 'examples' in test_types:
        print(f"Examples: {'✅ PASSED' if examples_success else '❌ FAILED'}")
    if 'all' in test_types or 'imports' in test_types:
        print(f"Imports: {'✅ PASSED' if imports_success else '❌ FAILED'}")
    
    # Set exit code
    if unittest_success and examples_success and imports_success:
        print("\n✅ All tests passed successfully!")
        return 0
    else:
        print("\n❌ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 