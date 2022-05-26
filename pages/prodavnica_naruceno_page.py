from selenium import webdriver
from base.base_page import Base_page
from base.selenium_driver import Selenium_actions
import utilities.custom_logger as cl
import logging


class Prodavnica_naruceno_page(Base_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    _confirmation_message = "//*[@id='doubleprovera']/div/table[1]/tbody/tr[1]/td[2]"

    def is_ordered_successfuly(self):
        try:
            result=self.get_element(self._confirmation_message).is_displayed()
            self.log.info("Magazine successfully ordered")
            return result
        except:
            self.log.error("Magazine oredring FAILED")
            return False

    def ime_i_prezime_error_present(self):
        try:
            result=self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Ime i prezime')]").is_displayed()
            return result
        except:
            return False

    def ulica_i_broj_error_present(self):
        try:
            result = self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Ulicu i Broj')]").is_displayed()
            return result
        except:
            return False

    def phone_error_present(self):
        try:
            result = self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Telefon')]").is_displayed()
            return result
        except:
            return False

    def email_error_present(self):
        try:
            result = self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Email')]").is_displayed()
            return result
        except:
            return False

    def postanski_broj_error_present(self):
        try:
            result = self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Poštanski broj')]").is_displayed()
            return result
        except:
            return False

    def grad_error_present(self):
        try:
            result = self.get_element("//*[@id='doubleprovera']//b[contains(text(),'Grad')]").is_displayed()
            return result
        except:
            return False


    def all_errors_present(self):
        try:
            if self.email_error_present() and self.phone_error_present():
                if self.ulica_i_broj_error_present() and self.ime_i_prezime_error_present():
                    if self.grad_error_present() and self.postanski_broj_error_present():
                        self.log.info("All errors present")
                        return True
        except:
            self.log.error("Error missing")
            return False