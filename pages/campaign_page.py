from pages.start_page import StartPage
from locators.pages_locators import CampaignPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class CampaignPage(StartPage):


    locators = CampaignPageLocators()
    #url = 'https://play.google.com/store/apps/details?id=com.supercell.brawlstars&hl=ru&gl=US'

    def choose_campaign_object(self):
        #self.autorization("dr.tarasenko2013@yandex.ru","M0zamb1qu3H3r3")
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        self.click(self.locators.TRAFFIC_LOCATOR)
        self.input(self.locators.ENTER_URL_LOCATOR,'https://target.my.com/')
        time.sleep(3)


    def choose_age(self,age1,age2):
        self.click(self.locators.OPEN_SLIDER_LOCATOR)
        self.click(self.locators.SELECT_AGE_LOCATOR)
        self.click(self.locators.SELECT_CUSTOM_AGE_LOCATOR)
        self.clear(self.locators.INPUT_AGE_LOCATOR)
        self.input(self.locators.INPUT_AGE_LOCATOR, "{}-{}".format(age1,age2))

    def add_location(self, country):
        self.click(self.locators.OPEN_LOCATION_LOCATOR)
        time.sleep(1)
        self.input(self.locators.INPUT_REGION_LOCATOR, country)
        time.sleep(1)
        self.click(self.locators.ADD_REGION_LOCATOR)

    def change_payment_type(self, payment):
        self.click(self.locators.PAYMENT_LOCATOR)
        if payment == "click":
            self.click(self.locators.CLICK_LOCATOR)
        else:
            self.click(self.locators.IMP_LOCATOR)

    def set_budget(self, daily, total):

        self.input(self.locators.DAILY_BUDGET_LOCATOR, daily)
        self.input(self.locators.TOTAL_BUDGET_LOCATOR, total)


    def context_config(self, category, context):
        self.click(self.locators.OPEN_CURRENT_OPTIONS_LOCATOR)
        self.input(self.locators.ENTER_CATEGORY_LOCATOR,category)
        self.input(self.locators.TEXT_CONTEXT_LOCATOR, context)
        self.click(self.locators.CREATE_CONTEXT_LOCATOR)


    def group_config(self, group):
        self.click(self.locators.GROUP_CONFIG_LOCATOR)
        self.input(self.locators.ENTER_GROUP_LOCATOR, group)
        self.click(self.locators.SELECT_GROUP_LOCATOR)
        self.click(self.locators.CREATE_GRIUP_LOCATOR)
       




      
    
       
    def upload(self, file_path):
        self.click(self.locators.ADS_FORMAT_LOCATOR)
        time.sleep(2)


        input_field = self.find(self.locators.BIG_IMG_LOCATOR)
        element = input_field.find_element(*self.locators.UPLOAD_LOCATOR)
        element.send_keys(file_path)

        small_img = self.input(self.locators.SMALL_IMG_LOCATOR,file_path) # '/home/ondrey/Desktop/autotest/HW2.1/img/87497-1.jpg'

        self.click(self.locators.CROPP_SUBMIT_LOCATOR)

    def ad_info(self, ad_title, ad_text):
        self.input(self.locators.AD_TITLE_LOCATOR, ad_title)
        self.input(self.locators.AD_TEXT_LOCATOR, ad_text)

    def set_campaign_name(self, name):
        self.clear(self.locators.CAMPAIGN_NAME_LOCATOR)
        self.input(self.locators.CAMPAIGN_NAME_LOCATOR, name)

