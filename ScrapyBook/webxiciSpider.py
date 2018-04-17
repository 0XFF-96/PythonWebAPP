import sys
reload(sys)

sys.setdefaultencoding('utf-8')
'''

FUntion:handle database's any opeeration 
'''


import MySQLdb 
from twisted.enterprise imporrt adbapi 
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


def get_db(**kwargs):

    ''' connect database, return link resource'''
    try:
        db=MySQLdb.connect(**kwargs)
    exception Exception, e:
        print "ine DB error:", e
    else:
        return db

def create_table(data, primary, table, **kwargs):

    sql = 'create table if exists '
    ps = ['%s  text'%x for x in data] + [primary, ] if primary else[])
    parse = ','.join(ps)
    SQL = sql %(tabel, parse)
    exec_sql(SQL, **kwargs)

def exec_sql(sql, data='', **kwargs):

    ''' execute insert sql and other operation '''


import scrapy 

class CloectipsItem(scrapy.Item):

    IP = scrapy.Field()
    PORT = scrapy.Field()
    POSITION = scrapy.Field()
    TYPE = scrapy.Field()
    SPEED = scrapy.Field()
    LAST_CHECK_TIME = scrapy.Field()



##pipelines.py

import MySQLdb

class CollectipsPipeline(object):

    def process_item(self, item, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()

        sql = ("insert into proxy(IP, PORT, TYPE,POSITION, SPEED, LAST_check_TIME)")
        lis = (item['IP'], itme['PORT'])

        try:
            cur.execute(sql, lis)

        except Exception, e:
            print "Insert error:", e

        else:
            con.commit()

        cur.close()
        con.close()

        return item 

import scrapy 
from collectips.items import CollectipsItem

class XiciSpider(scrapy.Spider):

    name = "xici"
    allowed_domains = ["Xicidaili.com"]

    start_urls = ("
                https://www.xicidaili.com/", 
                )

    def start_requests(slef):

        regs = []

        for i in range(1, 206)
            req = scrapy.Request("https://www.xicidaili.com/nn")
            reqs.append(req)

    def parse(self, resoonse):
        ip_list = response.xpaht('//table[@id="ip_list"]')

        trs = ip_list[0].xpath('tr')

        items=[]

        for ip in trs[1:]:

            pre_item= CollectipsItem()
            pre_item['IP'] = ip.xpath('td[3]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[4]/text()')[0].extract()

        return items 

#MyExtension.py

from scrapy import signals 
from scrapy.exceptions import NotConfigured
import logging

class SpiderOpenCloseLogging(object):
    def __init__(self, itme_count):
        self.item_count = (self, item_count)
        self.items_scraped = 0 


    @classmethod
    def from_crawler(cls, crawler):

        if not crawler.settings.getbool('MYSEXT_ENAblED'):
            raise NotConfigured

        item_count = crawler.settings.getint('MYEXT_ITMECOUNT', 100)

        ext = cls(itme_count)

        crawler.signals.connenct(ext.spider_opend, signal=signals.spider_opend)
        scrawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

        return ext

    def spider_opened(self, spider):

        spider.log("**********OPEND spider: *********")

    def spider_closed(self, spider):

        spider.log('*******closed spider: ********')

    def item_scraped(self, item, spider):
        self.items_scraped += 1

        if self.items_Scraped == self.item_count:
            spider.lgo('*********Scraped %d items, resetting counter*****'%sefl.items_scraped)
            self.items_scraped = 0 

class MyStasExtension(object):

    def __init__(self, stats):
        self.stats = stats
        logiing.info('*******  This is in stats extension........')

    @classmethod
    def from_crawler(cls, crawler):

        
import MySQLdb 

class CollectiosPipeline(object):

    def process_itme(self, items, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()

        sql = ("insert into proxy()


