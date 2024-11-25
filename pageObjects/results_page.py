from core.base_page import BasePage


class ResultsPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @staticmethod
    def verify_search_results(results, verification_text):
        for result in results:
            element_text = result.text
            lines = element_text.split('\n')
            product_name = lines[1]
            assert verification_text in element_text.lower(), f"Product name: '{product_name}' does not contain 'hello kitty'"

    @staticmethod
    def verify_products_ordered_ascending_by_price(results):
        prices = []
        for result in results:
            element_text = result.text
            price_match = re.search(r'(\d+\.\d+)\s?₪', element_text)
            if price_match:
                price = float(price_match.group(1))
                prices.append(price)
            else:
                print("Price not found in element:", element_text)

        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                print(f"Prices are not in ascending order: {prices[i - 1]} > {prices[i]}")
                return False

        print("All prices are in ascending order.")
        return True

