from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CUST_SERV_BTN = (By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display."].nav-a  ')


@when ('User Open Customer Service Page')
def open_cust_serv(context):
    context.driver.find_element(*CUST_SERV_BTN).click()