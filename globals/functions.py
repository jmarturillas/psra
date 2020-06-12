import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "globals")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import time

class Functions(object):

    def __init__(self, driver=None):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_browser(self, url=None):
        self.driver.get(url)

    def click_element(self, element):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, element)))
        self.driver.find_element_by_xpath(element).click()
        time.sleep(1.5)

    def is_input_element_contains_text(self, element=None) -> bool:
        count = self.count_elements(element)
        if count > 0:
            return True
        return False

    def count_elements(self, element) -> int:
        count = len(self.driver.find_elements_by_xpath(element))
        return count

    def is_element_present(self, element) -> bool:
        count = self.count_elements(element)
        if count > 0:
            return True
        return False

    def is_expected_url(self, url) -> bool:
        current = self.driver.current_url
        if url == current:
            return True
        return False

    def wait_until_page_is_loaded(self):
        page_state = None
        while page_state != 'complete':
            time.sleep(1)
            page_state = self.driver.execute_script('return document.readyState;')

    def input_text(self, element="", text=""):
        self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(text)
