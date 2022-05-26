from selenium import webdriver
from selenium.webdriver.support.select import Select
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

    def scroll_by_ele(self, element, by='xpath'):
        try:
            element=self.get_element(element, by)
            location = element.location_once_scrolled_into_view
            self.log.info("Scrolled to" + str(location))
            self.driver.execute_script("window.scrollBy(0, -160);")
        except:
            self.log.error("scroll_by_ele method do NOT work")

    def dropdown_select(self, items, element, by='xpath'):
        el = self.get_element(element, by)
        select = Select(el)
        select.deselect_all()
        if type(items) is list:
            for item in items:
                select.select_by_visible_text(item)
        else:
            select.select_by_visible_text(items)



    def element_present(self, element):
        try:
            element = self.get_element(element)
            if element is not None:
                return True
        except:
            return False