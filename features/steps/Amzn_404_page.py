from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


DOG_IMAGE = (By.CSS_SELECTOR, 'img#d')


@given('Store Original Window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('original window:', context.original_window)


@when('Click on the Dog Image')
def click_dog_img(context):
    sleep(3)
    context.driver.wait.until(
        EC.element_to_be_clickable(DOG_IMAGE), message="Dog Image NOt Clickable"
    ).click()


@when('Switch to New Window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    # print("Current Window: ", context.driver.window_handles)
    # ['CDwindow-50E152619F008FFEE5922AFE0A6A2591','CDwindow-15571AB4AB932CC7D2ADC58DEC36A896']
    # Index is [0, 1] , where '0' is the old/current window and '1' is the new window.

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    sleep(2)


@then('Verify the Blog is opened')
def verify_blog_open(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace'))
    sleep(3)


@then('Close the blog')
def close_blog(context):
    context.driver.close()
    sleep(2)


@then('Return to Original Window')
def return_to_org_window(context):
    context.driver.switch_to.window(context.original_window)
