from customLibrary.AppiumSessionHolder import AppiumSessionHolder


class AppiumActions():

    def __init__(self):
        pass

    def find(self, locate_st , locator , timeout=10):
        try:
            driver = self.get_instance()
            driver.implicitly_wait(timeout)
            element = driver.find_element(by=locate_st ,value=locator)
            return element
        except:
            raise Exception("element is not visible")

    def finds(self, locate_st , locator , timeout=10):
        try:
            driver = self.get_instance()
            driver.implicitly_wait(timeout)
            element = driver.find_elements(by=locate_st ,value=locator)
            return element
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def get_instance():
        return  AppiumSessionHolder.get_session_instance()


