# Automation Framework for UI and API Testing

## Project Structure

Project Structure
ArqivaTask/
│
├── test_ui.py        # UI test cases
├── test_api.py       # API test cases
├── conftest.py       # Shared fixtures for tests
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── report.html       # Test report generated after running tests

## Prerequisites
- Python 3.7 or above
- Google Chrome and `chromedriver` for Selenium UI tests
- `pip` for managing dependencies
   pip install -r requirements.txt


**How to Run Tests**

**UI Tests**

To run UI tests and generate an HTML report:

pytest test_ui.py --html=report.html --self-contained-html


API Tests
To run API tests:

pytest test_api.py

**Test Report**

After running the tests, the results will be available in report.html. 
Open this file in a browser to view the detailed results.

**CI/CD Integration**
Setting Up CI/CD Pipeline
To integrate this framework into a CI/CD pipeline:

Use GitHub Actions, GitLab CI/CD, or Jenkins.
Create a pipeline configuration file (.github/workflows/ci.yml for GitHub, .gitlab-ci.yml for GitLab).
Sample GitHub Actions Workflow (ci.yml):#   A r q i v a T a s k  
 