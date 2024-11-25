
from core.base_page import BasePage
from webLocators.web_locators import MainPageLocators


class MainPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_search_results(self, search_text):
        self.click_on_element(MainPageLocators.SEARCH_BUTTON)
        self.find_element_send_text_and_click_enter(MainPageLocators.SEARCH_INPUT, search_text)
        search_results = self.find_elements(MainPageLocators.SEARCH_RESULTS)
        return search_results











