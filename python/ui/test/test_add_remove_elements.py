from python.ui.method.add_remove_page import AddRemove
from python.ui.method.internet_home_page import Homepage


class TestAddRemove:

    def test_add_and_delete(self):
        the_homepage = Homepage()
        the_add_remove = AddRemove()

        the_homepage.navigate_to_page()
        the_homepage.text_is_present()
        the_homepage.add_remove_button_clickable()

        the_add_remove.text_is_present()
        the_add_remove.add_element_btn()
        the_add_remove.delete_element_btn()

    def test_add_and_delete_multiple(self):
        the_homepage = Homepage()
        the_add_remove = AddRemove()

        the_homepage.navigate_to_page()
        the_homepage.text_is_present()
        the_homepage.add_remove_button_clickable()

        the_add_remove.text_is_present()
        the_add_remove.add_element_btn()
        the_add_remove.add_element_btn()
        the_add_remove.add_element_btn()
        the_add_remove.add_element_btn()
        the_add_remove.delete_all_delete_btns()
