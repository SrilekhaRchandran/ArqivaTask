import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pytest_bdd import scenarios, given, when, then, parsers
import time
import allure
import os
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Load BDD scenarios from the feature file
feature_file = os.path.join(os.path.dirname(__file__), "../features/homepage.feature")
scenarios(feature_file)

# Global variables for video recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None


@pytest.fixture
def driver():
    global out
    options = Options()
    # Uncomment below if you want to run tests in headless mode
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Start video recording
    screen_size = (driver.get_window_rect()['width'], driver.get_window_rect()['height'])
    out = cv2.VideoWriter('test_video.avi', fourcc, 20.0, screen_size)

    yield driver

    # Stop video recording
    out.release()
    driver.quit()


def record_frame(driver):
    global out
    # Capture the current screen frame
    screenshot = driver.get_screenshot_as_png()  # Get screenshot as PNG
    image = Image.open(BytesIO(screenshot))  # Open it with PIL
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
    out.write(frame)  # Write to video file


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
    record_frame(driver)  # Record frame after loading homepage
    screenshot_path = os.path.join("screenshots", "homepage.png")
    driver.save_screenshot(screenshot_path)
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
        time.sleep(2)
        record_frame(driver)  # Record frame after clicking each tab
        print(f"Current URL: {driver.current_url}")
        assert driver.current_url != "http://www.arqiva.com", f"Failed to load tab: {tab_text}"

        # Capture a screenshot after clicking each tab
        screenshot_path = os.path.join("screenshots", f"{tab_text}_screenshot.png")
        driver.save_screenshot(screenshot_path)
        allure.attach(driver.get_screenshot_as_png(), name=f"{tab_text} Page Loaded",
                      attachment_type=allure.attachment_type.PNG)


@then("I should verify all tabs load correctly")
def verify_all_tabs(driver):
    pass  # This can be expanded for more specific checks if needed