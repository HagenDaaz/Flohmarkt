import urllib.request
import os
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
import io
import re
from openpyxl import load_workbook

main_site = "https://www.pz-news.de"

markt_site = "".join([main_site,"/index.php?abschicken=Anzeigen+suchen&"])

page_site1 = "costart=1"
page_site2 = "costart=26"
page_site3 = "costart=51"
page_site4 = "costart=76"
page_site5 = "costart=101"

end_site1 = "&date=0&location=&pageid=2065&puid=6&rubrik%5B0%5D=175&rubrik%5B1%5D=358&pageid=2065"
end_site2 = "&date=0&location=&pageid=2065&puid=6&rubrik%5B0%5D=175&rubrik%5B1%5D=360&pageid=2065"




theurl1 = markt_site + page_site1 + end_site1
theurl2 = markt_site + page_site2 + end_site1
theurl3 = markt_site + page_site3 + end_site1
theurl4 = markt_site + page_site4 + end_site1
theurl5 = markt_site + page_site5 + end_site1
theurl6 = markt_site + page_site1 + end_site2
theurl7 = markt_site + page_site2 + end_site2
theurl8 = markt_site + page_site3 + end_site2
theurl9 = markt_site + page_site4 + end_site2
theurl10 = markt_site + page_site5 + end_site2


# print(theurl1)

#urls = ([theurl1, theurl2, theurl3, theurl4, theurl5, theurl6, theurl7, theurl8, theurl9, theurl10])
urls = ([theurl1, theurl2, theurl3, theurl4, theurl5, theurl6])
#urls = ([theurl1, theurl2, theurl3, theurl4])

def text_from_img_url(img_url):
    """
    return ocr output from image
    """
    with urllib.request.urlopen(img_url) as url:

        f = io.BytesIO(url.read())
        # deutsches Sprachpaket ausgewählt
        return pytesseract.image_to_string(Image.open(f), lang='deu')

def harvest_url(urls=urls):
    pageno = 1
    liste = []

    for eachurl in urls:
        print("Seite ", pageno)
        pageno = pageno + 1
        thepage = urllib.request.urlopen(eachurl)
        soup = BeautifulSoup(thepage, "html.parser")
        # print(soup.title.text)
        # liste.append(soup.title.text)
        # print(eachurl)

        for anzeige in soup.findAll('section', {"class": "nfy-c-adv-advert-image"}):
            # print(anzeige.find('img').get('src'))
            anzeige_url = anzeige.find('img').get('src')
            # print(anzeige_url.text)
            # print(anzeige)

            if anzeige_url:
                # alle anzeigen, wenn anzeige_url
                img_url = "".join([main_site, anzeige_url])
                print(img_url)
                liste.append(str(img_url))

                try:
                    img_text = text_from_img_url(img_url)
                except OSError:
                    continue
                text = img_text.replace('\n', ' ')
                # text = img_text.replace(r'\n\r', '')
                text = text.replace(os.linesep, ' ')
                liste.append(text)
                print(text)

    return liste
