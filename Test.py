from PageObject import RequestHelper


def test_Search(browser):
    search_text = "toys"
    site = RequestHelper(browser)
    site.get_url()

    search_field = site.enter_word_in_search(search_text)
    site.click_enter(search_field)
    response = site.get_response_after_click()

    assert response == '"toys"'


def test_CheckResultOfSearching(browser):
    search_text = "toys"
    site = RequestHelper(browser)
    site.get_url()

    search_field = site.enter_word_in_search(search_text)
    site.click_enter(search_field)
    response = site.get_response_after_click2(4)

    assert response == "Pomatoy Inflatable Bounce House with Air Blower Jump House " \
                       "for Toddlers Baby with Basketball Hoop, Bouncy House for Kids Outdoor Indoor, " \
                       "Jumping and Party Gift for Toddler"



