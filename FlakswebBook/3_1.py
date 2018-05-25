#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re

html = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')

bsObj = BeautifulSoup(html.text,'lxml')

for link in bsObj.find('div', {'id':'bodayCOntent'}).findAll('a', 
        href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])


