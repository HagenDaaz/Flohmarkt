import urllib
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
from openpyxl import load_workbook
#soup = BeautifulSoup()



# theurl = "http://www.ntz.de/service/anzeigenservice/kleinanzeigen/marktplatz/"
theurl = "http://anzeigen.swp.de/rss.php?REGIO_PLZ_Lb=70499&tpl=such_marktplatz_privat_verkauf&radius=50"

urls = theurl

thepage = urllib.request.urlopen(urls)
soup = BeautifulSoup(thepage,"html.parser")


def harvest_url():
    i = 0
    liste = []
    for anzeigen in soup.findAll('description'):
        i = i + 1
        liste.append(str(i) + ") " + str(anzeigen.text))
        print(str(i) + ") " + str(anzeigen.text))
    return liste

