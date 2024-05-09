

**Overview**

This project is designed for testing both the UI and API of a web application. It contains automation modules for API testing (`automation_api_module`) and UI testing (`automation_ui_module`), along with test scenarios (`test_scenario`) for both types of testing.

**Project Structure**

- **automation_api_module**: Contains modules for API testing.
  - `api_base_scenario.py`: Utility class with common functions for API testing.
  - `pets.py`: Class for interacting with pet-related API endpoints.
- **automation_ui_module**: Contains modules for UI testing.
  - `locators.py`: Locators for identifying elements on web pages.
  - `base_element.py`: Base class for initializing page objects and handling web elements.
- **test_scenario**: Contains test scenarios for both API and UI testing.
  - `test_api.py`: Test cases for API testing.
  - `test_ui.py`: Test cases for UI testing.

**Usage**

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Navigate to the `test_scenario` directory.
4. Run the desired test files using pytest:
   ```
   pytest test_api.py
   pytest test_ui.py
   ```

5. View test results and logs for any failures or errors.

**Dependencies**

- Python 3.x
- Selenium WebDriver
- pytest
- requests
- allure-pytest

**Configuration**

- Ensure that the WebDriver (e.g., ChromeDriver) is installed and its path is properly configured.
- Modify the test data or configuration files as needed for your specific environment.

**Contributors**

- David Demeke - [@davidemeke](https://github.com/davidemeke)

Feel free to customize this README further to include any additional information specific to your project.

--- 

This version maintains the structure and content of your original README while making some minor adjustments for clarity and readability. If you have any specific additions or changes in mind, feel free to let me know!

