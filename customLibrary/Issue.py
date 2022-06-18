from os.path import join
from pathlib import Path
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from customLibrary.AppiumSessionHolder import AppiumSessionHolder
from customLibrary.AppiumActions import AppiumActions
from variables.config_variables import  *
from variables.locators import  *


class Issue(AppiumActions):

    def __init__(self):
        super().__init__()
        pass

    def click_on_issue_in_project(self):
        self.find(locate_st=By.ID  , locator=issues_row_in_project).click()

    def scroll_to_find_issue(self , issue_name = 'This project seems to be outdated' , scroll_count=20):
            issues_name = self.finds(locate_st=By.ID , locator=issue_labales_locator)
            for name in issues_name :
                if name.text.lower() == issue_name.lower():
                    name.click()
                    return

            scroll_count -= 1
            if scroll_count != 0 :
                actions = TouchAction(self.get_instance())
                actions.press(issues_name[len(issues_name)-1])
                actions.wait(100)
                actions.move_to(issues_name[len(issues_name)-4])
                actions.release().perform()
                self.scroll_to_find_issue(issue_name=issue_name , scroll_count=scroll_count)

    def add_comment_to_issue(self , comment = 'this comment is for test ' ):
        self.find(locate_st=By.ID , locator= comment_on_issue_edit_text ).send_keys(comment)
        self.find(locate_st=By.ID , locator= send_comment_btn)
        sleep(3)

    def check_comment_added(self , comment=''):
        sleep(3)
        texts = self.finds(locate_st=By.ID , locator= comment_text_id)
        for text in texts:
            if text.text.lower() == comment.lower():
                return True
        return False

    def open_new_issue_page(self):
        self.find(locate_st=By.ID , locator=add_issue_btn).click()

    def add_issue_from_search(self , title , desc):
        self.find(locate_st=By.ID , locator=new_issue_titile).send_keys(title)
        self.find(locate_st=By.ID , locator=new_issue_desc).send_keys(desc)
        self.find(locate_st=By.XPATH , locator=add_new_issue_btn).click()
        sleep(10)


    def close_issue(self):
        sleep(3)
        self.find(locate_st=By.ID , locator= edit_issue )
        self.find(locate_st=By.ID , locator= close_issue).click()
        self.find(locate_st=By.XPATH , locator= confirm_close_issue).click()

    def check_issue_is_close(self):
        sleep(3)
        text = self.find(locate_st=By.ID , locator=issue_state).text
        if text.lower() == 'closed':
            return True
        else :
            return False

    def is_issue_added(self):
        sleep(3)
        text = self.find(locate_st=By.ID, locator=issue_state).text
        if text.lower() == 'open':
            return True
        else:
            pass
        return False

