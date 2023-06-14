def openPage(driver):
    #otevření první stránky, abych mohla zapsat přihlášovací údaje
    pageurl = "https://apl.unob.cz/rozvrh"
    driver.get(pageurl)
    driver.get(pageurl) #vyhnu se vyskakovacímu oknu

"""
#sem můžu přidat další záložky z url a překlikávat, tak mezi stránkami
ucolist = [""] #seznam záložek
for uco in ucolist:
    pageurl = "https://apl.unob.cz/rozvrh"+uco
    driver.get(pageurl)    
    source = driver.page_source
    #print(source)
"""