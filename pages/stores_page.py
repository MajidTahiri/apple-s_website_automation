from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class StoresPage(Page):

    FIND_STORE = (By.CSS_SELECTOR, ".rs-shop-neareststore-content")

    def click_find_store(self):
        current_window = self.driver.current_window_handle
        self.wait_for_element_click(*self.FIND_STORE)
        return current_window

    def verify_store_locator_page_open(self, expected_url, current_window):
        all_windows = self.driver.window_handles
        # new_window = [window for window in all_windows if window != current_window][0]
        new_window = None
        for window in all_windows:
            if window != current_window:
                new_window = window
                break
        self.driver.switch_to.window(new_window)

        self.wait.until(EC.url_contains(expected_url))
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f"Expected URL '{expected_url}' to be part of '{actual_url}'"



