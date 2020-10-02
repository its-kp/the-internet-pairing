from python.common.baseui import BasicFunctions
from selenium.webdriver.common.by import By


class Dropdown(BasicFunctions):
    dropdown_header_text = dropdown_list_header_text = (By.XPATH, '//*[@id="content"]/div/h3')
    dropdown_btn = (By.XPATH, '//*[@id="dropdown"]')
    dropdown_select_option_one = (By.XPATH, '//*[@id="dropdown"]/option[2]')
    dropdown_select_option_two = (By.XPATH, '//*[@id="dropdown"]/option[3]')

    def text_is_present(self):
        self.verify_is_present(self.dropdown_list_header_text)

    def dropdown_button_clickable(self):
        self.mouse_click(self.dropdown_btn)

    def first_option_select(self):
        self.mouse_click(self.dropdown_select_option_one)

    def second_option_select(self):
        self.mouse_click(self.dropdown_select_option_two)
