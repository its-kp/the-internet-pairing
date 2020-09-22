from python.common.baseui import BasicFunctions
from selenium.webdriver.common.by import By


class AddRemove(BasicFunctions):
    add_remove_header_text = (By.XPATH, '//*[@id="content"]/h3')
    add_element_btn = (By.XPATH, '//*[@id="content"]/div/button')
    delete_element_btn = (By.XPATH, '//*[@id="elements"]/button')

    def text_is_present(self):
        self.verify_is_present(self.add_remove_header_text)

    def add_element_button_clickable(self):
        self.mouse_click(self.add_element_btn)

    def delete_element_button_clickable(self):
        self.mouse_click(self.delete_element_btn)

    def delete_all_delete_btns(self):
        all_deletes = self.find_multiple(self.delete_element_btn)

        for each in all_deletes:
            each.click()
