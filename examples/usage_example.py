#!/usr/bin/env python3
"""
Example demonstrating how to use the generated Schema.org msgspec.Struct classes.
"""

import msgspec

# Import models directly from the package
try:
    from msgspec_schemaorg.models import Person, PostalAddress
except ImportError:
    # If models haven't been generated yet, print an error message
    print("Error: Models not found. Please generate them first by running scripts/generate_models.py")
    exit(1)

def main():
    # Example data (as Python dict)
    person_data = {
        "@type": "Person",
        "name": "Jane Doe",
        "jobTitle": "Software Engineer",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "123 Main St",
            "addressLocality": "Anytown",
            "postalCode": "12345",
            "addressCountry": "US"
        }
    }

    # Converting dict to msgspec Structs
    try:
        # First, convert the nested PostalAddress
        address_data = person_data.get("address", {})
        address = PostalAddress(
            streetAddress=address_data.get("streetAddress"),
            addressLocality=address_data.get("addressLocality"),
            postalCode=address_data.get("postalCode"),
            addressCountry=address_data.get("addressCountry")
        )
        
        # Then create the Person with the nested address
        person = Person(
            name=person_data.get("name"),
            jobTitle=person_data.get("jobTitle"),
            address=address
        )
        
        print(f"Created Person object: {person.name}")
        print(f"Job Title: {person.jobTitle}")
        print(f"Address: {person.address.streetAddress}, {person.address.addressLocality}")
        
        # Encode to JSON
        json_data = msgspec.json.encode(person)
        print(f"\nEncoded to JSON: {json_data.decode()}")
        
    except Exception as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    main() 