from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(3)
    try:
        yield browser
    finally:
        browser.quit()

    return browser



