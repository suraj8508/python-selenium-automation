from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_CART_BTN = (By.CSS_SELECTOR, 'input#add-to-cart-button[name="submit.add-to-cart"]')


@when ('Click on add to Cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()