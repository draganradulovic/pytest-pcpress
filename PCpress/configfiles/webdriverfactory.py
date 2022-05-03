from selenium import webdriver
from selenium.webdriver.common.by import By

#Class contains method for defining browser.
class Webdriverfactory():

    def __init__(self, browser):
        self.browser=browser.lower()

    #other browsers will be added
    def driver_instance(self):
        #if self.browser == 'firefox':
            #driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilladriver\geckodriver.exe")
        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
        return driver

