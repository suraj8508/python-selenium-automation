from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    INPUT_FIELD = (By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute[aria-label="Search"]')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_BTN = (By.ID, 'nav-cart')
    ORDER_BTN = (By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_order(self, *locator):
        self.click(*self.ORDER_BTN)

    def click_cart(self, *locator):
        self.click(*self.CART_BTN)