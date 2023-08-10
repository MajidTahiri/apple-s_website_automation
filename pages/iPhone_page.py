from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class IphonePage(Page):
    SHOP_IPHONE_LINK = (By.CSS_SELECTOR, ".ribbon-link")


    def click_shop_iphone_link(self):
        self.wait_for_element_click(*self.SHOP_IPHONE_LINK)



