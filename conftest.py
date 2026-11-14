import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()

    try:
        yield browser
    finally:
        browser.quit()