from page_object import RequestHelper
from selector_name import *


def test_search(browser):
    search_text = "toys"
    site = RequestHelper(browser)
    site.get_url()

    search_field = site.enter_word_in_search(search_text)
    site.click_enter(search_field)
    response = site.get_response_after_click(SEARCH_RESULTS, 0)

    assert response == '"toys"'


def test_check_result_of_searching(browser):
    search_text = "toys"
    result_text = "Toys & Games"
    site = RequestHelper(browser)
    site.get_url()

    search_field = site.enter_word_in_search(search_text)
    site.click_enter(search_field)
    response = site.get_response_after_click(GOODS_IN_SEARCH_RESULTS, 3)

    assert response == result_text


def test_click_on_delivery_button(browser):
    delivery_text = "Choose your location"
    site = RequestHelper(browser)
    site.get_url()

    site.click_delivery_button()

    response = site.get_response_after_click_button()

    assert response == delivery_text


def test_click_on_categories_button(browser):
    search_text = "djodjo moyes"
    result_text = "jojo moyes"
    site = RequestHelper(browser)
    site.get_url()

    site.click_on_button(CATEGORIES_BUTTON)

    site.click_on_button(BOOK_CATEGORY)

    search_field = site.enter_word_in_search(search_text)
    site.click_enter(search_field)

    response = site.get_response_after_search()

    assert response == result_text







