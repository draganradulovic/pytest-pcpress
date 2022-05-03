from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging



#Class Selenium_actions contains methods with simple selenium actions, which can be used on every page.
class Selenium_actions():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver=driver

    def byMethod(self, by):
        by=by.lower()
        try:
            if by=='xpath':
                return By.XPATH
            if by=='id':
                return By.ID
            if by=='name':
                return By.NAME
            if by=='name':
                return By.CLASS_NAME
        except:
            self.log.error("Wrong By method enthered")

    def get_element(self,element, by='xpath'):
        el=self.driver.find_element(self.byMethod(by), element)
        return el

    def click(self, element, by='xpath'):
        self.get_element(element, by).click()

    def send_key(self,key, element, by='xpath'):
        el=self.get_element(element, by)
        el.clear()
        el.send_keys(key)

    def scroll_by_ele(self, element, by='xpath'):
        el=self.get_element(element, by)
        ActionChains(self.driver).move_to_element(el).perform()
        self.driver.execute_script("window.scrollBy(0, -50);")

    def dropdown_select(self,item, element, by='xpath'):
        el=self.get_element(element, by)
        select = Select(el)
        select.deselect_all()
        select.select_by_visible_text(item)












