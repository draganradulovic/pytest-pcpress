from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import Selenium_actions
import time

"""
Class Base_page contains methods which can be used on every page on test site. Base_page is child class of Selenium_actions class 
and uses methods defined in Selenium_actions parent class. In this specific project, only few methods are present in Base_page class
as example. In bigger projects, this class can be really useful.
"""

class Base_page(Selenium_actions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def validateTitle(self, title):
        page_title=self.driver.title
        assert title == page_title

    def sleep(self, seconds=5):
        time.sleep(seconds)


    def element_present(self, element):
        try:
            element = self.get_element(element)
            if element is not None:
                return True
        except:
            time.sleep(5)
            print('jbg')
            return False