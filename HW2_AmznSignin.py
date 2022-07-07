from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# selecting the Order Button from top right side
driver.find_element(By.XPATH, "//a[@id='nav-orders']//span[@class='nav-line-2']").click()

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