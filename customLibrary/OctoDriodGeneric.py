from os.path import join
from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By

from customLibrary.AppiumSessionHolder import AppiumSessionHolder
from customLibrary.AppiumActions import AppiumActions
from variables.config_variables import  *
from variables.locators import  *

class OctoDriodGeneric(AppiumActions):

    def __init__(self):
        super().__init__()
        pass

    def open_application(self , full_reset=False ,no_reset=no_reset):
        app_path = Path(__file__).parent.parent
        app_path = join(str(app_path), 'app', 'app.apk')
        caps = {
            'platformName': device_platform, 'fullReset':full_reset , 'deviceName': device_name, 'automationName': 'UiAutomator2',
            'skipServerInstallation': False, 'appActivity': app_acctivity, 'noReset': no_reset,
            'udid': udid, 'newCommandTimeout': 1200, 'autoGrantPermissions': True,
            'appPackage': app_package,'disableWindowAnimation': True , 'app':app_path
        }
        AppiumSessionHolder.open_application(host_url=appium_host , desired_caps= caps)
    
    def click_on_login_with_token(self):
        self.find(locate_st=By.ID , locator=token_check_box_for_login).click()
        self.find(locate_st=By.ID , locator=token_edit_box)


    def login_to_github(self , token = accses_token):
        self.find(locate_st=By.XPATH , locator=go_to_login_menu_button).click()
        self.click_on_login_with_token()
        self.find(locate_st=By.ID , locator=token_edit_box).send_keys(token)
        self.find(locate_st=By.XPATH , locator=login_btn).click()

    def is_in_main_page(self):
        try:
            self.find(locate_st=By.XPATH , locator=main_page_title_xpath)
            return True
        except:
            return False

    def click_device_back_btn(self):
        driver = self.get_instance()
        driver.press_keycode(4)

    def close_application(self):
        AppiumSessionHolder.close_application()

    def is_in_unauthrized_page(self):
        try:
            self.find(locate_st=By.XPATH , locator=go_to_login_menu_button)
            return True
        except:
            return False

    def check_user_is_loged_in(self):
        try :
            self.find(locate_st=By.XPATH , locator=go_to_login_menu_button)
            self.login_to_github()
            sleep(10)
        except:
            pass