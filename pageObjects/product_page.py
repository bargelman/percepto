
from core.base_page import BasePage
from webLocators.web_locators import ProductPageLocators


class ProductPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_product_price_is_exists(self):
        product_price = self.get_text(ProductPageLocators.PRODUCT_PRICE)
        if product_price:
            return product_price

    def verify_text_font_size(self, expected_font_size):
        element = self.find_element(ProductPageLocators.PRODUCT_PRICE)
        if element:
            actual_font_size = element.value_of_css_property('font-size')
            if actual_font_size == expected_font_size:
                print(f"Font size is correct: {actual_font_size}")
                return True
            else:
                print(f"Font size is incorrect. Expected: {expected_font_size}, but got: {actual_font_size}")
                return False


