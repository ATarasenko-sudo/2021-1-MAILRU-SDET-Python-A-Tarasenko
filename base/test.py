import pytest
import time
import os

from base import BaseCase

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains



class TestOne(BaseCase):
    @pytest.fixture(scope='function')
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'img', '87497-1.jpg')

   
    @pytest.fixture(scope = 'function')
    def logIn(self, log = 'dr.tarasenko2013@yandex.ru', pas = 'M0zamb1qu3H3r3'):
        try: 
            assert "Рекламная платформа myTarget — Сервис таргетированной рекламы" not in self.driver.title
        except AssertionError:
            self.start_page.click(self.start_page.locators.CHECK_LANGUAGE_LOCATOR)
            time.sleep(2)
            self.start_page.click(self.start_page.locators.AUTH_EN_BUTTON_LOCATOR)
            self.start_page.input(self.start_page.locators.AUTH_EMAIL_ROW_LOCATOR, log)
            self.start_page.input(self.start_page.locators.AUTH_PASSWOR_ROW_LOCATOR, pas)
            self.start_page.click(self.start_page.locators.LOGGIN_EN_BUTTON_LOCATOR)
            time.sleep(2)
        yield

    @pytest.mark.UI
    #@pytest.mark.skip()
    @pytest.mark.parametrize("email", [('111'), ('dr.tarasenko2013@yandex.ru')])
    @pytest.mark.parametrize("paswrd", [('bar')])
    def test_autorization(self, email, paswrd):
        time.sleep(5)
        self.start_page.autorization(email = email, password= paswrd)
        assert self.failed_autorization_page.fail_message_location() == "Invalid login or password"
    
    @pytest.mark.UI
    #@pytest.mark.skip()
    def test_campaign_config(self, logIn,file_path):
        self.campaign_page.choose_campaign_object()

        time.sleep(10)

        self.campaign_page.set_campaign_name(name = "target")
        time.sleep(2)
        self.campaign_page.choose_age(13,23)
        time.sleep(3)
        self.campaign_page.add_location("Ukraine")
        time.sleep(2)

        self.campaign_page.context_config(category = "ads",context = "таргет,маркетинг,реклама")
        time.sleep(2)
        self.campaign_page.group_config(group="таргетированная реклама")
        time.sleep(2)
        self.campaign_page.change_payment_type("Impressions")
        time.sleep(2)
        self.campaign_page.set_budget(daily = "200", total = '10000')
        time.sleep(2)
        self.campaign_page.upload(file_path)
        time.sleep(2)
        self.campaign_page.ad_info(ad_title = "foo", ad_text = "bar")
        time.sleep(2)
        self.campaign_page.click(self.campaign_page.locators. SAVE_AD_LOCATOR)
        self.campaign_page.click(self.campaign_page.locators.CREATE_NEW_CAMPAIGN_LOCATOR)
        time.sleep(10)
        assert  self.start_page.find(self.campaign_page.locators.CHECK_CAMPAIGN_LOCATOR).text == "target"
    
    @pytest.mark.UI
    #@pytest.mark.skip()
    def test_segment_config(self, logIn):
        self.segment_config_page.go_to_segments()

        try:
            self.segment_config_page.find(self.segment_config_page.locators.CHECK_EXIST_SEGMENTS)
            self.segment_config_page.click(self.segment_config_page.locators.CREATE_NEW_SEGMENT)
        except:
            self.segment_config_page.click(self.segment_config_page.locators.CREATE_NEW_SEGMENT_ALT_LOCATOR)
        finally:
            self.segment_config_page.switch_to_apps()
            self.segment_config_page.search_object("Mytarget")
            self.segment_config_page.add_object()

            self.segment_config_page.switch_to_groups()

            self.segment_config_page.search_object("TargetHunter")
            self.segment_config_page.add_object()
            time.sleep(3)
            self.segment_config_page.click(self.segment_config_page.locators.ADD_SEGMENT_BUTTON_LOCATOR)
            time.sleep(2)
            self.segment_config_page.name_of_segment(name = "app and targetHunter segment")
            self.segment_config_page.submit_segment()
            time.sleep(2)
            assert self.segment_config_page.check_segment_by_name() == "app and targetHunter segment"

    @pytest.mark.UI
    #@pytest.mark.skip()
    def test_delete_campaign(self, logIn):
        try:
            if self.start_page.find(self.campaign_page.locators.CHECK_CAMPAIGN_LOCATOR).text == "target":
                self.campaign_menu_page.delete_campaign()
                time.sleep(3)
        except TimeoutException:
            pass

   

    @pytest.mark.UI
    #@pytest.mark.skip()
    def test_delete_segment(self, logIn):
        self.segment_config_page.go_to_segments()
        try:
            assert self.segment_config_page.find(self.segment_config_page.locators.CHECK_EXIST_SEGMENTS).text == "How to get started?"
        except AssertionError:
            pass

        finally:
            try:
                id_segment_check = self.segment_config_page.id_segment()
                self.segment_config_page.delete_segment()
                time.sleep(2)
                assert id_segment_check != self.segment_config_page.id_segment()
            except: 
                try:
                    assert self.segment_config_page.find(self.segment_config_page.locators.CHECK_EXIST_SEGMENTS).text == "How to get started?"
                except:
                    assert self.segment_config_page.find(self.segment_config_page.locators.CHECK_EXIST_SEGMENTS).text == ''                    


     


    