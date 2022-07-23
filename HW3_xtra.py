import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Search for laptop
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('laptop')
driver.find_element(By.ID, 'nav-search-submit-button').click()

# Verifying the Laptop page displayed
expect_result = '"laptop"'
actual_result = driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text


assert expect_result == actual_result, f"Expected {expect_result} not matching {actual_result}"

# Selecting the first one from the list
driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]").click()

# Adding the Item to the Cart
driver.find_element(By.CSS_SELECTOR, 'input#add-to-cart-button[name="submit.add-to-cart"]').click()

# Avoiding the extra Protection Info
# time.sleep(3)
# add_button = driver.find_element(By.CSS_SELECTOR, '[data-asin="B07P6YXMZ5"][aria-labelledby="attachSiAddCoverage-announce"]')
#
# print(add_button.is_enabled())
# print(add_button.is_displayed())

# Selecting the Cart to Display the item
# driver.find_element(By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attach-sidesheet-view-cart-button-announce"]').click()
driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

# Verifying the Item selected is displayed in the cart
expected_res = "Subtotal (1 item):"
actual_res = driver.find_element(By.ID, 'sc-subtotal-label-activecart').text()

assert expected_res == actual_res, f" the {actual_res} and {expected_res} not matching"

driver.quit()