from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome(r'C:\Users\VnDell6u\Downloads\chromedriver_win32\chromedriver.exe')
    yield browser
    browser.close()