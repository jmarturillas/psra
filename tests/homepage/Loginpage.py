import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "tests")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from globals import config
from pagefactory.homepage import Loginpage as elem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from globals.functions import Functions
import random
import time


class Loginpage(object):

    def __init__(self, browser='chrome'):
        self.browser = browser
        self.driver = None
        self.wait = WebDriverWait(self.driver, 10)
        self.func = Functions(self.driver)
        self.choice = None
        self.selected_category = None
        self.random_category_text = None

        self.login_url = "https://bank.paysera.com/en/login"

    def open_browser(self, url: str = "https://bank.paysera.com/en/login"):
        self.driver = config.Config().get_browser(self.browser)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.func = Functions(self.driver)
        self.func.open_browser(url=url)
        self.func.wait_until_page_is_loaded()

    def close_browser(self):
        self.driver.quit()

    def assert_url(self, url=None):
        assert self.func.is_expected_url(url) is True

    def assert_element_is_present_in_the_page(self, element=""):
        if element.lower() == "login label":
            assert self.func.is_element_present(elem.Loginpage.lbl_login) is True
        elif element.lower() == "input box":
            assert self.func.is_element_present(elem.Loginpage.txt_user) is True
        elif element.lower() == "register now!":
            assert self.func.is_element_present(elem.Loginpage.lnk_register) is True
        elif element.lower() == "language option links":
            assert self.func.is_element_present(elem.Loginpage.panel_language) is True
        elif element.lower() == "privacy policy":
            assert self.func.is_element_present(elem.Loginpage.lnk_privacy) is True
        elif element.lower() == "service agreements":
            assert self.func.is_element_present(elem.Loginpage.lnk_service) is True
        elif element.lower() == "recommendations for the safe usage":
            assert self.func.is_element_present(elem.Loginpage.lnk_safe_usage) is True
        elif element.lower() == "username label":
            assert self.func.is_element_present(elem.Loginpage.lbl_user_name) is True
        elif element.lower() == "login method":
            assert self.func.is_element_present(elem.Loginpage.login_method_container) is True
        elif element.lower() == "mobile app header":
            assert self.func.is_element_present(elem.Loginpage.header_mobile_app) is True
        elif element.lower() == "password header":
            assert self.func.is_element_present(elem.Loginpage.header_password) is True
        elif element.lower() == "password field":
            assert self.func.is_element_present(elem.Loginpage.txt_password) is True
        elif element.lower() == "forgot password":
            assert self.func.is_element_present(elem.Loginpage.lnk_forgot_pw) is True
        elif element.lower() == "logout":
            assert self.func.is_element_present(elem.Loginpage.btn_logout) is True
        elif element.lower() == "invalid user":
            self.wait.until(ec.visibility_of_element_located((By.XPATH, elem.Loginpage.err_invalid_user)))
            assert self.func.is_element_present(elem.Loginpage.err_invalid_user) is True
        elif element.lower() == "wrong password":
            self.wait.until(ec.visibility_of_element_located((By.XPATH, elem.Loginpage.err_invalid_pw)))
            assert self.func.is_element_present(elem.Loginpage.err_invalid_pw) is True
        elif element.lower() == "avatar":
            time.sleep(2)
            assert self.func.is_element_present(elem.Loginpage.img_avatar) is True
            self.driver.back()
        else:
            raise Exception("This element is not yet supported in this automation.")

        time.sleep(1)

    def assert_input_element_contains_text(self, element="", text=""):
        if element.lower() == "username field":
            assert self.func.is_input_element_contains_text(elem.Loginpage.txt_user_editable(text)) is True

    def input_username(self, username=""):
        self.func.input_text(elem.Loginpage.txt_user, username)

    def input_password(self, password=""):
        self.func.input_text(elem.Loginpage.txt_password, password)

    def click_login(self):
        self.func.click_element(elem.Loginpage.btn_login)
        self.driver.implicitly_wait(10)
        self.func.wait_until_page_is_loaded()

    def login_with_web_app(self):
        logins = self.driver.find_elements_by_xpath(elem.Loginpage.btn_login_user)
        logins[1].click()
        self.driver.implicitly_wait(10)
        self.func.wait_until_page_is_loaded()

    def click_edit_username(self):
        self.func.click_element(elem.Loginpage.btn_edit_user)

    def click_password_header_to_select_it_as_login_method(self):
        # the delay here looks so long because the PASSWORD header # seems to be unclickable until certain period of time
        time.sleep(20)
        self.func.click_element(elem.Loginpage.header_password)

    def click_logout(self):
        self.func.click_element(elem.Loginpage.btn_logout)
