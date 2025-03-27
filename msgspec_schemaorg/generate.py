"""
Core logic for processing Schema.org definitions and generating msgspec.Struct classes.
"""
from __future__ import annotations

import json
import re
import os
import keyword
from pathlib import Path
from typing import Dict, List, Set, Any, Optional, Union, Tuple
from collections import defaultdict
from datetime import date, datetime, time

from .mapping import resolve_type_reference, get_type_specificity

class SchemaProcessor:
    """
    Processes Schema.org JSON-LD data and generates msgspec.Struct definitions.
    """
    
    # List of Python keywords and other reserved names that can't be used as identifiers
    PYTHON_RESERVED_KEYWORDS = set(keyword.kwlist) | {"None", "True", "False"}
    
    def __init__(self, schema_data: Dict[str, Any]):
        """
        Initialize with schema data.
        
        Args:
            schema_data: The loaded JSON-LD Schema.org data
        """
        self.schema_data = schema_data
        self.graph = schema_data.get('@graph', [])
        
        # Index entities by ID for quick lookup
        self.entity_map: Dict[str, Dict[str, Any]] = {}
        for entity in self.graph:
            entity_id = entity.get('@id', '')
            if entity_id:
                self.entity_map[entity_id] = entity
        
        # Map to store properties for each class (including inherited ones)
        self.class_properties: Dict[str, Dict[str, Dict[str, Any]]] = defaultdict(dict)
        
        # Processed classes to avoid duplicate processing
        self.processed_classes: Set[str] = set()
        
        # Store all class hierarchies for reference
        self.class_hierarchies: Dict[str, List[str]] = {}
        
        # Track class categories/namespaces for file organization
        self.class_categories: Dict[str, str] = {}
        
        # Track class dependencies for imports
        self.class_dependencies: Dict[str, Set[str]] = defaultdict(set)
        
        # Store normalized class names
        self.normalized_class_names: Dict[str, str] = {}
        
        # First, collect all classes and properties
        self.classes = self._collect_classes()
        self.properties = self._collect_properties()
        
        # Then process class properties (including inheritance)
        self._process_all_class_properties()
        
        # Determine class categories
        self._determine_class_categories()
        
        # Normalize all class names for consistency
        self._normalize_all_class_names()
        
        # Analyze dependencies between classes
        self._analyze_dependencies()
        
        # Detect circular dependencies
        self.circular_dependencies = self._detect_circular_dependencies()
    
    def _collect_classes(self) -> Dict[str, Dict[str, Any]]:
        """
        Identify all entities that are rdfs:Class.
        
        Returns:
            Dictionary mapping class IDs to class entities
        """
        classes = {}
        for entity in self.graph:
            if entity.get('@type') == 'rdfs:Class':
                class_id = entity.get('@id', '')
                if class_id:
                    classes[class_id] = entity
        return classes
    
    def _collect_properties(self) -> Dict[str, Dict[str, Any]]:
        """
        Identify all entities that are rdf:Property.
        
        Returns:
            Dictionary mapping property IDs to property entities
        """
        properties = {}
        for entity in self.graph:
            if entity.get('@type') == 'rdf:Property':
                prop_id = entity.get('@id', '')
                if prop_id:
                    properties[prop_id] = entity
        return properties
    
    def _get_parent_classes(self, class_id: str) -> List[str]:
        """
        Find all parent classes using rdfs:subClassOf, recursively.
        
        Args:
            class_id: ID of the class to find parents for
            
        Returns:
            List of parent class IDs
        """
        if class_id in self.class_hierarchies:
            return self.class_hierarchies[class_id]
            
        parents = []
        class_entity = self.entity_map.get(class_id, {})
        
        # Get immediate parent(s)
        sub_class_of = class_entity.get('rdfs:subClassOf', [])
        if not isinstance(sub_class_of, list):
            sub_class_of = [sub_class_of]
            
        for parent in sub_class_of:
            if isinstance(parent, dict) and '@id' in parent:
                parent_id = parent['@id']
                parents.append(parent_id)
                # Recursively get grandparents
                parents.extend(self._get_parent_classes(parent_id))
            elif isinstance(parent, str):
                parents.append(parent)
                # Recursively get grandparents
                parents.extend(self._get_parent_classes(parent))
                
        # Remove duplicates while preserving order
        unique_parents = []
        for p in parents:
            if p not in unique_parents:
                unique_parents.append(p)
                
        # Cache for future use
        self.class_hierarchies[class_id] = unique_parents
        return unique_parents
    
    def _process_property_types(self, property_entity: Dict[str, Any]) -> List[Union[type, str]]:
        """
        Process the range types for a property.
        
        Args:
            property_entity: The property entity to process
            
        Returns:
            List of Python types or class name strings for the property,
            sorted by specificity (most specific first)
        """
        range_includes = property_entity.get('schema:rangeIncludes', [])
        if not isinstance(range_includes, list):
            range_includes = [range_includes]
            
        types = []
        type_specs = []  # List of (type, specificity) tuples
        
        for range_type in range_includes:
            if isinstance(range_type, dict) and '@id' in range_type:
                type_ref = range_type['@id']
                resolved_type = resolve_type_reference(type_ref)
                
                # Get the type name for specificity lookup
                type_name = type_ref
                if isinstance(type_ref, str):
                    type_name = type_ref.replace("schema:", "").replace("http://schema.org/", "")
                
                specificity = get_type_specificity(type_name)
                type_specs.append((resolved_type, specificity))
                
            elif isinstance(range_type, str):
                # Handle direct string references
                resolved_type = resolve_type_reference(range_type)
                
                # Get specificity
                type_name = range_type.replace("schema:", "").replace("http://schema.org/", "")
                specificity = get_type_specificity(type_name)
                type_specs.append((resolved_type, specificity))
        
        # Sort by specificity (highest first)
        type_specs.sort(key=lambda x: x[1], reverse=True)
        
        # Extract just the types
        types = [t[0] for t in type_specs]
                
        return types or [str]  # Default to str if no type specified
    
    def _normalize_property_name(self, prop_name: str) -> str:
        """
        Normalize a property name to be a valid Python identifier.
        
        Args:
            prop_name: Property name from Schema.org
            
        Returns:
            Valid Python identifier
        """
        # If property name is a Python keyword, append an underscore
        if prop_name in self.PYTHON_RESERVED_KEYWORDS:
            return f"{prop_name}_"
        
        # Replace any invalid characters with underscores
        prop_name = re.sub(r'[^a-zA-Z0-9_]', '_', prop_name)
        
        # Ensure it doesn't start with a number
        if prop_name and prop_name[0].isdigit():
            prop_name = f"p_{prop_name}"
            
        return prop_name
    
    def _process_class_properties(self, class_id: str):
        """
        Process properties for a class, including inherited ones.
        
        Args:
            class_id: ID of the class to process properties for
        """
        if class_id in self.processed_classes:
            return
            
        self.processed_classes.add(class_id)
        
        # Process parent classes first
        parent_classes = self._get_parent_classes(class_id)
        for parent_id in parent_classes:
            self._process_class_properties(parent_id)
            
        # Inherit properties from parents
        for parent_id in parent_classes:
            if parent_id in self.class_properties:
                for prop_name, prop_info in self.class_properties[parent_id].items():
                    # Only add if not already defined for this class
                    if prop_name not in self.class_properties[class_id]:
                        self.class_properties[class_id][prop_name] = prop_info
        
        # Find properties for this class
        for prop_id, prop_entity in self.properties.items():
            domain_includes = prop_entity.get('schema:domainIncludes', [])
            if not isinstance(domain_includes, list):
                domain_includes = [domain_includes]
                
            for domain in domain_includes:
                if isinstance(domain, dict) and domain.get('@id') == class_id:
                    # Extract the property name from the ID
                    prop_name = prop_id.split('/')[-1]
                    if ':' in prop_name:
                        prop_name = prop_name.split(':')[-1]
                        
                    # Python-friendly property name
                    py_prop_name = self._normalize_property_name(prop_name)
                    
                    # Store property info
                    self.class_properties[class_id][py_prop_name] = {
                        'id': prop_id,
                        'name': prop_name,
                        'types': self._process_property_types(prop_entity),
                        'description': prop_entity.get('rdfs:comment', ''),
                    }
    
    def _determine_class_categories(self):
        """
        Determine category/namespace for each class based on its hierarchy and type.
        This will be used to organize classes into separate files.
        """
        # Common top-level categories in Schema.org
        top_categories = [
            'schema:CreativeWork', 
            'schema:Event',
            'schema:Organization',
            'schema:Person',
            'schema:Place',
            'schema:Product',
            'schema:Intangible',
            'schema:Action',
            'schema:Thing'
        ]
        
        # Find the category for each class
        for class_id in self.classes:
            # Default category is 'misc'
            self.class_categories[class_id] = 'misc'
            
            # Check if this is a top-level category
            for top_cat in top_categories:
                if class_id == top_cat:
                    short_name = top_cat.split(':')[-1].lower()
                    self.class_categories[class_id] = short_name
                    break
            
            # If not a top category, check if it's a subclass of one
            if self.class_categories[class_id] == 'misc':
                for top_cat in top_categories:
                    if top_cat in self._get_parent_classes(class_id):
                        short_name = top_cat.split(':')[-1].lower()
                        self.class_categories[class_id] = short_name
                        break
    
    def _process_all_class_properties(self):
        """
        Process properties for all classes.
        """
        for class_id in self.classes:
            self._process_class_properties(class_id)
    
    def _get_type_annotation_str(self, type_obj: Union[type, str]) -> str:
        """
        Convert a type to its string representation for annotations.
        
        Args:
            type_obj: A Python type or class name string
            
        Returns:
            String representation of the type for use in annotations
        """
        if isinstance(type_obj, type):
            return type_obj.__name__
        else:
            # It's already a string (likely a class name for forward reference)
            return str(type_obj)
    
    def _normalize_class_name(self, class_name: str) -> str:
        """
        Normalize a class name to be a valid Python identifier.
        
        Args:
            class_name: Original class name from Schema.org
            
        Returns:
            Normalized class name that is a valid Python identifier
        """
        # If class name starts with a number, prefix with 'Model'
        if class_name and class_name[0].isdigit():
            class_name = f"Model{class_name}"
            
        # Replace any invalid characters with underscores
        class_name = re.sub(r'[^a-zA-Z0-9_]', '_', class_name)
        
        # If class name is a Python keyword, append 'Type'
        if class_name in self.PYTHON_RESERVED_KEYWORDS:
            class_name = f"{class_name}Type"
            
        return class_name
    
    def _normalize_all_class_names(self):
        """
        Pre-normalize all class names for consistent references.
        """
        for class_id in self.classes:
            class_name = class_id.split('/')[-1]
            if ':' in class_name:
                class_name = class_name.split(':')[-1]
            
            normalized_name = self._normalize_class_name(class_name)
            self.normalized_class_names[class_id] = normalized_name
    
    def _analyze_dependencies(self):
        """
        Analyze dependencies between classes based on property types.
        """
        for class_id, props in self.class_properties.items():
            for prop_name, prop_info in props.items():
                types = prop_info['types']
                for typ in types:
                    # If type is a string but not a primitive type, it's a class reference
                    if isinstance(typ, str) and typ not in {'str', 'int', 'float', 'bool', 'date', 'datetime', 'time'}:
                        # Try to find the full class ID in our normalized names
                        for other_class_id, norm_name in self.normalized_class_names.items():
                            if norm_name == typ:
                                self.class_dependencies[class_id].add(other_class_id)
                                break
    
    def _detect_circular_dependencies(self) -> Dict[str, Set[str]]:
        """
        Detect circular dependencies between classes.
        
        Returns:
            Dictionary mapping class IDs to sets of class IDs that form a circular dependency
        """
        circular_deps = defaultdict(set)
        
        # For each class and its dependencies
        for class_id, deps in self.class_dependencies.items():
            # For each dependency
            for dep_id in deps:
                # If the dependency also depends on the class, it's a circular dependency
                if class_id in self.class_dependencies.get(dep_id, set()):
                    circular_deps[class_id].add(dep_id)
                    
        return circular_deps
    
    def _get_module_path(self, class_id: str) -> str:
        """
        Get the module path for importing a class.
        
        Args:
            class_id: ID of the class
            
        Returns:
            Module path for importing the class
        """
        category = self.class_categories.get(class_id, 'misc')
        class_name = self.normalized_class_names.get(class_id, 'Unknown')
        return f"msgspec_schemaorg.models.{category}.{class_name}"
    
    def _escape_docstring(self, docstring: str) -> str:
        """
        Escape problematic characters in docstrings to prevent SyntaxErrors.
        
        Args:
            docstring: Original docstring
            
        Returns:
            Cleaned docstring
        """
        if not docstring:
            return ""
            
        # Check if docstring is not a string
        if not isinstance(docstring, str):
            print(f"Warning: Docstring is not a string but {type(docstring)}: {docstring}")
            # Try to convert to string
            try:
                docstring = str(docstring)
            except Exception as e:
                print(f"Error converting docstring to string: {e}")
                return ""
        
        # Replace backslashes with double backslashes to prevent escape sequence errors
        docstring = docstring.replace('\\', '\\\\')
        return docstring
    
    def generate_struct_code(self, schema_class_id: str) -> tuple[list[str], str]:
        """Generate a msgspec.Struct definition for a Schema.org class.

        Args:
            schema_class_id: The Schema.org class ID.

        Returns:
            A tuple of (import_statements, class_code).
        """
        class_entity = self.entity_map.get(schema_class_id, {})
        if not class_entity:
            return "", []
            
        # Get the normalized class name
        class_name = self.normalized_class_names.get(schema_class_id, "Unknown")
            
        # Get class description and escape it
        class_description = self._escape_docstring(class_entity.get('rdfs:comment', ''))
        
        # Get properties for this class
        properties = self.class_properties.get(schema_class_id, {})
        
        # Get circular dependencies for this class
        circular_deps = self.circular_dependencies.get(schema_class_id, set())
        
        # Collect imports needed
        imports = set()
        typed_imports = set()
        
        # Add imports for primitive types
        has_date = False
        has_datetime = False
        has_time = False
        has_url = False  # Track URL type usage
        
        # Flag to track if this class uses date types
        needs_date_handling = False
        
        # Generate code
        code = [f"class {class_name}(Struct, frozen=True):"]
        
        # Add docstring
        if class_description:
            code.append(f'    """{class_description}"""')
        
        # Add fields and collect dependencies
        for prop_name, prop_info in properties.items():
            types = prop_info['types']
            
            # Track dependencies
            prop_type_imports = []
            
            # Check if this property has date/datetime type or URL type
            has_date_type = False
            has_url_type = False
            
            for typ in types:
                if isinstance(typ, type):
                    if typ.__name__ == 'date':
                        has_date = True
                        has_date_type = True
                    elif typ.__name__ == 'datetime':
                        has_datetime = True
                        has_date_type = True
                    elif typ.__name__ == 'time':
                        has_time = True
                elif isinstance(typ, str) and typ == 'URL':
                    has_url = True
                    has_url_type = True
                else:
                    # If it's a string (class name), find the class ID and add it to imports
                    for other_class_id, norm_name in self.normalized_class_names.items():
                        if norm_name == typ:
                            # For all Schema.org types, use string annotations and put imports under TYPE_CHECKING
                            other_category = self.class_categories.get(other_class_id, 'misc')
                            typed_imports.add(f"from msgspec_schemaorg.models.{other_category}.{norm_name} import {norm_name}")
                            break
            
            # Create type annotation string
            if len(types) > 1:
                # Use Union for multiple types
                type_str = " | ".join(self._get_string_type_annotation(t) for t in types)
            elif len(types) == 1:
                type_str = self._get_string_type_annotation(types[0])
            else:
                type_str = "str"  # Default
                
            # Make all fields optional for now
            code.append(f"    {prop_name}: {type_str} | None = None")
            
            # Mark if we need date handling
            if has_date_type:
                needs_date_handling = True
        
        # Add empty class if no properties
        if len(code) == 1:
            code.append("    pass")
        
        # Build imports list
        import_statements = ["from __future__ import annotations", "from msgspec import Struct, field"]
        
        # Add utilities for ISO8601 parsing if needed
        if needs_date_handling:
            import_statements.append("from msgspec_schemaorg.utils import parse_iso8601")
            
        # Add URL imports if needed
        if has_url:
            import_statements.append("from msgspec_schemaorg.utils import URL")
            import_statements.append("from typing import Annotated")
            import_statements.append("from msgspec import Meta")
            
        # Add TYPE_CHECKING for all Schema.org types
        if typed_imports:
            import_statements.append("from typing import TYPE_CHECKING")
            import_statements.append("\nif TYPE_CHECKING:")
            for typed_import in sorted(typed_imports):
                import_statements.append(f"    {typed_import}")
        
        # Add datetime imports if needed
        if has_date or has_datetime or has_time:
            date_imports = []
            if has_date:
                date_imports.append("date")
            if has_datetime:
                date_imports.append("datetime")
            if has_time:
                date_imports.append("time")
            import_statements.append(f"from datetime import {', '.join(date_imports)}")
        
        # Combine imports and code
        return "\n".join(code), import_statements
    
    def _get_string_type_annotation(self, type_obj: Union[type, str]) -> str:
        """
        Convert a type to its string representation for annotations, using quoted strings for Schema.org types.
        
        Args:
            type_obj: A Python type or class name string
            
        Returns:
            String representation of the type for use in annotations
        """
        if isinstance(type_obj, type):
            return type_obj.__name__
        else:
            # Check if it's a Schema.org type (one of our model classes)
            for norm_name in self.normalized_class_names.values():
                if norm_name == type_obj:
                    return f"'{type_obj}'"  # Use string literal for all Schema.org types
            # It's a primitive type or unknown
            return str(type_obj)
    
    def generate_all_structs(self, output_dir: Path) -> Dict[str, str]:
        """
        Generate msgspec.Struct definitions for all Schema.org classes,
        with each class in its own file organized by category.
        
        Args:
            output_dir: Root directory to save the generated files
            
        Returns:
            Dictionary mapping file paths to generated code
        """
        # Create output directory if it doesn't exist
        output_dir = Path(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        
        # Map to store generated files
        files = {}
        
        # Create one file per class, organized by category
        for class_id in sorted(self.classes.keys()):
            category = self.class_categories.get(class_id, 'misc')
            class_name = self.normalized_class_names.get(class_id, 'Unknown')
            
            # Create category directory if it doesn't exist
            category_dir = output_dir / category
            os.makedirs(category_dir, exist_ok=True)
            
            # Skip if we couldn't get a valid class name
            if class_name == 'Unknown':
                continue
                
            # Generate code for this class
            class_code, imports = self.generate_struct_code(class_id)
            
            # Skip if we couldn't generate code
            if not class_code:
                continue
                
            # Create file path
            file_path = category_dir / f"{class_name}.py"
            
            # Combine imports and code
            full_code = "\n".join(imports) + "\n\n\n" + class_code
            
            # Add to files map
            files[file_path] = full_code
            
            # Create/update category __init__.py
            init_path = category_dir / "__init__.py"
            if init_path not in files:
                files[init_path] = f'"""Generated Schema.org {category} models using msgspec."""\n\n'
            
            # Add import to category __init__.py
            init_content = files[init_path]
            import_line = f"from .{class_name} import {class_name}\n"
            if import_line not in init_content:
                files[init_path] += import_line
        
        # Create category __all__ statements
        for category in set(self.class_categories.values()):
            category_dir = output_dir / category
            init_path = category_dir / "__init__.py"
            if init_path in files:
                # Get all classes in this category
                class_names = []
                for class_id, cat in self.class_categories.items():
                    if cat == category:
                        class_name = self.normalized_class_names.get(class_id)
                        if class_name:
                            class_names.append(class_name)
                
                # Add __all__ statement
                if class_names:
                    init_content = files[init_path]
                    init_content += "\n__all__ = [\n"
                    for name in sorted(class_names):
                        init_content += f"    '{name}',\n"
                    init_content += "]\n"
                    files[init_path] = init_content
        
        # Create main models/__init__.py
        main_init_path = output_dir / "__init__.py"
        main_init_content = '"""Generated Schema.org models using msgspec."""\n\n'
        
        # Get all categories (directories)
        categories = set(self.class_categories.values())
        
        # Add imports for each category
        for category in sorted(categories):
            main_init_content += f"from . import {category}\n"
        
        # Add all class imports to the top level
        main_init_content += "\n# Import all classes directly\n"
        for category in sorted(categories):
            main_init_content += f"from .{category} import *\n"
        
        # Add __all__ list
        main_init_content += "\n__all__ = [\n"
        for category in sorted(categories):
            main_init_content += f"    '{category}',\n"
            
        # Add all class names to __all__
        for class_id, class_name in sorted(self.normalized_class_names.items()):
            if class_name != 'Unknown':
                main_init_content += f"    '{class_name}',\n"
                
        main_init_content += "]\n"
        
        files[main_init_path] = main_init_content
        
        return files


def fetch_and_generate(schema_data: Dict[str, Any], output_dir: Path) -> Dict[str, str]:
    """
    Process Schema.org data and generate Python code.
    
    Args:
        schema_data: The loaded JSON-LD Schema.org data
        output_dir: Directory to save the generated files
        
    Returns:
        Dictionary mapping file paths to generated code
    """
    processor = SchemaProcessor(schema_data)
    return processor.generate_all_structs(output_dir)
