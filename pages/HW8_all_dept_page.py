from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class AllDept(Page):
    DEPT_SELECT = (By.ID, 'searchDropdownBox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SEARCH_BOX = (By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute[aria-label="Search"]')
    DEPT_NAME = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUBSTR}"]')

    def select_computers_dept(self, alias):
        dept = self.find_element(*self.DEPT_SELECT)
        select = Select(dept)
        select.select_by_value(f'search-alias={alias}')

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_BOX)
        self.click(*self.SEARCH_ICON)

    def get_substr_locator(self, category):
        return [self.DEPT_NAME[0], self.DEPT_NAME[1].replace('{SUBSTR}', category)]

    def verify_dept_selected(self, category):
        locator = self.get_substr_locator(category)
        self.wait_for_element_appear(*locator)



