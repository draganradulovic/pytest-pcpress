from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import Base_page
from base.selenium_driver import Selenium_actions
from selenium.webdriver.support.ui import Select
import time


class Prodavnica_page(Base_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    def base_locator(self, magazine):
        magazine = magazine.lower()
        elements = {"aktuelni broj casopisa pc": "//*[@id='artikal5bg']",
                    "godisnja pretplata na casopis pc (11 brojeva)": "//*[@id='artikal1bg']",
                    "polugodisnja pretplata na casopis pc (6 brojeva)": "//*[@id='artikal0bg']",
                    "pretplata na digitalno izdanje casopisa pc - godisnja": "//*[@id='artikal14bg']",
                    "pretplata na digitalno izdanje casopisa pc - polugodisnja": "//*[@id='artikal15bg']",
                    "knjiga 50 godina racunarstva u srbiji": "//*[@id='artikal4bg']",
                    "arhiva brojeva casopisa pc": "//*[@id='artikal6bg']",
                    "arhiva brojeva casopisa connect": "//*[@id='artikal8bg']",
                    "knjiga office i windows na radnom mestu": "//*[@id='artikal9bg']",
                    "ipc 2008+ dl dvd - elektronski indeks casopisa PC": "//*[@id='artikal10bg']",
                    "knjiga pc vodic kroz primene racunara": "//*[@id='artikal12bg']"
        }

        if magazine in elements:
            base = elements.get(magazine)
            return base

    def checkbox_locator(self, magazine):
        __checkbox = (self.base_locator(magazine)) + ("//table/tbody/tr[2]/td[2]/input")
        return __checkbox

    def kolicina_field_locator(self, magazine):
        __kolicina_field = (self.base_locator(magazine)) + ("//input[contains(@id, 'kolselektor')]")
        return __kolicina_field

    def dropdown_menu_locator(self, magazine):
        __dropdown_menu = (self.base_locator(magazine))+("//select")
        return __dropdown_menu
    def kupujem_button_locator(self, magazine):
        __kupujem = (self.base_locator(magazine)) + ("//img[contains(@alt, 'Kupujem')]")
        return __kupujem



    #_checkbox = "//table/tbody/tr[2]/td[2]/input"

    #_kolicina_field = "//*[@id='kolselektor1']"
    #_dropdown_menu = "123"

    #_kupujem = "//*[@id='artikal5bg']/table/tbody/tr[2]/td[2]/img"

    _ime_i_prezime_field = "//*[@id='korisnik']/tbody/tr[1]/td[2]/input"
    _ulica_i_broj_field = "//*[@id='korisnik']/tbody/tr[2]/td[2]/textarea"
    _postanski_broj_field = "//*[@id='korisnik']/tbody/tr[3]/td[2]/input[1]"
    _grad_field = "//*[@id='korisnik']/tbody/tr[3]/td[2]/input[2]"
    _telefon_field = "//*[@id='korisnik']/tbody/tr[4]/td[2]/input"
    _email_field = "//*[@id='korisnik']/tbody/tr[5]/td[2]/input"
    _napomena_field = "//*[@id='korisnik']/tbody/tr[6]/td[2]/textarea"
    _narucujem_button = "//*[@id='korisnik']/tbody/tr[7]/td/input[2]"
    _odustajem_button = "//*[@id='korisnik']/tbody/tr[7]/td/input[3]"

    _confirmation_message="//*[@id='doubleprovera']/br[1]"


    #sa = Selenium_actions(self.driver)
    def ordering_by_field(self, magazin, kolicina, ime_i_prezime, ulica_i_broj, Postanski_broj, grad, telefon, email, napomena=''):
        self.scroll_by_ele(self.checkbox_locator(magazin))
        time.sleep(2)
        self.click(self.checkbox_locator(magazin))
        time.sleep(2)
        self.send_key(kolicina ,self.kolicina_field_locator(magazin))
        time.sleep(2)

        self.click(self.kupujem_button_locator(magazin))
        time.sleep(2)
        self.fill_ordering_form(ime_i_prezime, ulica_i_broj, Postanski_broj, grad, telefon, email, napomena)
        time.sleep(2)
        self.click(self._narucujem_button)

    def ordering_by_dropdown(self, magazin, drpd_item, ime_i_prezime, ulica_i_broj, Postanski_broj, grad, telefon, email, napomena=''):
        self.scroll_by_ele(self.checkbox_locator(magazin))
        self.click(self.checkbox_locator(magazin))
        time.sleep(2)
        self.select_from_dropdown(drpd_item, magazin)
        time.sleep(2)

        self.click(self.kupujem_button_locator(magazin))
        time.sleep(2)
        self.fill_ordering_form(ime_i_prezime, ulica_i_broj, Postanski_broj, grad, telefon, email, napomena)
        time.sleep(2)
        self.click(self._narucujem_button)


    def fill_ordering_form(self, ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena=''):
        self.send_key(ime_i_prezime, self._ime_i_prezime_field)
        self.send_key(ulica_i_broj, self._ulica_i_broj_field)
        self.send_key(postanski_broj, self._postanski_broj_field)
        self.send_key(grad, self._grad_field)
        self.send_key(telefon, self._telefon_field)
        self.send_key(email,self._email_field)
        self.send_key(napomena, self._napomena_field)

    def select_from_dropdown(self, drpd_item, magazine):
        self.dropdown_select(drpd_item, self.dropdown_menu_locator(magazine))


    def order(self, magasines_list, order_parmeters_list, ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena=''):
        magasines_list=[magasines_list]
        parameters_list=[order_parameters_list]
        i=0
        for magasine in magasines_list:
            if 'Broj' in parameters_list[i]:
                self.ordering_by_dropdown(parameters_list[i], ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena)
            else:
                self.ordering_by_field(parameters_list[i], ime_i_prezime, ulica_i_broj, postanski_broj, grad, telefon, email, napomena)




    def is_ordered(self):
        result=self.element_present(self._confirmation_message)
        return result

