# simple_CI
This README  describes the CI pipeline for API testing using FastAPI.

## Services
The project exposes two services:

- **add_service:** Running on port 5000
- **multiply_service:** Running on port 5001

## Testing
Integration tests are located in `tests/integration_tests/test_integration.py`. For simplicity, unit tests are not included in this pipeline.

## GitHub Actions Workflow
The pipeline is defined in `.github/workflows/integration.yml`

### Triggers 
The workflow is triggered by:
- Push events to the docker branch
- Pull requests to the docker branch

### Workflow Steps
1. **Environment Setup**
    - Runs on Ubuntu's container-optimized runner (`ubuntu-latest-containers`)
    - Uses `actions/checkout@v4` to clone the repository
2. **Caching**
    - Implements Docker layer caching
    - Caches Docker Compose installation
    - Stores layers for subsequent runs
    - Caches pip packages using `actions/cache@v3`
3. Python Environment
    - Sets up Python 3.9 using `actions/setup-python@v5`
    - Installs pipenv
    - Creates virtual environment using Pipfile and Pipfile.lock
4. **Service Deployment**
    - Starts services using `docker-compose -f docker-compose.yml up -d`
    - Runs pytest for integration testing
5. **Cleanup**
    - Executes docker-compose down to tear down services
    - Cleanup runs regardless of test outcome (using `if: always()`)
