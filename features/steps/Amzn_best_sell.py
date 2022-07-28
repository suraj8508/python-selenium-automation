from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BEST_SELL_BTN = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"].nav-a  ')
BEST_MENU_LINKS = (By.ID, 'zg_header a')
T_DEAL_MENU_LINKS = (By.CSS_SELECTOR, 'div#nav-subnav a')
CUST_SERVICE_LINKS = (By.CSS_SELECTOR, 'div.issue-card-wrapper')


# @given ('Amazon Best Sellers page')
# def open_bestsellers(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when ('User Select Best Sellers')
def open_bestsellers(context):
    context.driver.find_element(*BEST_SELL_BTN).click()



# @then ('User Verifies the Number of Links')
# def verify_links(context):
#     link = context.driver.find_elements(By.CSS_SELECTOR, 'div[class*=_p13n-zg-nav-tab-all_style_zg-tabs-li]')

@then('User Verifies {link_counts}Links')
# def verify_best_links(context, link_counts):
#     link_counts = int(link_counts)
#     menu_items = context.driver.find_elements(*BEST_MENU_LINKS)
#
#     assert len(menu_items) == link_counts, f"Links expected {link_counts} not matching with {len(menu_items)}"
#
# def verify_tdeals_links(context, link_counts):
#     link_counts = int(link_counts)
#     menu_items = context.driver.find_elements(*T_DEAL_MENU_LINKS)
#
#     assert len(menu_items) == link_counts, f"Links expected {link_counts} not matching with {len(menu_items)}"


def verify_cust_serv_links(context, link_counts):
    link_counts = int(link_counts)
    menu_items = context.driver.find_elements(*CUST_SERVICE_LINKS)

    assert len(menu_items) == link_counts, f"Links expected {link_counts} not matching with {len(menu_items)}"
