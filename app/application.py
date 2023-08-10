from pages.base_page import Page
from pages.home_page import HomePage
from pages.header import Header
from pages.iPhone_page import IphonePage
from pages.buy_iPhone_page import BuyIphonePage
from pages.search_results_page import SearchResultsPage
from pages.stores_page import StoresPage
from pages.retail_page import RetailPage
from pages.signin_page import SigninPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.home_page = HomePage(self.driver)
        self.header = Header(self.driver)
        self.iPhone_page = IphonePage(self.driver)
        self.buy_iPhone_page = BuyIphonePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.stores_page = StoresPage(self.driver)
        self.retail_page = RetailPage(self.driver)
        self.signin_page = SigninPage(self.driver)

