from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResult
from pages.signin_page import SigninPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.HW8_all_dept_page import AllDept


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResult(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.HW8_all_dept_page = AllDept(self.driver)
