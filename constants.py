from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Constants:
    def __init__(self, browser):
        self.url = "https://www.amazon.com/"
        self.browser = browser

    def get_url(self):
        return self.browser.get(self.url)

    def find_element(self, name, time=30):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(name),
                                                       message=f"Can't find {name} element")

    def find_elements(self, name, time=30):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(name),
                                                       message=f"Can't find {name} element")



