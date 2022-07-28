from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL_BTN=(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
CART = (By.ID, 'nav-cart-count')


@when('Open the Cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then ('Verify Cart has {actl_count} item(s)')
def verify_cart(context, actl_count):
    exp_count = context.driver.find_element(*CART).text
    # exp_count = int(exp_count)
    assert actl_count == exp_count, f"Mismatch between {actl_count} and {exp_count}"





# @then('User see Empty Cart page')
# def verify_empty_cart(context):
#     # expected_result = "Your Amazon Cart is empty"
#     # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
#     context.driver.find_element(*EMAIL_BTN).is_displayed()
#     # assert expected_result == actual_result