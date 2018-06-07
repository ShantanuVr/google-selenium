#!/usr/bin/env python
'''
Description:
Created on 07/06/18

'''
__author__ = 'Shantanu Vichare'
__copyright__ = ""
__credits__ = []

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from base_page import BasePage

import time

class HomePageLocators(object):
    SEARCH_BAR = (By.XPATH, "//*[@id='lst-ib']")
    SEARCH_BUTTON = (By.XPATH, "//*[@name='btnK']")

class HomePage(BasePage):
    """Home page action methods come here. I.e. Google.com"""

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        WebDriverWait(driver, 150).until(
            lambda driver: driver.find_element(*HomePageLocators.SEARCH_BAR))
        time.sleep(5)

    def do_search_text(self, SEARCH_QUERY):
        search_bar = self.driver.find_element(*HomePageLocators.SEARCH_BAR)
        search_bar.send_keys(SEARCH_QUERY)

        search_button = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        search_button.click()

        return self.driver