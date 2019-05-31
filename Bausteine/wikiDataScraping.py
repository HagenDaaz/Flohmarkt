import urllib
import urllib.request
from bs4 import BeautifulSoup
#soup = BeautifulSoup()
i = 1

theurl = "https://twitter.com/realDonaldTrump"

thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

print(soup.title.text)
""""
for link in soup.findAll('a'):
    #print(link.get('href'))
    print(link.text)
"""
#print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p'))

for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i= i + 1
