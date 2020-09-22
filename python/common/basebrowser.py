from selenium import webdriver


class BrowserExample:

    def __init__(self):
        self.browser = webdriver.Chrome()

    def navigate_to_page(self):
        self.browser.get('https://the-internet.herokuapp.com/')
