# Contributing to msgspec-schemaorg

Thank you for your interest in contributing to msgspec-schemaorg! This document provides guidelines and instructions for contributing to this project.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/username/msgspec-schemaorg.git
   cd msgspec-schemaorg
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

4. Generate the models:
   ```bash
   python scripts/generate_models.py
   ```

5. Run tests:
   ```bash
   python run_tests.py
   ```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Commit your changes with semantic commit messages (`feat: add amazing feature`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration and Deployment.

### Automated Tests

Every pull request and push to the main branch triggers a test workflow that:
- Runs on multiple Python versions (3.10, 3.11, 3.12)
- Generates the Schema.org models
- Runs the test suite

### Publishing to PyPI

The package is automatically published to PyPI when a new release is created:

1. **Tag Release Process**:
   - When you push a tag starting with `v` (e.g., `v0.1.0`), the package will be built and published to TestPyPI
   - Example:
     ```bash
     git tag v0.1.0
     git push origin v0.1.0
     ```

2. **GitHub Release Process**:
   - When you create an official release through the GitHub interface, the package will be published to the main PyPI repository
   - Go to the repository's "Releases" tab
   - Click "Draft a new release"
   - Choose the tag version
   - Fill in the release details
   - Click "Publish release"

### Required Secrets

For the CI/CD pipeline to work properly, the following secrets need to be configured in the GitHub repository:

- `PYPI_API_TOKEN`: API token for publishing to PyPI
- `TEST_PYPI_API_TOKEN`: API token for publishing to TestPyPI

Repository admins can add these secrets in the repository settings.

## Code Style

- Follow PEP 8 guidelines
- Use semantic commit messages
- Add docstrings to functions and classes
- Write unit tests for new functionality

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License. 