import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io
#variable = np.array(["Hagen",2,3])
main_site = "https://www.mein-mittwochmarkt.de"
markt_site = "".join([main_site,"/Marktplatz/"])
theurlpage1 = "".join([markt_site, "dies-und-das.html?sl=60400"])
theurlpage2 = "".join([markt_site, "dies-und-das-Part2.html?sl=60400&nPart=2"])
#theurlpage3 = "".join([markt_site, "dies-und-das-Part3.html?sl=60400&nPart=3"])
#theurlpage4 = "".join([markt_site, "dies-und-das-Part4.html?sl=60400&nPart=4"])
#theurlpage5 = "".join([markt_site, "dies-und-das-Part5.html?sl=60400&nPart=5"])

theurl = ([theurlpage1, theurlpage2])
pageno=1

for i in theurl:
    #thepage = urllib.request.urlopen(theurlpage1)
    #soup = BeautifulSoup(thepage, "html.parser")
    #print(soup.title.text)
    print(i)
    print("Seite ", pageno)
    pageno=pageno+1
