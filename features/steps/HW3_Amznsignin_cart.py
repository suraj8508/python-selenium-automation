from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('selecting the Order Button from top right side')
def select_orders(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']").click()

@then('User sees Sign In page')
def open_signin(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result == actual_result, f"Expected {expected_result} not matched with Actual {actual_result}"

@then('User see email field')
def verify_email(context):
    context.driver.find_element(By.ID, 'ap_email').is_displayed()


@when('Selecting cart from homepage')
def select_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()

@then('User see Empty Cart page')
def verify_empty_cart(context):
    # expected_result = "Your Amazon Cart is empty"
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').is_displayed()
    # assert expected_result == actual_result
