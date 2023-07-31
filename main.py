from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.login import *
from modules.open_rozvrh import *
from modules.open_page import *
import uuid
import json
import re

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
openPage(driver) 
#assert "Python" in driver.title
login(driver)
driver.maximize_window()
openRozvrh(driver)

"""
Zkouším vypsat informace z rozvrhu
nejdříve nadpis léto 2022/2023

potom celé políčko:
    přes XPATH --> nefunguje (zakomentováno)
    přes CLASS_NAME --> funguje

potom jeden konrétní řádek
"""

#nadpis léto 2022/2023
try:
    elem = WebDriverWait(driver, timeout=120).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/button'))
    print("Nadpis nalezen")
    print(elem.text)
except:
    print("Nadpis NEnalezen")

try:
    #elem = WebDriverWait(driver, timeout=120).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div/svg/g/g[1]/g'))
    elem = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,'event-description'))
    print("Políčko nalezeno")
    print(elem.text)
except:
    print("Políčko NEnalezeno")

#jeden konkretní řádek v políčku --> nefunguje
try:
    elem = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,'text.event-text.who'))
    print("Řádek nalezen")
    print(elem.text)
except:
    print("Řádek NEnalezen (1)")

#jeden konkretní řádek v políčku --> nefunguje
try:
    elem = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,'event-text who'))
    print("Řádek nalezen")
    print(elem.text)
except:
    print("Řádek NEnalezen (2)")

source = driver.page_source
# print(source)
assert "No results found." not in driver.page_source
driver.close()

# stáhnout celou stránku - uložit do souboru