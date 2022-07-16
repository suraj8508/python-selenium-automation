"""
Amazon Logo ( in Create New Account Page):
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

Create Account:
driver.find_element(By>CSS_SELECTOR, '.a-spacing-small')
driver.find_element(By>CSS_SELECTOR, 'h1.a-spacing-small')

Name Input Field:
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(BY.CSS_SELECTOR, 'input.a-input-text.a-span12[type="text"]')
driver.find_element(BY.CSS_SELECTOR, '.a-input-text.a-span12[type="text"]')

Email Input Field:
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.CSS_SELECTOR, '.a-span12.auth-require-claim-validation')
driver.find_element(By.CSS_SELECTOR, '[tabindex="3"][autocomplete="email"]')

Password Input Field:
driver.find_element(By.ID, 'ap_password')
driver.find_element(By. CSS_SELECTOR, '[name="password"].auth-required-field')

Password requirement: # used tag2 class inside tag1
driver.find_element(By.CSS_SELECTOR, 'i div.a-alert-content')

Password Re-Enter:
driver.find_element(BY.ID, 'ap_password_check')
driver.find_element(By.CSS_SELECTOR, '[type="password"][name="passwordCheck"].auth-required-field')

Continue or Create Account :
driver.find_element(By.ID, 'continue')
driver.find_element(By.CSS_SELECTOR, '.a-button-input[type="submit"]')

Conditions of Use:
driver.find_element(By.CSS_SELECTOR, 'a[href*="register_notification_condition_of_use"]')
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"]')

Privacy Notice:
driver.find_element(By.CSS_SELECTOR, 'a[href*="register_notification_privacy_notice"]')

Sign-in, for Existing Account:
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis[href*="/ap/signin?openid.pape.max_auth_age"]')

Create a Free Business Account:
driver.find_element(By.ID, 'ab-registration-link')
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis[href*="www.amazon.com/business/register/org/landing?"]')








"""