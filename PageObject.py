from Constants import *
from selector_name import *
from selenium.webdriver.common.keys import Keys


class RequestHelper(Constants):

    def enter_word_in_search(self, word):
        search_field = self.find_element(search)
        search_field.send_keys(word)
        return search_field

    def click_enter(self, search_field):
        return search_field.send_keys(Keys.ENTER)

    def get_response_after_click(self):
        return self.find_elements(result_search)[0].text

    def get_response_after_click2(self, number):
        return self.find_elements(result_search2)[number].text

