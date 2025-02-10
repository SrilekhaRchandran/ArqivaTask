import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytest_bdd import scenarios, given, when, then, parsers
import time
import allure
import os

feature_file = os.path.join(os.path.dirname(__file__), "../features/homepage.feature")
scenarios(feature_file)

@pytest.fixture
def driver():
    options = Options()
    # Uncomment below if you want to run tests in headless mode
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

TAB_XPATHS = [
    "//button[normalize-space()='About']",
    "//button[normalize-space()='Media']",
    "//button[normalize-space()='Utilities']",
    "//button[normalize-space()='Satellite Data']",
    "//button[normalize-space()='Careers']",
    "//a[normalize-space()='News & Views']",
    "//a[normalize-space()='Contact']"
]

@given("the homepage is loaded")
def load_homepage(driver):
    driver.get("http://www.arqiva.com")
    time.sleep(2)
    screenshot_path = os.path.join("screenshots", "homepage.png")
    driver.save_screenshot(screenshot_path)  # Save screenshot to file
    allure.attach(driver.get_screenshot_as_png(), name="Homepage Loaded", attachment_type=allure.attachment_type.PNG)

@then('the title should be "Arqiva"')
def check_homepage_title(driver):
    assert "Arqiva" in driver.title, "Homepage did not load correctly"

@when(parsers.parse('I navigate through the main tabs from {start_index:d} to {end_index:d}'))
def navigate_tabs(driver, start_index, end_index):
    for i in range(start_index, end_index + 1):
        tab = driver.find_element(By.XPATH, TAB_XPATHS[i])
        tab_text = tab.text
        tab.click()
        print(f"Navigating to: {tab_text}")
        time.sleep(2)  # Wait for the page to load
        print(f"Current URL: {driver.current_url}")
        assert driver.current_url != "http://www.arqiva.com", f"Failed to load tab: {tab_text}"

@then("I should verify all tabs load correctly")
def verify_all_tabs(driver):
    pass