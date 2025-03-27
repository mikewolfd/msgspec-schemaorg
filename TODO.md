# TODO List for msgspec-schemaorg

## High Priority

- [ ] Fix cross-module imports between generated files to handle references properly (e.g., Person references CreativeWork)
- [ ] Add docstring escaping to prevent invalid escape sequence warnings
- [ ] Implement proper forward references for circular dependencies
- [ ] Add type checking for the generated code to ensure it's valid

## Completed

- [x] Basic project structure
- [x] Schema.org data fetching
- [x] Type mapping for Schema.org primitive types
- [x] Basic class and property extraction
- [x] Inheritance handling
- [x] Code generation for Struct classes
- [x] Multi-file organization by category
- [x] Python reserved keyword handling
- [x] Basic command-line interface
- [x] Simple example script 