from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '.nav-hasArrow[aria-label="New Arrivals"]')
    ITEM_CATEGORY_WOMEN = (By.CSS_SELECTOR, 'a[href*="fashion-womens"]')

    def open_prod_page(self):
        self.open_url(end_url='/gp/product/B074TBCSC8')

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_category_women(self):
        self.wait_for_element_appear(*self.ITEM_CATEGORY_WOMEN)

    def add_to_cart(self, *locator):
        self.click(*self.ADD_TO_CART_BTN)

