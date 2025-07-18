import pytest
from selenium import webdriver

from pages.translate_page import TranslatePage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def translate_page_driver(driver):
    return TranslatePage(driver)