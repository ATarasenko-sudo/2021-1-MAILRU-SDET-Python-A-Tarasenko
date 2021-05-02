from pages.start_page import StartPage
from locators.pages_locators import SegmentConfigPageLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SegmentConfigPage(StartPage):

    locators = SegmentConfigPageLocators()

    def go_to_segments(self):
        self.click(self.locators.GO_TO_SEGMENTS_LOCATOR)

    def search_object(self, obj):
        self.input(self.locators.SEARCH_SEGMENT_LOCATOR, obj)

    def add_object(self):
        self.click(self.locators.CHECKBOX_SEGMENT_LOCATOR)

    def switch_to_apps(self):
        self.click(self.locators.APPS_AND_GAMES_LOCATOR)
    
    def switch_to_groups(self):
        self.click(self.locators.GROUPS_SEGMENT_LOCATOR)

    def name_of_segment(self,name):
        self.clear(self.locators.SEGMENT_NAME_FIELD_LOCATOR)
        self.input(self.locators.SEGMENT_NAME_FIELD_LOCATOR, name)

    def submit_segment(self):
        self.click(self.locators.SUBMIT_SEGMENT_LOCATOR)
    
    def check_segment_by_name(self):
        return self.find(self.locators.CHECK_SEGMENT_LOCATOR).text

    def id_segment(self):
        return self.find(self.locators.SAVE_ID_LOCATOR).text

    def delete_segment(self):
        self.click(self.locators.CHECKBOX_SEGMENT_MENU_LOCATOR)
        self.click(self.locators.ACTIONS_BUTTON_LOCATOR)
        self.click(self.locators.REMOVE_BUTTON_LOCATOR)


    def create_segment(self, apps, groups):

        self.switch_to_apps()
        self.search_object(apps)
        self.add_object()

        self.switch_to_groups()

        self.search_object(groups)
        self.add_object()
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.ADD_SEGMENT_BUTTON_LOCATOR))
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR)
        
        