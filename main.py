#!/usr/bin/env python
'''
Description:
Created on 07/06/18

'''
__author__ = 'Shantanu Vichare'
__copyright__ = ""
__credits__ = []

from selenium import webdriver
from pages import home_page, search_page

class Google:
    ''' Main Class for referencing all methods. '''

    def __init__(self):
        # The below code is used so we can start browser in maximized window.
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.maximize_window()

    def test_google_search(self, SITE_URL, SEARCH_QUERY):
        self.driver.get(SITE_URL)

        home_page_obj = home_page.HomePage(self.driver)
        home_page_obj.do_search_text(SEARCH_QUERY)

        search_page_obj = search_page.SearchPage(self.driver)
        search_page_obj.get_search_links()

    def close_driver(self):
        self.driver.close()

if __name__ == "__main__":
    SITE_URL = "https://www.google.com"
    SEARCH_QUERY = "How to learn Python and Selenium"
    main_class_obj = Google()
    main_class_obj.test_google_search(SITE_URL, SEARCH_QUERY)
    main_class_obj.close_driver()