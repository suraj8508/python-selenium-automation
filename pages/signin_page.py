from selenium.webdriver.common.by import By
from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_signin_page(self, expected_text, *locator):
        # expected_text = "Sign-In"
        self.verify_element_text(expected_text, *self.SIGNIN_TEXT)

