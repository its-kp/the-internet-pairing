from python.common.basebrowser import BrowserExample
from python.ui.method.dropdown_page import Dropdown
from python.ui.method.internet_home_page import Homepage


class TestDropdown:

    def test_select_dropdown_object(self):
        browser = BrowserExample().browser

        the_homepage = Homepage(browser)
        the_dropdown = Dropdown(browser)

        the_homepage.navigate_to_page()
        the_homepage.text_is_present()
        the_homepage.dropdown_button_clickable()

        the_dropdown.text_is_present()
        the_dropdown.dropdown_button_clickable()
        the_dropdown.first_option_select()
        the_dropdown.second_option_select()

        browser.quit()
