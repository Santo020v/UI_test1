from constants import *
from selector_name import *
from selenium.webdriver.common.keys import Keys


class RequestHelper(Constants):

    def enter_word_in_search(self, word):
        search_field = self.find_element(SEARCH)
        search_field.send_keys(word)
        return search_field

    @staticmethod
    def click_enter(search_field):
        return search_field.send_keys(Keys.ENTER)

    def get_response_after_click(self, result_search, index):
        return self.find_elements(result_search)[index].text

    def click_delivery_button(self):
        return self.find_element(CLICK_DELIVERY_BUTTON).click()

    def get_response_after_click_button(self):
        return self.find_element(DELIVERY_TEXT).text

    def click_on_button(self, button):
        return self.find_element(button).click()

    def get_response_after_search(self):
        return self.find_element(SEARCH_BOOK).text
