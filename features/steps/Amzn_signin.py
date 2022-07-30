from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Varify Sign In page opened')
def open_signin(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result == actual_result, f"Expected {expected_result} not matched with Actual {actual_result}"


@then('User see email field')
def verify_email(context):
    context.driver.find_element(By.ID, 'ap_email').is_displayed()
