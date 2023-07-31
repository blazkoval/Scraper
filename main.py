from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.login import *
from modules.open_rozvrh import *
from modules.open_page import *
from modules.download_rozvrh import *
from modules.data_extraction import *


from os import path


#změna defaultního adresáře pro stahování souborů
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\work\Stefek\Scraper"}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=options)

openPage(driver) 
login(driver)
driver.maximize_window()
openRozvrh(driver)
downloadRozvrh(driver)
driver.close()
dataExtraction()
