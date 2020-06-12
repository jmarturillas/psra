import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "pagefactory")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

import random


class Loginpage(object):

    user_name = "jamesmart2991@gmail.com"
    password = "Jamlie29!"

    lbl_login = "//div[@class='panel-title']"
    txt_user = "//input[@id='userIdentifier']"
    lnk_register = "//a[@href='/en/registration']"
    panel_language = "//div[@id='react-language-list-container']"

    lnk_privacy = "//a[contains(., 'Privacy Policy')]"
    lnk_service = "//a[contains(., 'Service agreements')]"
    lnk_safe_usage = "//a[contains(., 'Recommendations for the safe usage')]"

    btn_login = "//button[@class='btn btn-primary btn-block btn-rounded text-uppercase']"

    lbl_user_name = "//div[@class='row user-identifier-row']/div/strong"

    img_avatar = "//img[@alt='avatar']"

    btn_edit_user = "//i[@class='ti-pencil']"

    login_method_container = "//div[@id='login-methods']"
    header_mobile_app = "//div[@id='login-methods-heading-app_credentials']"
    header_password = "//div[@id='login-methods-heading-user_credentials']"

    txt_password = "//input[@id='password']"

    btn_login_user = "//button[@class='btn btn-primary btn-block btn-rounded text-uppercase']"  # select the second ones

    lnk_forgot_pw = "//a[contains(., 'Forgot password?')]"

    btn_logout = "//span[contains(., 'Log out')]"

    err_invalid_user = "//div[@class='alert alert-danger']/div"

    err_invalid_pw = "//div[@class='alert alert-danger']/div/span[contains(.,'Incorrect password. Please try again.')]"

    loader_icon = "//div[@class='Loader__message']"

    @staticmethod
    def txt_user_editable(name=""):
        elem = "//input[@id='userIdentifier'][@value='{}']".format(name)
        return elem


