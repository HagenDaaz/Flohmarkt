import urllib
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
#soup = BeautifulSoup()
i = 0

main_site = "https://www.esslinger-zeitung.de/"
markt_site = "".join([main_site,"/anzeigensuche_costart,"])

theurl1 = "".join([markt_site, "1_pageid,anzeigensuche_rubrik,1172.html"])
theurl2 = "".join([markt_site, "11_pageid,anzeigensuche_rubrik,1172.html"])
theurl3 = "".join([markt_site, "21_pageid,anzeigensuche_rubrik,1172.html"])
theurl4 = "".join([markt_site, "31_pageid,anzeigensuche_rubrik,1172.html"])
theurl5 = "".join([markt_site, "41_pageid,anzeigensuche_rubrik,1172.html"])
theurl6 = "".join([markt_site, "51_pageid,anzeigensuche_rubrik,1172.html"])
theurl7 = "".join([markt_site, "61_pageid,anzeigensuche_rubrik,1172.html"])

urls = ([theurl1, theurl2, theurl3, theurl4, theurl5, theurl6, theurl7])
Anzeigennr=1
Seitennr=1

for eachurl in urls:
    print("Seite",Seitennr)
    thepage = urllib.request.urlopen(eachurl)
    soup = BeautifulSoup(thepage,"html.parser")
    Seitennr=Seitennr+1

    for anzeigen in soup.findAll('section', {"class": "nfy-c-adv nfy-c-adv-search-teaser cf"}):
        print("Anzeige ",Anzeigennr)
        print(anzeigen.find('p').text)
        Anzeigennr = Anzeigennr + 1
""""
for link in soup.findAll('a'):
    #print(link.get('href'))
    print(link.text)
"""
#print(soup.find('div',{"class":"tx-ntzkleinanz-pi1"}).find('article',{"class":"teaser"}).find('p').text)

liste = []

    #liste.append(str(i) + ". " + str(anzeigen.find('p').text))

#print(liste[0])
