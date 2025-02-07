import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Fixture to initialize and quit the browser session."""
    driver = webdriver.Chrome()  # Make sure you have the correct driver (chromedriver) installed
    driver.maximize_window()
    yield driver
    driver.quit()
