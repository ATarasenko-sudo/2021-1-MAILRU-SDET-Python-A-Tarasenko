from pages.start_page import StartPage
from locators.pages_locators import CampaignPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CampaignPage(StartPage):


    locators = CampaignPageLocators()
   

    def choose_campaign_object(self):
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        self.click(self.locators.TRAFFIC_LOCATOR)
        self.input(self.locators.ENTER_URL_LOCATOR,'https://target.my.com/')
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.ENTER_URL_LOCATOR))


    def choose_age(self,age1,age2):
        self.click(self.locators.OPEN_SLIDER_LOCATOR)
        self.click(self.locators.SELECT_AGE_LOCATOR)
        self.click(self.locators.SELECT_CUSTOM_AGE_LOCATOR)
        self.clear(self.locators.INPUT_AGE_LOCATOR)
        self.input(self.locators.INPUT_AGE_LOCATOR, "{}-{}".format(age1,age2))

    def add_location(self, country):
        self.click(self.locators.OPEN_LOCATION_LOCATOR)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.INPUT_REGION_LOCATOR))
        self.input(self.locators.INPUT_REGION_LOCATOR, country)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.ADD_REGION_LOCATOR))
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
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.CREATE_GROUP_LOCATOR))
        self.click(self.locators.CREATE_GROUP_LOCATOR)
       


    def create_campaign(self, campaign_name, first_age, last_age, location, context_category, context, payment_type = 'click'):

        self.set_campaign_name(campaign_name)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.CAMPAIGN_NAME_LOCATOR))
        
        self.choose_age(first_age,last_age)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.OPEN_SLIDER_LOCATOR))
        
        self.add_location(location)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.OPEN_LOCATION_LOCATOR))
        
        self.context_config(category = context_category,context = context)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.OPEN_CURRENT_OPTIONS_LOCATOR))
        
        
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.PAYMENT_LOCATOR))
        self.change_payment_type(payment_type)
        


       
    def upload(self, file_path):
        self.click(self.locators.ADS_FORMAT_LOCATOR)
        self.driver.implicitly_wait(3)


        input_field = self.find(self.locators.BIG_IMG_LOCATOR)
        element = input_field.find_element(*self.locators.UPLOAD_LOCATOR)
        element.send_keys(file_path)

        small_img = self.input(self.locators.SMALL_IMG_LOCATOR,file_path) 
        self.click(self.locators.CROPP_SUBMIT_LOCATOR)

    def ad_info(self, ad_title, ad_text):
        self.input(self.locators.AD_TITLE_LOCATOR, ad_title)
        self.input(self.locators.AD_TEXT_LOCATOR, ad_text)

    def set_campaign_name(self, name):
        self.clear(self.locators.CAMPAIGN_NAME_LOCATOR)
        self.input(self.locators.CAMPAIGN_NAME_LOCATOR, name)

    def create_ad(self,file_path, ad_title,ad_text):
        self.upload(file_path)
        self.driver.implicitly_wait(3)

        self.ad_info(ad_title = ad_title, ad_text = ad_text)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.AD_TITLE_LOCATOR))
        
        self.click(self.locators. SAVE_AD_LOCATOR)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.locators.SAVE_AD_LOCATOR))

        self.click(self.locators.CREATE_NEW_CAMPAIGN_LOCATOR)
        self.driver.implicitly_wait(3)
