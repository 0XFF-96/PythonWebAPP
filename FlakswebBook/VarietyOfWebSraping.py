from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Retrieves a list of all Internall links found on a page 
def getInternalLinks(bsOjb, includeUrl):
    internalLinks = []
    for lin 



    return internalLinks

def getExternalLinks(bsOjb, excludeUrl):
    externalLinks = []

    #Finds all links that start with 'http' or 

    return externalLinks

def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')

    return addressParts

def getRandomExternalLink(startingPage):

    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)

    externalLinks = getExternalLins(bsOjb, splitAddress(starignPage)[0])

    return 

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink('hh')
    print('R')
    followExternalOnly(exteranlLink)

followExternalOnly('https:')

#Refactored 


allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getIntgeranlLinks(bsOjb, splitAddress(siteUrl)[0])
    externalLinks = getExteranlLinks(bsObj, splitAddress(siteUrl)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinsk.add(Link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print('About to get link' + link)
            allIntLinks.add(link)
            getallExternalLinks(link)


    getAllExternalLinks('http://oreilly.com')


