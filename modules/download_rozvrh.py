from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def downloadRozvrh(driver):
    if (path.exists("rozvrh.csv") == False):
        elem = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/div[2]/button[3]'))
        elem.click()
    else:
        print("soubor rozvrh.csv jiz stazen")