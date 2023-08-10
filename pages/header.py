from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Header(Page):

    IPHONE_LINK = (By.CSS_SELECTOR, ".globalnav-link-iphone")
    SHOPPING_BAG = (By.ID, "globalnav-menubutton-link-bag")
    STORES_LINK = (By.CSS_SELECTOR, ".globalnav-link-store")
    SEARCH_ICON = (By.ID, "globalnav-menubutton-link-search")
    APPLE_LOGO = (By.CSS_SELECTOR, ".globalnav-link-apple")


    def click_iphone_link(self):
        self.click_element_by_index(*self.IPHONE_LINK, index=0)

    def open_shopping_cart(self):
        self.click(*self.SHOPPING_BAG)

    def click_store_link(self):
        self.wait_for_element_click(*self.STORES_LINK)

    def click_search_icon(self):
        self.wait_for_element_click(*self.SEARCH_ICON)

    def hover_over_iphone_link(self):
        iphone_link_element = self.find_element(*self.IPHONE_LINK)
        iphone_link_element.is_displayed()
        self.hover_over_element(iphone_link_element)

    def click_apple_logo(self):
        self.click(*self.APPLE_LOGO)



