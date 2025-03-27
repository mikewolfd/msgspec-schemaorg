#!/usr/bin/env python3
"""
Advanced example demonstrating how to use complex Schema.org types and nested structures.
"""

import msgspec
from datetime import date

try:
    from msgspec_schemaorg.models import (
        Person, 
        Organization, 
        PostalAddress, 
        BlogPosting, 
        ImageObject, 
        Review, 
        Rating
    )
    from msgspec_schemaorg.utils import parse_iso8601
except ImportError:
    print("Error: Models not found. Please generate them first by running scripts/generate_models.py")
    exit(1)

def main():
    # Create a complex structure with nested objects
    
    # 1. Create an author (Person)
    author_address = PostalAddress(
        streetAddress="456 Author Ave",
        addressLocality="Writerville",
        postalCode="54321",
        addressCountry="US"
    )
    
    author = Person(
        name="Jane Author",
        jobTitle="Technical Writer",
        address=author_address,
        email="jane@example.com",
        url="https://janeauthor.example.com"
    )
    
    # 2. Create a publisher (Organization)
    publisher_address = PostalAddress(
        streetAddress="789 Publisher Blvd",
        addressLocality="Mediacity",
        postalCode="98765",
        addressCountry="US"
    )
    
    publisher = Organization(
        name="TechMedia Inc.",
        url="https://techmedia.example.com",
        address=publisher_address,
        email="contact@techmedia.example.com"
    )
    
    # 3. Create an image
    image = ImageObject(
        name="Blog Header Image",
        url="https://example.com/images/header.jpg",
        width="1200px",
        height="600px",
        encodingFormat="image/jpeg"
    )
    
    # 4. Create a review with rating
    rating = Rating(
        ratingValue=4.5,
        bestRating=5,
        worstRating=1
    )
    
    review = Review(
        name="Great Article",
        reviewBody="This article is very informative and well-written.",
        reviewRating=rating,
        author=Person(name="John Reviewer")
    )
    
    # 5. Create the blog posting that contains all the above elements
    # Use ISO8601 strings for dates
    date_published_str = "2023-09-15"
    date_modified_str = "2023-09-20T14:30:00Z"
    
    # Parse ISO8601 strings to Python date/datetime objects
    date_published = parse_iso8601(date_published_str)
    date_modified = parse_iso8601(date_modified_str)
    
    blog_post = BlogPosting(
        name="Understanding Schema.org with Python",
        headline="How to Use Schema.org Types in Python Applications",
        author=author,
        publisher=publisher,
        # Pass the parsed date objects
        datePublished=date_published,
        dateModified=date_modified,
        image=image,
        review=review,
        description="Learn how to work with Schema.org types in Python using msgspec-schemaorg",
        articleBody="This is the full text of the blog post...",
        keywords="schema.org, python, msgspec, structured data"
    )
    
    # Encode to JSON
    json_data = msgspec.json.encode(blog_post)
    
    # Print out information about the blog post
    print(f"Blog Post: {blog_post.headline}")
    print(f"By: {blog_post.author.name} ({blog_post.author.jobTitle})")
    print(f"Published by: {blog_post.publisher.name}")
    
    # Date handling demonstration
    print(f"Date Published: {blog_post.datePublished}")
    print(f"Date Published Type: {type(blog_post.datePublished).__name__}")
    if isinstance(blog_post.datePublished, date):
        print(f"Date Published Year: {blog_post.datePublished.year}")
    
    print(f"Date Modified: {blog_post.dateModified}")
    print(f"Date Modified Type: {type(blog_post.dateModified).__name__}")
    if hasattr(blog_post.dateModified, 'hour'):
        print(f"Date Modified Time: {blog_post.dateModified.hour}:{blog_post.dateModified.minute}")
    
    print(f"Review Rating: {blog_post.review.reviewRating.ratingValue}/{blog_post.review.reviewRating.bestRating}")
    print(f"Review Comment: {blog_post.review.reviewBody}")
    
    # Print JSON sample
    print("\nJSON Preview (first 300 chars):")
    print(json_data.decode()[:300] + "...")
    
    print("\nWorking with Schema.org JSON from an external source:")
    print("1. Parse dates yourself before creating objects")
    print("2. Or use the parse_iso8601 utility function when needed:")
    print(f"   parse_iso8601('2023-12-31') → {parse_iso8601('2023-12-31')} (type: {type(parse_iso8601('2023-12-31')).__name__})")
    print(f"   parse_iso8601('2023-12-31T23:59:59Z') → {parse_iso8601('2023-12-31T23:59:59Z')} (type: {type(parse_iso8601('2023-12-31T23:59:59Z')).__name__})")

if __name__ == "__main__":
    main() 