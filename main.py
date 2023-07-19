from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.login import *
from modules.open_rozvrh import *
from modules.open_page import *


#driver = webdriver.Firefox()
driver = webdriver.Chrome()
openPage(driver) 
#assert "Python" in driver.title
login(driver)
driver.maximize_window()
openRozvrh(driver)

try:
    #jedno políčko v rozvhru
    #elem = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div/svg/g/g[1]/g'))
    elem = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.CLASS_NAME,'event-description'))
    print("Element nalezen")
except:
    print("Element NEnalezen")
#elem = WebDriverWait(driver, timeout=40).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div/svg/g/g[6]/g/text[1]'))
print(elem.text)

# source = driver.page_source
# print(source)
assert "No results found." not in driver.page_source
driver.close()
