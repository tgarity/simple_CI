# simple_CI

This branch implements a simple Continuous Integration (CI) pipeline. It assumes that **all code to be tested resides within the same container**, focusing on testing interactions between functions—addition and multiplication, in this case.

The workflow for this branch is as follows:
1. **Create the initial feature:**

    * On a new branch, implement the first feature (e.g., addition) inside the `src` folder.
    * Write corresponding unit tests for the feature in the `tests` folder.
    * Create a `pytest.ini` file to define configurations, including the `PYTHONPATH` environment variable and the location of the tests.

2. **Add the next feature:**
    * Create a second branch and implement the new feature (e.g., multiplication) inside the `src` folder.
    * Write unit tests for the new feature in the `tests` folder.
3. **Write integration tests:**
    * Develop integration tests to ensure the features (e.g., addition and multiplication) work together as expected.
4. **Automate testing with GitHub Actions:**
    *Place the action definition file, named `CI_push.yml`, inside the `.github/workflows` folder.
    *This action runs on a minimal version of the latest Ubuntu.


## Action Workflow Steps
The CI action is triggered on any push to the `main` branch and executes the following steps:

- **Checkout the code:**
    
    Use the action `actions/checkout@v3` to clone the repository into the container.
- **Set up Python:** 
    
    Use the action `actions/setup-python@v4` to define the Python version (e.g., 3.12).
- **Set the environment variable:** 
    
    Define the `PYTHONPATH` environment variable to include the repository directory, allowing Python to import the code. Use the `GITHUB_ENV` file to persist this setting across workflow steps.
- **Install dependencies:** 
    
    Install the required packages, including `pip`, `pytest`, and `pytest-cov`. You can also install other dependencies listed in the `Pipfile`.
- **Run tests and generate a coverage report:**
    
    Execute the test suite and generate a coverage report in HTML format using `pytest-cov`.
- **Upload the coverage report as an artifact:**
    
    Use the action `actions/upload-artifact@v3` to upload the coverage report as an artifact. This artifact will persist after the action completes, allowing you to access the HTML report.