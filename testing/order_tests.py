from selenium import webdriver
from testing.conftest import *
from pages.prodavnica_index_page import Prodavnica_page
from pages.prodavnica_naruceno_page import Prodavnica_naruceno_page
import unittest
import pytest
from ddt import ddt, unpack, data
from utilities.read_data import get_csv_data
import logging
import utilities.custom_logger as cl

#defining test cases based on documentation
@pytest.mark.usefixtures("oneTimeSetUp6", "setUp6")
@ddt
class Order_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setingUp(self, oneTimeSetUp6, setUp6):
        self.pp = Prodavnica_page(self.driver)
        self.np = Prodavnica_naruceno_page(self.driver)
        self.log = cl.customLogger(logging.DEBUG)

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_positive_order_data.csv'))))
    @unpack
    def test_positive_order(self,magazines, quantity, name, adress, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, adress, zip, city, phone, email)
        result = self.np.is_ordered_successfuly()
        assert result == True


    @pytest.mark.run(order=2)
    def test_empty_order(self):
        result = self.pp.empty_order()
        assert result == True

    @pytest.mark.run(order=3)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_quantity_data.csv'))))
    @unpack
    def test_invalid_quantity(self,magazine, quantity):
        result = self.pp.invalid_quantity_order(magazine,quantity)
        assert result == True

    @pytest.mark.run(order=4)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_drpd_select_data.csv'))))
    @unpack
    def test_invalid_drpd_select(self, magazine, item):
        items=item.split(",")
        result = self.pp.invalid_selection_order(magazine, items)
        assert result == True

    @pytest.mark.run(order=5)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_name_field_data.csv'))))
    @unpack
    def test_invalid_name_field(self,magazines, quantity, name, address, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, address, zip, city, phone, email)
        result = self.np.ime_i_prezime_error_present()
        assert result == True

    @pytest.mark.run(order=6)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_address_field_data.csv'))))
    @unpack
    def test_invalid_address_field(self, magazines, quantity, name, address, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, address, zip, city, phone, email)
        result = self.np.ulica_i_broj_error_present()
        assert result == True

    @pytest.mark.run(order=7)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_phone_field_data.csv'))))
    @unpack
    def test_invalid_phone_field(self, magazines, quantity, name, address, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, address, zip, city, phone, email)
        result = self.np.phone_error_present()
        assert result == True

    @pytest.mark.run(order=8)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_invalid_email_field_data.csv'))))
    @unpack
    def test_invalid_email_field(self, magazines, quantity, name, address, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, address, zip, city, phone, email)
        result = self.np.email_error_present()
        assert result == True

    @pytest.mark.run(order=9)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'test_empty_ordering_form_data.csv'))))
    @unpack
    def test_empty_ordering_form(self, magazines, quantity, name, address, zip, city, phone, email):
        ordering_magasines = magazines.split(",")
        ordering_values = quantity.split(",")
        self.pp.order(ordering_magasines, ordering_values, name, address, zip, city, phone, email)
        result = self.np.all_errors_present()
        assert result == True

    @pytest.mark.run(order=10)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files',
                                                      'verify_zip_city_sync_data.csv'))))
    @unpack
    def test_city_zip_sync(self, magazines, quantity, name, address, zip, city, phone, email):
        result = self.pp.verify_zip_city_sync(magazines, quantity, name, address, zip, city, phone, email)
        assert result == True

