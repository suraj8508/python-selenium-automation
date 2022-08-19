from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    INPUT_FIELD = (By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute[aria-label="Search"]')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_BTN = (By.ID, 'nav-cart')
    ORDER_BTN = (By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPAN_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')


    def search_product(self, search_word):
        self.input_text(search_word, *self.INPUT_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_order(self, *locator):
        self.click(*self.ORDER_BTN)

    def click_cart(self, *locator):
        self.click(*self.CART_BTN)

    def hover_language(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_appliances(self):
        dept = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(dept)
        select.select_by_value("search-alias=appliances")


    def select_dept(self, alias):
        department = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department)
        select.select_by_value(f'search-alias={alias}')

    def verify_span_lang(self):
        self.wait_for_element_appear(*self.SPAN_LANG)


