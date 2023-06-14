from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def openRozvrh(driver):
    #elem = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME, "input-box")) #pouziva element class --> lepsi je xpath (originalni)
    elem = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/input"))
    elem.clear()
    elem.send_keys("léto 2022/2023")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/button').click() #zavření panelu

    # počkat na stránku - najít funkci ...exeption - opustí příkaz řádek až když je stránka načtena něco jako "wait for page"