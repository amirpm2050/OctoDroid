from selenium.webdriver.common.by import By

from customLibrary.AppiumActions import AppiumActions
from variables.locators import  *


class SideMenu(AppiumActions):

    def __init__(self):
        super().__init__()
        pass

    def open_side_menu(self):
        header_list = self.finds(locate_st=By.XPATH , locator="//*[@resource-id='com.gh4a:id/toolbar']/*")
        header_list[0].click()

    def open_profile_tab(self):
        self.find(locate_st=By.ID , locator= profile_in_side_menu_btn).click()

    def click_logout_user(self):
        self.find(locate_st=By.XPATH , locator= side_menu_logout_btn).click()

    def logout_user(self):
        self.open_side_menu()
        self.open_profile_tab()
        self.click_logout_user()

    def open_search_menu(self):
        self.open_side_menu()
        self.find(locate_st=By.XPATH , locator=search_in_side_menu).click()
