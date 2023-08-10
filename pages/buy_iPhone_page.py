import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class BuyIphonePage(Page):
    IPHONE_14 = (By.CSS_SELECTOR, "a[href='https://www.apple.com/shop/buy-iphone/iphone-14")
    SELECT_IPHONE_14 = (By.CSS_SELECTOR, ".rf-bfe-column-right .rc-dimension .form-selector-label")
    SELECT_IPHONE_COLOR = (By.CSS_SELECTOR, ".colornav-item")
    SELECT_STORAGE = (By.CSS_SELECTOR, ".rc-dimension-selector-row.form-selector")
    NO_TRADE_IN = (By.ID, "noTradeIn_label")
    PAYMENT_OPTION = (By.CSS_SELECTOR, ".rf-po-bfe-dimension-base-option")
    CHOOSE_CARRIER = (By.CSS_SELECTOR, ".rc-dimension-multiple")
    CHOOSE_COVERAGE = (By.ID, "applecareplus_58_noapplecare_label")
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart")
    REVIEW_BAG = (By.CSS_SELECTOR, ".rc-summaryheader-right")


    def select_iphone_model(self):
        self.wait_for_element_click(*self.IPHONE_14)

    def select_iphone_14(self):
        self.click_element_by_index(*self.SELECT_IPHONE_14, index=0)

    def select_iphone_color(self):
        self.click_element_by_index(*self.SELECT_IPHONE_COLOR, index=1)

    def select_iphone_storage(self):
        self.click_element_by_index(*self.SELECT_STORAGE, index=2)  # available indexes are 2, 3, and 4

    def select_no_trade_in(self):
        self.wait_for_element_click(*self.NO_TRADE_IN)

    def select_payment_option(self):
        self.click_element_by_index(*self.PAYMENT_OPTION, index=0)  # available indexes are 0, 1, and 2

    def choose_carrier(self):
        self.click_element_by_index(*self.CHOOSE_CARRIER, index=10)  # available indexes are 7, 8, 9, 10


    def choose_coverage(self):
        self.wait_for_element_click(*self.CHOOSE_COVERAGE)


    def add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART)


    def review_bag(self):
        self.wait_for_element_click(*self.REVIEW_BAG)







