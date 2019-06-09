import urllib
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
#soup = BeautifulSoup()
i = 0



theurl = "http://www.ntz.de/service/anzeigenservice/kleinanzeigen/marktplatz/"

thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
""""
for link in soup.findAll('a'):
    #print(link.get('href'))
    print(link.text)
"""
#print(soup.find('div',{"class":"tx-ntzkleinanz-pi1"}).find('article',{"class":"teaser"}).find('p').text)

liste = []
for anzeigen in soup.findAll('article',{"class":"teaser"}):
    print(anzeigen)
    #print(anzeigen.find('p').text)
    i = i + 1
    #liste.append(str(i) + ". " + str(anzeigen.find('p').text))

#print(liste[0])



