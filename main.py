from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.login import *


driver = webdriver.Chrome()

#otevření první stránky, abych mohla zapsat přihlášovací údaje
pageurl = "https://apl.unob.cz/rozvrh"
driver.get(pageurl)
driver.get(pageurl) #vyhnu se vyskakovacímu oknu

#assert "Python" in driver.title

"""
#sem můžu přidat další záložky z url a překlikávat, tak mezi stránkami
ucolist = [""] #seznam záložek
for uco in ucolist:
    pageurl = "https://apl.unob.cz/rozvrh"+uco
    driver.get(pageurl)    
    source = driver.page_source
    #print(source)
"""
login(driver)

elem = driver.find_element(By.CLASS_NAME, "input-box")
elem.clear()
elem.send_keys("léto 2022/2023")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/button')
#elem = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/button/svg')
#elem = driver.find_element(By.CLASS_NAME, "bt-knob")
elem.clear()
elem.click()


assert "No results found." not in driver.page_source
driver.close()