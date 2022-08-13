from selenium.webdriver.common.by import By
from pages.base_page import Page


class BestSellerPage(Page):

    def open_best_seller(self):
        self.open_url(end_url='gp/bestsellers')

