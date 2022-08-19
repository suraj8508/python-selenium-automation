from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FIRST_PROD = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
PROD_NAME = (By.ID, 'productTitle')
PROD_TITLE = (By. CSS_SELECTOR, 'h2.a-size-mini')
PROD_IMG = (By.CSS_SELECTOR,'[data-component-type="s-product-image"]')
PROD_SCH_RES = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
PROD_PAGES = (By.CSS_SELECTOR, 'span.s-pagination-item')
CURR_PAGE_NUM = (By.CSS_SELECTOR, 'span.s-pagination-selected')


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*FIRST_PROD).click()


@when('Store product name')
def store_prod_name(context):
    context.prod_name = context.driver.find_element(*PROD_NAME).text
    print(f"Current Product Name is {context.prod_name}")


# @then ('User sees the {search_result}')
# def search_results(context, search_result):
#     search_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold').text
#
#     assert expected_result == search_result, f"Expected {expected_result} not matched with Actual {actual_result}"


@then('User sees the {search_result}')
def verify_search_results(context, search_result):
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold').text
    # assert search_result == actual_result, f'Expected {search_result} but got {actual_result}'
    context.app.search_results_page.verify_search_results(search_result)


@then('Verify every product has a name and image')
# def verify_prod_name_img(context):
#     all_products = context.driver.find_elements(*PROD_SCH_RES)
#     for product in all_products:
#         print(product)
#         print(product.text)
#         title = product.find_element(*PROD_TITLE).text
#         print("\n\nProduct Title: ", title)
#         assert title, 'Error, title is not matching or blank'
#         product.find_element(*PROD_IMG)
#         print("IMG Element", product.find_element(*PROD_IMG))

def verify_multi_pages(context):
    all_pages = context.driver.find_elements(*PROD_PAGES)
    for page in all_pages:
        curr_page = page.find_element(*CURR_PAGE_NUM).click()
        if curr_page != ' ':
            verify_prd_nm_img(curr_page)


def verify_prd_nm_img(context):
    all_products = context.driver.find_elements(*PROD_SCH_RES)
    for product in all_products:
        title = product.find_element(*PROD_TITLE).text
        assert title, 'Error, title is not matching or blank'
        product.find_element(*PROD_IMG)


@then('User select the first product')
def select_first_prod(context):
    context.app.search_results_page.select_first_product()


@then('Verify {category} department is selected')
def verify_dept_selected(context, category):
    context.app.search_results_page.verify_dept_selected(category)


@then('Verify Appliances Dept is Selected')
def verify_appliances_dept(context):
    context.app.search_results_page.verify_appliances_dept()
