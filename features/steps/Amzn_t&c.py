from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
PRIVACY_PAGE_HEADING = (By.CSS_SELECTOR, 'a.cs-help-title')


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get(
        "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 "
    )


@when('Store Original Window')
def store_org_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRIVACY_NOTICE)).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)
    sleep(2)


@then('Verify Amazon Privacy Notice page is opened')
def varify_privacy_page(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer'))

    expected_result = "Help & Customer Service"
    actual_result = context.driver.find_element(*PRIVACY_PAGE_HEADING).text
    assert actual_result == expected_result, f"Expected {expected_result} not " \
                                             f"matching {actual_result}"


@then('User can close new window and switch back to original')
def switch_to_org_window(context):
    context.driver.switch_to.window(context.original_window)
    sleep(5)
