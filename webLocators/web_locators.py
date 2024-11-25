from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='qa-header-login-button']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@id='qa-login-email-input']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@id='qa-login-password-input']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='qa-login-submit']")


class MainPageLocators:
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test-id='qa-header-search-button']")
    SEARCH_INPUT = (By.XPATH, "//input[@data-test='search-input']")
    SEARCH_RESULTS = (By.XPATH, "//*[contains(@class, 'product-list_')]/li")


class ProductPageLocators:
    PRODUCT_PRICE = (By.XPATH, "//div[@data-test-id='qa-pdp-price-final']")



