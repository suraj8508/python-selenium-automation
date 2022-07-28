from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FIRST_PROD = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*FIRST_PROD).click()


# @then ('User sees the {search_result}')
# def search_results(context, search_result):
#     search_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold').text
#
#     assert expected_result == search_result, f"Expected {expected_result} not matched with Actual {actual_result}"


@then('User sees the {search_result}')
def verify_search_results(context, search_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold').text
    assert search_result == actual_result, f'Expected {search_result} but got {actual_result}'
