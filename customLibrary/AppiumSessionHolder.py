from appium import webdriver
from appium.webdriver.webdriver import WebDriver

class AppiumSessionHolder():

    __driver = None

    def __init__(self):
        pass

    @staticmethod
    def open_application(host_url, desired_caps: dict) -> WebDriver:
        AppiumSessionHolder.__driver = webdriver.Remote(str(host_url), desired_caps)
        return AppiumSessionHolder.__driver

    @staticmethod
    def get_session_instance()-> WebDriver:
        if not AppiumSessionHolder.__driver:
            raise Exception("no App opened")
        return AppiumSessionHolder.__driver

    @staticmethod
    def close_application():
        AppiumSessionHolder.__driver.quit()




