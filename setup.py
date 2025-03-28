from setuptools import setup, find_packages

setup(
    name="msgspec-schemaorg",
    version="0.1.3",
    author="Michael Deeb",
    author_email="michael.f.deeb@gmail.com",
    description="Generate Python msgspec.Struct classes from the Schema.org vocabulary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mikewolfd/msgspec-schemaorg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.10",
    install_requires=[
        "msgspec>=0.19.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "msgspec-schemaorg-generate=msgspec_schemaorg.cli:generate_models_command",
        ],
    },
    include_package_data=True,
) 