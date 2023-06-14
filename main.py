from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.login import *
from modules.open_rozvrh import *
from modules.open_page import *

driver = webdriver.Chrome()

openPage(driver) 
#assert "Python" in driver.title
login(driver)
openRozvrh(driver)

assert "No results found." not in driver.page_source
driver.close()