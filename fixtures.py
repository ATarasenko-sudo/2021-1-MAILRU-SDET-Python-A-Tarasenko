import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.start_page import StartPage
from pages.failed_autorization_page import FailAutorizationPage
from pages.campaign_page import CampaignPage
from pages.campaign_menu_page import CampaignMenuPage
from pages.segment_config_page import SegmentConfigPage

from locators.pages_locators import StartPageLocators
from selenium.webdriver.common.by import By



@pytest.fixture
def start_page(driver):
    return StartPage(driver=driver)

@pytest.fixture
def failed_autorization_page(driver):
    return FailAutorizationPage(driver= driver)

@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)

@pytest.fixture
def campaign_menu_page(driver):
    return CampaignMenuPage(driver=driver)

@pytest.fixture
def segment_config_page(driver):
    return SegmentConfigPage(driver=driver)

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()
