from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasicFunctions:

    def __init__(self, browser):
        self.browser = browser

    def mouse_click(self, element):
        WebDriverWait(self.browser, 0.5).until(EC.element_to_be_clickable(element)).click()

    def verify_is_present(self, element):
        WebDriverWait(self.browser, 0.5).until(EC.element_to_be_clickable(element))

    def find_multiple(self, element):
        return self.browser.find_elements_by_xpath(element[1])
