import os, sys
import urllib
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from pprint import pprint

_basePath = os.path.realpath(os.path.dirname(__file__))
sys.path.append(_basePath)

from Bausteine.xlsxReader import XlsxReader
from Bausteine.Esslinger_Zeitung import harvest_url as esz_liste
from Bausteine.Schw_Tagblatt import harvest_url as schw_tag_liste

#reader = XlsxReader("Anzeigen_Flohmarkt.xlsx", path=os.path.dirname(__file__), sheet_name="Anzeigen")

# reader.find_header(header_names=["Datum Suche", "Zeitung", "Bezeichnung",
#                                  "Datum", "Uhrzeit Start", "Uhrzeit Ende",
#                                  "Ort", "PLZ", "Straße", "Haus-Nr.", "Zusatz",
#                                  "Telefon-nummer", "Text"])

liste1 = esz_liste()

liste2 = schw_tag_liste()

print(liste1 + liste2)
