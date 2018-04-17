## items.py

import scrapy 

class DmozItem(scrapy.Item):

    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


### Pipelines.py

class TutorialPipeline(object):

    def process_item(self, item, spider):
        return item  


###
import scrapy 

class DmozSpider(scrapy.Spider):

    name = 'dmoz'
    allowed_domains = ['dmonz.org']

    start_urls  = {
            'http://www.dmoz.org....', 
            'https://www.dmoz/coum/..', 
            }
    def parse(self, response):

        filename = response.url.split("/")[-2] + '.hmtl'

        with open(fileanme, 'wb') as f:
            f.write(response.body)

##pipelines.py

#   Define your item pipelines here 
# Don't forget to add your pipeline to the ITEM_PIPELIENS setting 

import MySQLdb 

DBKWARGS={'db':'test', 'user':'root', 'passwd':'', 
        'host':'localhost', 'user_unicode':True, 'charset':'utf-8'}

class TutorialPipeline(object):

    def __init__(self):
        try:
            self.con =MySQLdb.connect(**DBKWARGS)
            
        except Exception, e:

            print "Connect db error", e

    def process_item(self, item, spider):

        cur = self.con.cursor()
        sql = "insert into dmoz_book vlaues(%s, %s, %s)"
        lis = (''.join(item['title']).''.join(item['link']), 
                ''.join(item['desc']))

        try:
            cur.execute(sql, lis)

        except Exception, e:
            print "insert error", e
            self.con.rollback()

        else:
            self.con.commit()

        cur.close()

        return item


    def __del__():

        try:
            self.con.close()

        except Exception, e:
            print "Close db error"

## Don't forget to add your pipelines 
## ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline': 300, 
}



