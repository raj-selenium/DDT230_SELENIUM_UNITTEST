import os
import unittest

from ddt import ddt, data, unpack

from Pages.login_page import LoginPage
from TestCases.initializer import driver_init, take_screenshot
from TestData.config_data import env, admin_user
from Utils.csvReader import get_data


@ddt
class TestMenuBar(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init(env["browser"])
        login_page = LoginPage(cls.driver)
        login_page.load()
        cls.dashboard_page = login_page. \
            login(admin_user["username"], admin_user["password"])

    def setUp(self):
        pass

    def tearDown(self):
        take_screenshot(self.driver, self.shortDescription())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @unittest.skipIf(env["browser"] == "Firefox", "Element Click not working in FF")
    def test_3_logout(self):
        """test_logout"""
        actual_url = self.dashboard_page.logout()
        self.assertIn("login", actual_url)

    def test_1_welcome_msg(self):
        """test_welcome_msg"""
        wel_msg = self.dashboard_page.get_welcome_msg()
        self.assertIn("Welcome ", wel_msg)


    @data(*get_data(os.getcwd()+"\..\TestData\menu_navigation_tc.csv"))
    @unpack
    def test_2_menu_navigation(self, menus, expected_url):
        """Menu_Navigation_Test"""
        actual_url = self.dashboard_page.navigate_to_menu_by_dynamic_loc(menus)
        self.assertIn(expected_url, actual_url)


if __name__ == "__main__":
    unittest.main(verbosity = 2)