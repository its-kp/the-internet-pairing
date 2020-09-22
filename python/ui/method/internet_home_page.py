from python.common.baseui import BasicFunctions
from selenium.webdriver.common.by import By


class Homepage(BasicFunctions):
    header_text = (By.XPATH, '//*[@id="content"]/h1')
    add_button = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')

    def text_is_present(self):
        self.verify_is_present(self.header_text)

    def add_remove_button_clickable(self):
        self.mouse_click(self.add_button)

    def navigate_to_page(self):
        self.browser.get('https://the-internet.herokuapp.com/')
        