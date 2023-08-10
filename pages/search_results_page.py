from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SearchResultsPage(Page):

    IPHONE_14_RESULT = (By.XPATH, "//*[text()='iPhone 14 and iPhone 14 Plus']")

    def verify_correct_page_opened(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL '{expected_url}', but got '{actual_url}'"


    def verify_iphone_14_found(self, expected_text):
        self.verify_element_text(expected_text,*self.IPHONE_14_RESULT)






