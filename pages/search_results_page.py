from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResult(Page):
    RESULT = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'div.sg-col-inner [data-component-type="s-search-result"]')

    def verify_search_results(self, expected_text, *locator):
        # actual_result = self.driver.find_element(*self.RESULT).text
        # assert search_result == actual_result, f'Expected {search_result} but got {actual_result}'
        self.verify_element_text(expected_text, *self.RESULT)

    def select_first_product(self, *locator):
        self.find_elements(*self.SEARCH_RESULT)
        self.click(*self.SEARCH_RESULT)
