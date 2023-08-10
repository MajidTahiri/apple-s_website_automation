from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SigninPage(Page):

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.as-l-container.rs-sign-in-header")


    def verify_signin_page_is_opened(self, expected_text):
        actual_text = self.verify_partial_text(expected_text, *self.PAGE_TITLE).text.strip()
        assert expected_text == actual_text, f"Expected title '{expected_text}', but got '{actual_text}'"

