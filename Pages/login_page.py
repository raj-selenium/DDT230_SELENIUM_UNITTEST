from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Pages.dashboard_page import DashboardPage


class LoginPage(BasePage):

    #locators
    __uname_tbox = By.ID, "txtUsername"
    __upass_tbox = By.ID, "txtPassword"
    __login_btn = By.ID, "btnLogin"
    __err_msg_text = By.ID, "spanMessage"

    def _enter_username(self, username):
        self._input_text(self.__uname_tbox, username)

    def _enter_password(self, password):
        self._input_text(self.__upass_tbox, password)

    def _click_login(self):
        self._click_element(self.__login_btn)

    def login(self, username, password, scenario ="pass"):
        self._enter_username(username)
        self._enter_password(password)
        self._click_login()
        if scenario == "pass":
            return DashboardPage(self.driver)
        elif scenario == "fail":
            return LoginPage(self.driver)



    def get_err_msg(self):
        return self._get_text(self.__err_msg_text)
