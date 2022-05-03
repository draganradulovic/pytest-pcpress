import time
from selenium import webdriver
from configfiles.webdriverfactory import Webdriverfactory
from testing.conftest import *
from pages.prodavnica_page import Prodavnica_page
import unittest
import pytest

#defining test cases based on documentation
@pytest.mark.usefixtures("oneTimeSetUp6", "setUp6")
class Positive_order_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setingUp(self, oneTimeSetUp6):
        self.pp=Prodavnica_page(self.driver)

    @pytest.mark.run(order=1)
    def test_positive_order1(self):
        ordering_magasines=['godisnja pretplata na casopis pc (11 brojeva)']
        ordering_values=['1']
        self.pp.order(ordering_magasines, ordering_values, 'M g', 'Z x', '71000', 'Sarajevo', '003819994', 'D@g.c')
        result=self.pp.is_ordered()
        assert result == True


    @pytest.mark.run(order=2)
    def test_positive_order2(self):
        self.driver.get("https://pcpress.rs/prodavnica/index.php")
        ordering_magasines = ['polugodisnja pretplata na casopis pc (6 brojeva)']
        ordering_values = ['2']
        time.sleep(3)
        self.pp.order(ordering_magasines, ordering_values, 'ab xy', 'Dt 45', '88000', 'Mostar', '1112223334', 'ab@c.c', 'Q')
        result = self.pp.is_ordered()
        assert result == True



    @pytest.mark.run(order=3)
    def test_positive_order3(self):
        self.driver.get("https://pcpress.rs/prodavnica/index.php")
        ordering_magasines=['pretplata na digitalno izdanje casopisa pc - godisnja']
        ordering_values=['99']
        time.sleep(3)
        self.pp.order(ordering_magasines, ordering_values, 'a+B #2', 'Bo%. 2', '78000', 'Banja Luka', '012345678912', 'H_8@2.b')
        result = self.pp.is_ordered()
        assert result == True

    @pytest.mark.run(order=4)
    def test_positive_order4(self):
        self.driver.get("https://pcpress.rs/prodavnica/index.php")
        ordering_magasines = ['pretplata na digitalno izdanje casopisa pc - polugodisnja']
        ordering_values=['100']
        time.sleep(3)
        self.pp.order(ordering_magasines, ordering_values, 'Mike Johnes', 'Prijedorska 3','76300', 'Bijeljina', '065056046', 'stefan22@br.tel')
        result = self.pp.is_ordered()
        assert result == True

    @pytest.mark.run(order=5)
    def test_positive_order5(self):
        self.driver.get("https://pcpress.rs/prodavnica/index.php")
        time.sleep(3)
        ordering_magasines = ['arhiva brojeva casopisa pc']
        ordering_values = ['Broj 1']
        self.pp.order(ordering_magasines, ordering_values, 'Petar Peric', 'kozarska 2a', '78000', 'Banja Luka', '065987648', 'cpu123@gmail.co')
        result = self.pp.is_ordered()
        assert result == True

    @pytest.mark.run(order=6)
    def test_positive_order6(self):
        self.driver.get("https://pcpress.rs/prodavnica/index.php")
        time.sleep(3)
        ordering_magasines = ['knjiga 50 godina racunarstva u srbiji','arhiva brojeva casopisa pc']
        ordering_values = ['2','Broj 1']
        self.pp.order(ordering_magasines, ordering_values, 'Jovana Perić Milić', 'Siroka 4','11000', 'Beograd', '065553996', 'Zoran.123@mail.com')
        result = self.pp.is_ordered()
        assert result == True
        
