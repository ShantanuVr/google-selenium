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

class SearchPageLocators(object):
    SEARCH_FOOTER = (By.XPATH, "//*[@id='foot']")
    SEARCH_LINKS = (By.XPATH, "//div[@class='g']/div/div/h3/a")

class SearchPage(BasePage):
    """Search page action methods come here. I.e. Google.com"""

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        WebDriverWait(driver, 150).until(
            lambda driver: driver.find_element(*SearchPageLocators.SEARCH_FOOTER))
        time.sleep(5)

    def get_search_links(self):
        for search_link in self.driver.find_elements(*SearchPageLocators.SEARCH_LINKS):
            print search_link.get_attribute("href")

        return self.driver
