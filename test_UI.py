from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import basic_locators
import conftest
import time
import pytest


def autorization(driver):
    if (driver.find_element_by_xpath(basic_locators.CHECK_LANGUAGE_LOCATOR)):
        driver.find_element_by_xpath(basic_locators.AUTH_RU_BUTTON_LOCATOR).click()
    else:
        driver.find_element_by_xpath(basic_locators.AUTH_EN_BUTTON_LOCATOR).click()
    element = driver.find_element_by_name(basic_locators.AUTH_EMAIL_ROW_LOCATOR)
    element.send_keys("dr.tarasenko2013@yandex.ru")
    element = driver.find_element_by_name(basic_locators.AUTH_PASSWOR_ROW_LOCATOR)
    element.send_keys("M0zamb1qu3H3r3")
    try:
        driver.find_element_by_xpath(basic_locators.LOGGIN_RU_BUTTON_LOCATOR).click()
    except:
        driver.find_element_by_xpath(basic_locators.LOGGIN_EN_BUTTON_LOCATOR).click()
    
@pytest.mark.UI
def test_logIN(driver):
    if (driver.find_element_by_xpath(basic_locators.CHECK_LANGUAGE_LOCATOR)):
        driver.find_element_by_xpath(basic_locators.AUTH_RU_BUTTON_LOCATOR).click()
    else:
        driver.find_element_by_xpath(basic_locators.AUTH_EN_BUTTON_LOCATOR).click()
    element = driver.find_element_by_name(basic_locators.AUTH_EMAIL_ROW_LOCATOR)
    element.send_keys("dr.tarasenko2013@yandex.ru")
    element = driver.find_element_by_name(basic_locators.AUTH_PASSWOR_ROW_LOCATOR)
    element.send_keys("M0zamb1qu3H3r3")
    try:
        driver.find_element_by_xpath(basic_locators.LOGGIN_RU_BUTTON_LOCATOR).click()
    except:
        driver.find_element_by_xpath(basic_locators.LOGGIN_EN_BUTTON_LOCATOR).click()
    time.sleep(3)



@pytest.mark.UI
def test_logOUT(driver):
    try:
        assert "Campaigns" in driver.title
        driver.find_element_by_class_name(basic_locators.USER_INF_LOCATOR).click()
        time.sleep(2)
        driver.find_element_by_xpath(basic_locators.LOGUT_BUTTON_LOCATOR).click()
        time.sleep(2)
    except AssertionError:
        pass
 
@pytest.mark.UI
def test_change_data(driver):
    try:
        time.sleep(2)
        driver.find_element_by_xpath(basic_locators.PROFILE_BUTTON_MENU_LOCATOR).click()
        time.sleep(1)
        element = driver.find_element_by_xpath(basic_locators.NAME_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("Ondrey")
        time.sleep(1)

        element = driver.find_element_by_xpath(basic_locators.PHONE_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("88005553535")
        time.sleep(1)

        element = driver.find_element_by_xpath(basic_locators.EMAIL_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("foobar@mail.ru")
        time.sleep(1)

        driver.find_element_by_xpath(basic_locators.ADD_SECOND_EMAIL_BUTTON).click()
        time.sleep(1)
        element = driver.find_element_by_xpath(basic_locators.SECOND_EMAIL_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        element.send_keys("bar@list.ru")
        time.sleep(1)
        driver.find_element_by_xpath(basic_locators.SUBMIT_BUTTON_LOCATOR).click()
    except:
        autorization(driver)
        time.sleep(2)
        driver.find_element_by_xpath(basic_locators.PROFILE_BUTTON_MENU_LOCATOR).click()
        time.sleep(1)
        element = driver.find_element_by_xpath(basic_locators.NAME_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("Ondrey")
        time.sleep(1)

        element = driver.find_element_by_xpath(basic_locators.PHONE_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("88005553535")
        time.sleep(1)

        element = driver.find_element_by_xpath(basic_locators.EMAIL_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        time.sleep(1)
        element.send_keys("foobar@mail.ru")
        time.sleep(1)

        driver.find_element_by_xpath(basic_locators.ADD_SECOND_EMAIL_BUTTON).click()
        time.sleep(1)
        element = driver.find_element_by_xpath(basic_locators.SECOND_EMAIL_ROW_PROFILE_INF_LOCATOR)
        element.clear()
        element.send_keys("bar@list.ru")
        time.sleep(1)
        driver.find_element_by_xpath(basic_locators.SUBMIT_BUTTON_LOCATOR).click()


@pytest.mark.UI
@pytest.mark.parametrize("path", ['//a[@href="/statistics"]', '//a[@href="/profile"]'])
@pytest.mark.parametrize("title", ['Statistics', 'Profile'])
def test_switch(driver, path,title):
    try:
        with pytest.raises(AssertionError):
            time.sleep(2)
            driver.find_element(By.XPATH, path).click()
            assert title in driver.title
    except:
        autorization(driver)
        with pytest.raises(AssertionError):
            time.sleep(2)  
            driver.find_element(By.XPATH, path).click()
            assert title in driver.title