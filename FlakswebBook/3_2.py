from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLink(articleUrl):

    html = urlopen('http://')
    bsObj = BeautifulSoup()

    return bsObj

links = getLins()

while len(links)>0:
    newAticle = lins[random.randint(0, len(links)-1)].attrs['href']
    print(newAtticle)
    links = getLinks(newArticle)

pages = set()

def getLinks(pageUrl):
    global pages 
    html = urlopen('ht..')
    bsOjb = BeautifulSoup(html)

    for link in bsObj.findAll('a', href=re.compile('..')):
        if 'href' in link.attrs:
            if lin.attrs['href'] not in pages:
                newPage = 
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")



try: 
    print(bsObj.h1.get_text())
    print(bsObj.find(id='mw-content-text').findAll('p')[0])
    print(bsObj.find(id='ca-edit').find('sapn').find('a').attrs['href'])

except AttributeError:
    print('pages were not found')



