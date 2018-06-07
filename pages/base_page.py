#!/usr/bin/env python
'''
Description:
Created on 17/05/18

'''
__author__ = 'Shantanu Vichare'
__copyright__ = ""
__credits__ = []

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver