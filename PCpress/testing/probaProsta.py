from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
driver.get(https://www.olx.ba/)

magasines=['pc prodaja casopisa']
kolicina=['2']

def ispis(niz):
    i=0
    for item in niz:
        if kolicina[i]=='2':
            print(item)
            i=i+1
        else:
            print("jbg")

ispis(magasines)