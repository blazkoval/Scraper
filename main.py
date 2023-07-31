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
import uuid
import json
import re

#změna defaultního adresáře pro stahování souborů
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\work\Stefek\Scraper"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)

openPage(driver) 
login(driver)
driver.maximize_window()
openRozvrh(driver)
# try:
#     elem = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/button'))
#     print("rozvrh nacten")
# except:
#     print("rozvrh nenacten")
downloadRozvrh(driver)
dataExtraction()

# source = driver.page_source
# print(source)
assert "No results found." not in driver.page_source
driver.close()

# 'events': [
#     {
#         'id': "45b2df80-ae0f-11ed-9bd8-0242ac110002" , 'name': 'Zkouška', 'name_en': 'Exam', 
#         'eventtype_id': 'b87d3ff0-8fd4-11ed-a6d4-0242ac110002',
#         'startdate': datetime.datetime(year=2022, month=11, day=2, hour=8, minute=0), 
#         'enddate': datetime.datetime(year=2022, month=11, day=2, hour=10, minute=0)
#     }

# 'eventtypes' : [
#       {'id': "c0a12392-ae0e-11ed-9bd8-0242ac110002" , 'name': 'P', 'name_en': ''},