import pytest
from selenium import webdriver
import time


@pytest.fixture(scope='session', autouse=True)
def driver():
    browser = webdriver.Chrome(executable_path='/home/ondrey/Desktop/autotest/HW1/chromedriver')
    browser.get("https://target.my.com/")
    browser.maximize_window()
    time.sleep(2)
    yield browser
    browser.close()
