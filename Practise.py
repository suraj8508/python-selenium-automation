# import Utility
#
# numbers = [23, 45, 54, 34, 56, 65]
# print(Utility.find_max(numbers))
#
# print(Utility.kgs_to_lbs(56))
#
# print(Utility.lbs_to_kgs(124))
#
#
# from Utility import find_max, kgs_to_lbs, lbs_to_kgs
#
# numbers = [23, 45, 54, 34, 56, 65]
# print(find_max(numbers))
#
# print(kgs_to_lbs(56))
#
# print(lbs_to_kgs(124))

from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# selecting the Order Button from top right side
driver.find_element(By.CSS_SELECTOR, '.nav-cart-icon nav-sprite').click()

# Verifying the Sign-In page opened
expected_result = "Sign-In"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result == actual_result, f"Expected {expected_result} not matched with Actual {actual_result}"

# Email Input Field Verification
expected_result = "Email or mobile phone number"
actual_result = driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']//label[@class='a-form-label']").text

assert expected_result == actual_result, f"Expected {expected_result} not matched with Actual {actual_result}"

driver.find_element(By.ID, 'ap_email').send_keys('john123@abc.com')


print("Test case passed")

driver.quit()