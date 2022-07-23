from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

T_DEAL_BTN = (By.CSS_SELECTOR, 'a[href="/deals?ref_=nav_cs_gb"].nav-a  ')
# T_DEAL_MENU_LINKS = (By.CSS_SELECTOR, 'div#nav-subnav a')


@when("User Select Today's Deal")
def open_t_deal(context):
    context.driver.find_element(*T_DEAL_BTN).click()


# @then('User Verifies {link_count}Links')
# def verify_links(context, link_count):
#     link_count = int(link_count)
#     menu_items = context.driver.find_elements(*T_DEAL_MENU_LINKS)
#
#     assert len(menu_items) == link_count, f"Links expected {link_count} not matching with {len(menu_items)}"
