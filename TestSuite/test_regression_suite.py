import unittest
import HtmlTestRunner
import os

from TestCases import test_loginpage, test_menubar

class RegressionTestSuite(unittest.TestCase):

    def test_regression(self):
        testsuite = unittest.TestSuite()

        testsuite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_loginpage.LoginPageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_menubar.TestMenuBar),
        ])

        file_path = os.getcwd()+"\\..\\Targets\\Reports\\consolidated_report.html"

        with open(file_path, "w") as output_file:
            runner = HtmlTestRunner.HTMLTestRunner(
                stream = output_file,
                output = "../Targets/Reports/",
                report_title = "Regression Suite",
                report_name = "Login and MenuBar Test"
            )

            runner.run(testsuite)


if __name__ == "__main__":
    unittest.main(verbosity=2)