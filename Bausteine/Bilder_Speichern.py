import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io

main_site = "https://www.mein-mittwochmarkt.de"

markt_site = "".join([main_site,"/Marktplatz/"])

theurlpage1 = "".join([markt_site, "dies-und-das.html?sl=60400"])
theurlpage2 = "".join([markt_site, "dies-und-das-Part2.html?sl=60400&nPart=2"])
theurlpage3 = "".join([markt_site, "dies-und-das-Part3.html?sl=60400&nPart=3"])
theurlpage4 = "".join([markt_site, "dies-und-das-Part4.html?sl=60400&nPart=4"])
theurlpage5 = "".join([markt_site, "dies-und-das-Part5.html?sl=60400&nPart=5"])


thepage = urllib.request.urlopen(theurlpage1)


soup = BeautifulSoup(thepage,"html.parser")
print(soup.title.text)


def text_from_img_url(img_url):
    """
    return ocr output from image
    """
    with urllib.request.urlopen(img_url) as url:

        f = io.BytesIO(url.read())

        return pytesseract.image_to_string(Image.open(f), lang='eng')


for anzeige in soup.findAll('div',{"class":"MarketSearchCtrl_ResultList_Image"}):
        anzeige_url = anzeige.find('a').get('href')
        if anzeige_url:
            # alle anzeigen, wenn anzeige_url
            this_url = "".join([main_site, anzeige_url])
            sub_soup = BeautifulSoup(urllib.request.urlopen(this_url),"html.parser")


            for item in sub_soup.findAll('div',{"class":"lightBoxDiv"}):
                img_url = "".join([markt_site, item.find('a').get('href')])

                img_text = text_from_img_url(img_url)

                if len(img_text.split('\n')) <= 10:
                    print(img_text, )


#theurl2 = "https://www.mein-mittwochmarkt.de/Marktplatz/Motiv-m128823.html?from=29.05.2019&to=04.06.2019&sort=tblMotif.dtmWebBegin+desc&sl=60400&cid=70300&sl=60400&branch="
#for image in soup.findAll('div',{"class":"lightBoxDiv"}):
#        print(image)
#for link in soup.findAll('a'):
#    variable = link.get('href')
#    print(variable)



#https://www.mein-mittwochmarkt.de/Marktplatz/Motif/Korb-Rattan-TruhenAuswahl-Korbhaus-Tue-Kilchberg-Bahnhofs--v3-w1024-h-m128814.jpg


#for img in soup.findAll('img'):
#print(img.get('src'))

#thepage = urllib.request
#soupdata=BeautifulSoup(thepage, "html.paser")
#soup = make_soup




#resource = urllib.request.urlopen("https://www.mein-mittwochmarkt.de/Marktplatz/Motif/Verkaufe-Schmuck-und-Gemaelde--v3-w1024-h-m128823.jpg")
#output = open("file01.jpg","wb")
#output.write(resource.read())
#output.close()
