import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io
from openpyxl import load_workbook

main_site = "https://www.pz-news.de"

markt_site = "".join([main_site,"/index.php?abschicken=Anzeigen+suchen&"])

page_site1 = "costart=1"
page_site2 = "costart=26"
page_site3 = "costart=51"
page_site4 = "costart=76"
page_site5 = "costart=101"

end_site = "&date=0&location=&pageid=2065&puid=6&rubrik%5B0%5D=175&rubrik%5B1%5D=0&pageid=2065"



theurl1 = markt_site + page_site1 + end_site
theurl2 = markt_site + page_site2 + end_site
theurl3 = markt_site + page_site3 + end_site
theurl4 = markt_site + page_site4 + end_site
theurl5 = markt_site + page_site5 + end_site

print(theurl1)

urls = ([theurl1, theurl2, theurl3, theurl4, theurl5])

def text_from_img_url(img_url):
    """
    return ocr output from image
    """
    with urllib.request.urlopen(img_url) as url:

        f = io.BytesIO(url.read())
        # deutsches Sprachpaket ausgewählt
        return pytesseract.image_to_string(Image.open(f), lang='deu')

#def harvest_url(urls=urls):
pageno = 1
liste = []

for eachurl in urls:
    print("Seite ", pageno)
    pageno = pageno + 1
    thepage = urllib.request.urlopen(eachurl)
    soup = BeautifulSoup(thepage, "html.parser")
    print(soup.title.text)
    liste.append(soup.title.text)

    for anzeige in soup.findAll('section', {"class": "nfy-c-adv-advert-image"}):
        anzeige_url = anzeige.find('a').get('href')
        if anzeige_url:
            # alle anzeigen, wenn anzeige_url
            this_url = "".join([main_site, anzeige_url])
            sub_soup = BeautifulSoup(urllib.request.urlopen(this_url), "html.parser")

            for item in sub_soup.findAll('aside', {"class": "nfy-c-adv-advert-image"}):
                img_url = "".join([main_site, item.find('a').get('href')])
                print(img_url)
                liste.append(str(img_url))
                img_text = text_from_img_url(img_url)
                liste.append(str(img_text))
                print(img_text)

                if len(img_text.split('\n')) <= 10:
                    print(img_text, )
#     return liste