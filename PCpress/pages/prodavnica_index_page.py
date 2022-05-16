from selenium import webdriver
from base.base_page import Base_page
from base.selenium_driver import Selenium_actions
import utilities.custom_logger as cl
import logging
from selenium.webdriver.support.color import Color


"""
Class Prodavnica_page contains locators and methods used specificaly on "Prodavnica" section on "PCpress" site,
for finding elements and manipulating with elements. Class Prodavnica_page is child class of Base_page class.
"""
class Prodavnica_page(Base_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    log = cl.customLogger(logging.DEBUG)

    """
    Method taking name of magazine and defining the beginning of the XPATH to which the suffix(path to specific element)
     will be added, in order to create full XPATH.
    This functionality will be improved, in order to find elements more dynamically.
    """
    def base_locator(self, magazine):
        #magazine = magazine.lower()
        elements = {"aktuelni broj casopisa pc": "//*[@id='artikal5bg']",
                    "godisnja pretplata na casopis pc (11 brojeva)": "//*[@id='artikal1bg']",
                    "polugodisnja pretplata na casopis pc (6 brojeva)": "//*[@id='artikal0bg']",
                    "pretplata na digitalno izdanje casopisa pc - godisnja": "//*[@id='artikal14bg']",
                    "pretplata na digitalno izdanje casopisa pc - polugodisnja": "//*[@id='artikal15bg']",
                    "knjiga 50 godina racunarstva u srbiji": "//*[@id='artikal4bg']",
                    "arhiva brojeva casopisa pc": "//*[@id='artikal6bg']",
                    "arhiva brojeva casopisa connect": "//*[@id='artikal8bg']",
                    "knjiga office i windows na radnom mestu": "//*[@id='artikal9bg']",
                    "ipc 2008+ dl dvd - elektronski indeks casopisa pc": "//*[@id='artikal10bg']",
                    "knjiga pc vodic kroz primene racunara": "//*[@id='artikal12bg']"
        }
        try:
            if magazine in elements:
                base = elements.get(magazine)
                self.log.info("Magazine found")
                return base
        except:
            self.log.error("Entered magazine not on magazines list")

    def checkbox_locator(self, magazine):
        try:
            __checkbox = (self.base_locator(magazine)) + ("//table/tbody/tr[2]/td[2]/input")
            self.log.info("Checkbox element found")
            return __checkbox
        except:
            self.log.error("Checkbox element not found")

    def kolicina_field_locator(self, magazine):
        try:
            __kolicina_field = (self.base_locator(magazine)) + ("//input[contains(@id, 'kolselektor')]")
            self.log.info("'Kolicina' field found")
            return __kolicina_field
        except:
            self.log.error("'Kolicina' field not found")

    def dropdown_menu_locator(self, magazine):
        try:
            __dropdown_menu = (self.base_locator(magazine))+("//select")
            self.log.info("Dropdown menu found")
            return __dropdown_menu
        except:
            self.log.error("Dropdown menu not found")


    def kupujem_button_locator(self, magazine):
        try:
            __kupujem = (self.base_locator(magazine)) + ("//img[contains(@alt, 'Kupujem')]")
            self.log.info("'Kupujem' button found")
            return __kupujem
        except:
            self.log.error("'Kupujem' button not found")


    def ordering_by_field(self, magazin, kolicina):
        try:
            self.scroll_by_ele(self.checkbox_locator(magazin))
            self.click(self.checkbox_locator(magazin))
            self.send_key(kolicina ,self.kolicina_field_locator(magazin))
            self.log.info("Data entered in 'Kolicina' field")
        except:
            self.log.error("Data entering in 'Kolicina' field FAILED")

    def ordering_by_dropdown(self, magazin, drpd_items):
        try:
            self.scroll_by_ele(self.checkbox_locator(magazin))
            self.click(self.checkbox_locator(magazin))
            self.select_from_dropdown(drpd_items, magazin)
            self.log.info("Item selected in 'Izaberite brojeve' dropdown list")
        except:
            self.log.error("Item selection in 'Izaberite brojeve' dropdown list FAILED")

    def select_from_dropdown(self, drpd_item, magazine):
            self.dropdown_select(drpd_item, self.dropdown_menu_locator(magazine))


        # ORDERING FORM LOCATORS:
    _ime_i_prezime_field = "//*[@id='korisnik']/tbody/tr[1]/td[2]/input"
    _ulica_i_broj_field = "//*[@id='korisnik']/tbody/tr[2]/td[2]/textarea"
    _postanski_broj_field = "//*[@id='korisnik']/tbody/tr[3]/td[2]/input[1]"
    _grad_field = "//*[@id='korisnik']/tbody/tr[3]/td[2]/input[2]"
    _telefon_field = "//*[@id='korisnik']/tbody/tr[4]/td[2]/input"
    _email_field = "//*[@id='korisnik']/tbody/tr[5]/td[2]/input"
    _napomena_field = "//*[@id='korisnik']/tbody/tr[6]/td[2]/textarea"
    _narucujem_button = "//*[@id='korisnik']/tbody/tr[7]/td/input[2]"
    _odustajem_button = "//*[@id='korisnik']/tbody/tr[7]/td/input[3]"
    _lower_kupujem_button = "//*[@id='porudzbenica']/div[12]/input[2]"

    _empty_order_error = "//*[@id='proverainside']//p[contains(text(),'Molimo izaberite jedan od ponuđenih artikala klikom na')]"
    _invalid_quantity_error = "//*[@id='proverainside']//p[contains(text(),'Molimo unesite kolicinu u rasponu 0-100')]"
    _invalid_selection_error = "//*[@id='proverainside']//p[contains(text(),'Molimo izaberite samo jedan magazin')]"


    def fill_ordering_form(self, ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena=''):
        try:
            self.send_key(ime_i_prezime, self._ime_i_prezime_field)
            self.send_key(ulica_i_broj, self._ulica_i_broj_field)
            self.send_key(postanski_broj, self._postanski_broj_field)
            self.send_key(grad, self._grad_field)
            self.send_key(telefon, self._telefon_field)
            self.send_key(email,self._email_field)
            self.send_key(napomena, self._napomena_field)
            self.log.info("'Narudzbenica' form filled")
        except:
            self.log.error("'Narudzbenica' form NOT filled")


    def order(self, magasines_list, order_parameters_list, ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena=''):
        magasines_list = magasines_list
        parameters_list = order_parameters_list
        i = 0
        for magasine in magasines_list:
            if 'Broj' in parameters_list[i]:
                self.ordering_by_dropdown(magasine, parameters_list[i])
                i = i + 1
            else:
                self.ordering_by_field(magasine, parameters_list[i])
                i = i + 1
        self.click(self.kupujem_button_locator(magasines_list[i - 1]))
        self.fill_ordering_form(ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena)
        self.click(self._narucujem_button)
        self.sleep(5)

    def empty_order(self):
        try:
            self.click(self._lower_kupujem_button)
            self.sleep(3)
            result=self.get_element(self._empty_order_error).is_displayed()
            self.log.info("Empty order error message displayed")
            return result
        except:
            self.log.error("Empty order error message NOT displayed")
            return False

    def invalid_quantity_order(self,magazine, quantity):
        try:
            self.ordering_by_field(magazine, quantity)
            self.click(self._lower_kupujem_button)
            result =self.get_element(self._invalid_quantity_error).is_displayed()
            self.log.info("Ivalid quantity error message displayed")
            return result
        except:
            self.log.error("Invalid quantity error NOT displayed")
            return False

    def invalid_selection_order(self,magazine,items):
        try:
            self.ordering_by_dropdown(magazine,items)
            self.click(self._lower_kupujem_button)
            result = self.get_element(self._invalid_selection_error).is_displayed()
            self.log.info("Ivalid dropdown selection error message displayed")
            return result
        except:
            self.log.error("Invalid dropdown error NOT displayed")
            return False


    def verify_zip_city_sync(self, magazines, quantity, name, address, zip, city, phone, email):
        self.ordering_by_field(magazines, quantity)
        self.click(self._lower_kupujem_button)
        self.fill_ordering_form(name, address, zip, city, phone, email)
        city = self.get_element(self._grad_field).value_of_css_property('background')
        zip =  self.get_element(self._postanski_broj_field).value_of_css_property('background')
        cityRgb=city[0:18]
        zipRgb=zip[0:18]
        hex_city = Color.from_string(cityRgb).hex
        hex_zip = Color.from_string(zipRgb).hex
        if hex_city == '#ff0000' and hex_zip == '#ff0000':
            self.log.info("'Grad' and 'Postanski broj' fields are synchronised")
            return True
        else:
            self.log.error("'Grad' and 'Postanski broj' fields are NOT synchronised")
            return False
