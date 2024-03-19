import time

from locators.elements_page_locator import TextBoxPageLocator
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocator


    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('asdf')
        self.element_is_visible(self.locators.EMAIL).send_keys('asdf@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('asdf')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('asdf')
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)