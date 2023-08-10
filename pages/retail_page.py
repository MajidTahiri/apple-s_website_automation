from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class RetailPage(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, ".form-textbox-input")

    def find_store_by_location(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)


    def switch_to_original_window(self, original_window):
        self.driver.switch_to.window(original_window)



