import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Make sure you have the correct WebDriver installed
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage_loads(driver):
    driver.get("http://www.arqiva.com")
    assert "Arqiva" in driver.title, "Homepage did not load correctly"
