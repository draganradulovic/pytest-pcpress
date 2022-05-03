import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilladriver\geckodriver.exe")
driver.get("https://pcpress.rs/prodavnica/index.php")
url=driver.current_url
print(url)

print("https://pcpress.rs/prodavnica/naruceno.php")

driver.find_element(By.XPATH, "//*[@id='artikal5bg']/table/tbody/tr[2]/td[2]/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='artikal5bg']/table/tbody/tr[2]/td[2]/img").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='korisnik']/tbody/tr[1]/td[2]/input").send_keys("dragan op")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='korisnik']/tbody/tr[7]/td/input[2]").click()
url=driver.current_url
print(url)
time.sleep(5)