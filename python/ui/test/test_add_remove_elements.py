from python.common.basebrowser import BrowserExample
from python.ui.method.add_remove_page import AddRemove
from python.ui.method.internet_home_page import Homepage


class TestAddRemove:

    def test_add_and_delete(self):
        browser = BrowserExample().browser

        the_homepage = Homepage(browser)
        the_add_remove = AddRemove(browser)

        the_homepage.navigate_to_page()
        the_homepage.text_is_present()
        the_homepage.add_remove_button_clickable()

        the_add_remove.text_is_present()
        the_add_remove.add_element_button_clickable()
        the_add_remove.delete_element_button_clickable()

        browser.quit()

    def test_add_and_delete_multiple(self):
        browser = BrowserExample().browser

        the_homepage = Homepage(browser)
        the_add_remove = AddRemove(browser)

        the_homepage.navigate_to_page()
        the_homepage.text_is_present()
        the_homepage.add_remove_button_clickable()

        the_add_remove.text_is_present()
        the_add_remove.add_element_button_clickable()
        the_add_remove.add_element_button_clickable()
        the_add_remove.add_element_button_clickable()
        the_add_remove.add_element_button_clickable()
        the_add_remove.delete_all_delete_btns()

        browser.quit()
