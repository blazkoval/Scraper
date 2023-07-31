# Projekt Scraper

## Zadání
Extrakce dat z prostředí IS UO () pro kontejner gql_events (kategorie událostí, typy událostí, trvání události)

## Úvod
Veškeré vytvořené funkce jsou ve složce modules a jsou naimportovány do main.py<br>

## Otevření, přihlášení
Moduly open_page.py a login.py slouží k otevření stránky, následné přihlášení do systému pomocí knihovny Selenium. Přihlašovací údaje jsou umístěny v adresáři nad složkou Scraper, abych je neposílala zároveň s aktualizacemi na github.<br>

## Načtení rozvrhu
Načtení rozvrhu je v modulu open_rozvrh.py<br>
První problém, který se objevil bylo dlouhé načítání rozvrhu. Proto je potřeba použít WevDriverWait, který čeká, než se element na stránce objeví, a nebo až uběhne timeout (v sekundách) - efektivnější řešení oproti pouhému sleep.<br>
Elementy na stránce hledám pomocí XPATH a NAME, ale lze je hledat i např. pomocí CLASS_NAME.<br>
Nedařilo se mi lokalizovat elementy, které vyjadřují jednotlivé položky události jako název, typ události apod. Dalším velkým problémem je, že se zdrojový kód stránky zobrazuje pouze z toho, co je na obrazovce a při každém posunutí kolečkem myši se mění. Použití knihovny Selenium by pro scrapování dat přímo ze stránky bylo proto obtížnější. Zvolila tedy jednodušší cestu a to stažení souboru csv, který se na stránce nabízí, a s ním dále pracovat.

## Extrakce dat
V modulu data_extracion.py jsou funkce pro extrakci dat z rozvrh.csv a následně vytvoření JSON file. <br>
Exhtrahuuji data pro kontejner gql_event https://github.com/hrbolek/_uois/tree/v2.1/gql_events/gql_events <br>
Zde jsou globální proměnné events a eventtypes typu list, které vyjadřují dva hlavní modely podle DBDefinitions. Atributy těchto modelů jsou ukládány do dictionary ve formátu z příkladu v DBFeeder.<br>
Každému eventu a eventtypu generuji originální ID podle uuid1.<br>
*Poznámka: znaky v uuid1 se viditelně mění v předposlední skupině znaků mezi spojovníky, takže na první pohled vypadají stejně, ale opravdu má každá událost jiné uuid.*<br>
Poslední problém byl načítání dat do listu, kde na 3501. položce v rozvrh.csv mi vyskočila chyba. Tato chyba byla způsobená nehomogenní strukturou v rozvrh.csv, kde 3501. položka (a pravděpodobně další) má pouze jeden sloupec.
Nakonec jsem data z proměnných vložila do JSON souboru extractedData.json.
