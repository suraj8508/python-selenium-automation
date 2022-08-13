from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty h2')

    def verify_cart_empty(self, expected_text, *locator):
        self.verify_element_text(expected_text, *self.CART_EMPTY_TEXT)
