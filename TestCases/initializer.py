import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def driver_init(browser = "Chrome"):
    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.maximize_window()

    return driver

def take_screenshot(driver, test_name):
    filename = f"{time.strftime('%Y_%m_%d-%H_%M_%S')}_{test_name}.png"
    filepath = os.getcwd()+f"/../Targets/Screenshots/{filename}"
    driver.get_screenshot_as_file(filepath)