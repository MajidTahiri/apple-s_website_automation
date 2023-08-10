from selenium.common import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from support.logger import logger


class Page:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://www.apple.com/'


    def open_url(self, url=''):
        print(f'Opening URL: {url}')
        logger.info(f'Opening URL: {url}')
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def click(self, *locator):
        logger.info('Clicking on {}, {}'.format(*locator))
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        # element.send_keys(Keys.RETURN)  # Simulate pressing the "Enter" key after typing the search query
        element.submit()
        print(f'Inputting text: {text}')


    def wait_for_element_click(self, *locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator),
                                      message=f'Element not clickable by {locator}')
            element.click()
        except StaleElementReferenceException:
            element = self.wait.until(EC.element_to_be_clickable(locator),
                                      message=f'Element not clickable by {locator}')
            element.click()


    def click_element_by_index(self, *locator, index):
        try:
            self.wait.until(EC.presence_of_all_elements_located(locator), message=f'Element not clickable by {locator}')
            elements = self.driver.find_elements(*locator)
            element = elements[index]
            element.click()
        except StaleElementReferenceException:
            # If the element reference becomes stale, re-find the element and try clicking again.
            elements = self.driver.find_elements(*locator)
            element = elements[index]
            element.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))


    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_element_text(self, expected_text, *locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            actual_text = self.driver.find_element(*locator).text
        except TimeoutException:
            raise NoSuchElementException(f"Element not found by locator {locator}")

        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'


    def verify_partial_text(self, expected_text, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found by locator {locator}")


    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def hover_over_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def wait_for_element_visibility(self, *locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)



