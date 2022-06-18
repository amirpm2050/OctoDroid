from selenium.webdriver.common.by import By

from customLibrary.AppiumActions import AppiumActions
from variables.locators import  *


class Search(AppiumActions):

    def __init__(self):
        super().__init__()
        pass

    def search_project_and_open(self , project_name = 'cafebazaar/AdContainer'):
        self.find(locate_st=By.ID , locator=search_edit_text ).send_keys(project_name)
        self.get_instance().press_keycode(66);
        self.find_and_click_on_project_in_search_list(project_name=project_name)


    def find_and_click_on_project_in_search_list(self , project_name):
        projects = self.finds(locate_st=By.ID , locator='tv_title')
        for project in projects :
            if project.text.lower() == project_name.lower():
                project.click()
            else :
                raise Exception('Project Not Found')