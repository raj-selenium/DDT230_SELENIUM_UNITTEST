import os
import unittest

from Utils.csvReader import get_data
from Pages.login_page import LoginPage
from TestCases.initializer import driver_init, take_screenshot
from TestData.config_data import env, admin_user

from ddt import ddt, data, unpack

@ddt
class LoginPageTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init(env["browser"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.delete_all_cookies()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.load()

    def tearDown(self):
        take_screenshot(self.driver, self.shortDescription())

    def test_login_pass(self):
        """TestLoginPass"""
        dashboard_page = self.loginpage.login(admin_user["username"], admin_user["password"])
        self.assertIn(dashboard_page.url, dashboard_page.get_url())

    @data(*get_data(os.getcwd()+"\\..\\TestData\\login_fail_data.csv"))
    @unpack
    def test_login_fail(self, username, password, expected_err_msg):
        """TestLoginFail"""
        loginpage = self.loginpage.login(username, password, "fail")
        self.assertEqual(expected_err_msg, loginpage.get_err_msg())


if __name__ == '__main__':
    unittest.main()


# ddt
# install ddt
# import methods ddt data unpack from ddt
    # from ddt import ddt, data, unpack
#add @ddt above the test class
#add @data above the test_ method
    # @data(*values) - use get_data(filename) to read data and get data
#add @unpack after @data
    #unpack will unpack the data from each set and give to the parameters in test_