import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\Users\VnDell6u\Downloads\chromedriver_win32\chromedriver.exe')
browser.get("https://www.amazon.com/")
browser.implicitly_wait(20)

search_term = "toys"
browser.find_element_by_css_selector('[id="twotabsearchtextbox"]').send_keys(search_term)
time.sleep(2)
browser.find_element_by_css_selector('[id="twotabsearchtextbox"]').send_keys(Keys.ENTER)
time.sleep(2)

actual_text = browser.find_element_by_css_selector('[class="a-color-state a-text-bold"]').text
time.sleep(2)

assert actual_text == '"toys"'

browser.close()
