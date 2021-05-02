from pages.start_page import StartPage
from locators.pages_locators import FailAutorizationPageLocators



class FailAutorizationPage(StartPage):

    locators = FailAutorizationPageLocators()

    def fail_message_location(self):
        return self.find(self.locators.WRONG_LOG_PASS_LOCATOR).text
