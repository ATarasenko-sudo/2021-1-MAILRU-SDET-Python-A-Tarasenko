from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.pages_locators import StartPageLocators

import time
import pytest

CLICK_RETRY = 3
BASE_TIMEOUT = 5


class StartPage(object):

    locators = StartPageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def input(self, locator, input_inf):
        input_raw = self.find(locator, timeout=None)
        input_raw.send_keys(input_inf)

    def clear(self, locator, timeout = None):
        element = self.find(locator, timeout=timeout)
        element.clear()

    def autorization(self, email, password):
        self.click(self.locators.AUTH_RU_BUTTON_LOCATOR)
        self.input(self.locators.AUTH_EMAIL_ROW_LOCATOR, email)
        self.input(self.locators.AUTH_PASSWOR_ROW_LOCATOR, password)
        self.click(self.locators.LOGGIN_RU_BUTTON_LOCATOR)
        self.driver.implicitly_wait(3)
