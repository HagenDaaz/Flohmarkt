import urllib.request
from bs4 import BeautifulSoup

theurl = "https://www.mein-mittwochmarkt.de/Marktplatz/dies-und-das.html?sl=60400"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")
print(soup.title.text)

for anzeige in soup.findAll('div',{"class":"MarketSearchCtrl_ResultList_Image"}):
        print(anzeige.find('a').get('href'))

#theurl2 = "https://www.mein-mittwochmarkt.de/Marktplatz/Motiv-m128823.html?from=29.05.2019&to=04.06.2019&sort=tblMotif.dtmWebBegin+desc&sl=60400&cid=70300&sl=60400&branch="
#for image in soup.findAll('div',{"class":"lightBoxDiv"}):
#        print(image)
#for link in soup.findAll('a'):
#    variable = link.get('href')
#    print(variable)






#for img in soup.findAll('img'):
#print(img.get('src'))

#thepage = urllib.request
#soupdata=BeautifulSoup(thepage, "html.paser")
#soup = make_soup




#resource = urllib.request.urlopen("https://www.mein-mittwochmarkt.de/Marktplatz/Motif/Verkaufe-Schmuck-und-Gemaelde--v3-w1024-h-m128823.jpg")
#output = open("file01.jpg","wb")
#output.write(resource.read())
#output.close()