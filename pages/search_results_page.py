from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResult(Page):
    RESULT = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'div.sg-col-inner [data-component-type="s-search-result"]')
    DEPT_APPLIANCES = (By.CSS_SELECTOR, '#nav-subnav[data-category="appliances"]')
    NAV_DEPT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUBSTR}"]')

    def get_dept_locator(self, category):
        #By.CSS_SELECTOR, '#nav-subnav[data-category="{SUBSTR}"]
        return [self.NAV_DEPT[0], self.NAV_DEPT[1].replace("{SUBSTR}", category)]

    def verify_search_results(self, expected_text, *locator):
        # actual_result = self.driver.find_element(*self.RESULT).text
        # assert search_result == actual_result, f'Expected {search_result} but got {actual_result}'
        self.verify_element_text(expected_text, *self.RESULT)

    def select_first_product(self, *locator):
        self.find_elements(*self.SEARCH_RESULT)
        self.click(*self.SEARCH_RESULT)

    def verify_appliances_dept(self):
        self.wait_for_element_appear(*self.DEPT_APPLIANCES)

    def verify_dept_selected(self, category):
        locator = self.get_dept_locator(category)
        self.wait_for_element_appear(*locator)
"""
Am getting the Error message :
 File "features/steps/Amzn_search_results.py", line 76, in verify_dept_selected
    context.app.search_results_page.verify_dept_selected(category)
  File "/Users/sbt/Documents/automation/python-selenium-automation/pages/search_results_page.py", line 25, in verify_dept_selected
    self.wait_for_element_appear(*locator)
  File "/Users/sbt/Documents/automation/python-selenium-automation/pages/base_page.py", line 37, in wait_for_element_appear
    return self.wait.until(EC.presence_of_element_located(locator))
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/selenium/webdriver/support/wait.py", line 90, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:
"""
# I coded same as explained in the class.



