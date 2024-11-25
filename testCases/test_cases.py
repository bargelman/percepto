import pytest

from pageObjects.product_page import ProductPage
from pageObjects.results_page import ResultsPage
from pageObjects.main_page import MainPage


@pytest.mark.usefixtures("setup")
class Tests:

    def test_check_if_all_the_dropdown_results_contains_the_phrase_hellokitty(self, setup):
        main_page = MainPage(self.driver)
        search_results = main_page.get_search_results("hello")
        results_page = ResultsPage(self.driver)
        results_page.verify_search_results(search_results, "hello kitty")

    def test_check_if_the_products_ordered_ascending_by_the_price(self, setup):
        main_page = MainPage(self.driver)
        search_results = main_page.get_search_results("hello")
        results_page = ResultsPage(self.driver)
        assert results_page.verify_products_ordered_ascending_by_price(search_results)

    def test_verify_price_in_the_product_page_and_the_text_size(self, setup):
        main_page = MainPage(self.driver)
        search_results = main_page.get_search_results("hello")
        search_results[2].click()
        product_page = ProductPage(self.driver)
        product_page.verify_text_font_size("28.8px")    # 1.8rem = 28.8px


