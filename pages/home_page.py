from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class HomePage(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, ".globalnav-searchfield-input")
    SIGNIN_LINK = (By.CSS_SELECTOR, ".ac-gn-bagview-nav-link")
    IPHONE_14_PRO = (By.XPATH, "//a[text()='Explore All iPhone']")



    def search_for_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_signin_link(self):
        self.click_element_by_index(*self.SIGNIN_LINK, index=3)

    def click_iphone_14_pro(self):
        self.wait_for_element_visibility(*self.IPHONE_14_PRO)


