from selenium.webdriver.common.by import By
from behave import given, when, then

CART_BTN = (By.ID, 'nav-cart')
ORDER_BTN =(By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']")
INPUT_FIELD = (By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute[aria-label="Search"]')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR,'table.navFooterMoreOnAmazon td a')

@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word} on amazon')
def search_products(context, search_word):
    context.driver.find_element(*INPUT_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_ICON).click()



@when('Click on Order button')
def select_orders(context):
    context.driver.find_element(*ORDER_BTN).click()


@when('Selecting cart from homepage')
def select_cart(context):
    context.driver.find_element(*CART_BTN).click()

@then('Verify Hamburger Menu displayed')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU)

@then('Verify {link_counts} footer links')
def verify_links(context, link_counts):
    link_counts = int(link_counts)
    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == link_counts, f"Links expected {link_counts} not matching with {len(links)}"

