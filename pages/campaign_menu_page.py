from locators.pages_locators import CampaignMenuPageLocators
from pages.start_page import StartPage


class CampaignMenuPage(StartPage):

    locators = CampaignMenuPageLocators()

    def delete_campaign(self):
        self.click(self.locators.FIND_CHECKBOX_LOCATOR)
        self.click(self.locators.FIND_ACTION_MENU_LOCATOR)
        self.click(self.locators.DELETE_BUTTON_LOCATOR)