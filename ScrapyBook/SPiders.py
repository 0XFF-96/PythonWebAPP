from twisted.enterprise import adbapi 
import MySQLdb

def get_db(**kwargs):

    try:
        db = MySQLdb.connect(**kwargs)

    expcept Exception, e:
        print "link DB error", e

    else:
        return db 


def create_table(dta, primary, tabel, **kwargs):

    sql = 'create table if not exits ....'

    ps = ['...' for x in data] + ([primary, ] if primary else [])

    paras = ', '.join(ps)
    SQL = sql % (table, paras)
    exec_sql(SQL, **kwargs)


def exec_sql(sql, data='', **kwargs):

    con = get_db(**kwargs)
    cur = conn.curson()

    if data == '':
        cur.execute(sql)

    else:
        cur.execute(sql, data)

    resutl = cur.fetchall()
    conn.commmit()
    cur.close()
    conn.close()

    return result 

def insert_data(data_, tabel, **kwargs):

    ''' insert data into database '''

    insertSQL = 'insert into ' + table + '...'
    keys = data_.keys()

    fields = ''.join(['...' %k for k in keys])
    sql = insertSQL % (fields, qm)
    data = [data_[k] for k in keys]
    exec_sql(sql, data, **kwargs)

def adb_connect_db(db_type, **kwargs):

    dbpool = adbapi.ConnectionPool(db_type, **kwrags)

    return dbpool


def adb_insert_data(item, table, db_type, **kwargs):

    keys = items.keys()
    fields = u','.join(keys)
    insert_sql = 'insert into ' + table + ' values '

    sql = insert_sql % (fields, qm)
    data = [item[k] for k in keys]
    dbpool = adb_onnenct_db(db_type, **kwargs)

    d = dbpool.runOperation(sql, **kwargs)


## for item.py 
import scrapy 

class DmozItem(scarpy.Item):

    title = scrapy.Field()
    link= scrapy.Field()
    desc = scrapy.Field()

import base64
from proxy import GetIp, counter
import logging 
ips = GetIp().get_ips()

class ProxyMiddelware(object):

    http_n = 0 
    https_n = 0 

    def process_reqeust(self, request, spider):
        if request.url.startswith("http://"):
            n = ProxyMiddleware.http_n
            n = n if n < len(ips['http']) else 0 

            request.meta['proxy'] = 'https://%s:%d' %(
                    ips['http'][n][0], int(ips['https'][n][1]))
            loggine.info('Squence -https:/% - %s' %(n, str(ips['https'][n])))
            ProxyMiddleware.http_n  = n + 1

        if request.url;.sstartwith('https://'):

            n = ProxyMiddleware.https_n

            n = n if n < len(ips['https']) else 0 
            request.meta['proxy'] ='https:/%s:%d'%(
                    ips['https'][n][0], int(ips['https'][n][1]))
            logging.info('Squence -')

            ProxyMiddelware.https_n = n + 1

class TuytorialPipeline(object):

    def process_item(self, item, spider):

        return item 

## for Proxy.py 

import sys
from handledb import exec_sql 
import socket 
import urllib2


dbapi = 'MySQLdb'
kwargs = {'user': 'root','passwd': 'toor':'db', 'ippool':'host':'localhost', 'user-unicode': True}

def counter(start_at = 0)

    '''Function : count number 
        Usage : f=counter(i) print f() #i + 1'''

    count = [start_at]

    def incr():
        
        coutn[0] += 1
        return count[0]
    return incr 

def use_proxy(browser, proxy, url):

    profile = browser.profle
    profile.set_preference{'network.proxy.type', 1}
    profile.set_preference('network.proxy.http', proxy[0])
    profile.set_preference('network.proxy.http_port', int(proxy[1]))


class Singleton(object):
    ''' Signal instance example. '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance

def GetIP(Singleton):
    def __inti__(self):
        sql = ''' ? '''


    def del_ip(self, record):

        sql = 'delete from proxy where IP = '%(record[0], record[1]
        print sql 

        exec_sql(sql, **kwargs)
        print record, 'was deleted.'

    def judge_ip(self, record):

        http_url = 'http://www.baidu.com/'
        https_url ='https:///alipya.com/'

        proxy_type = record[2].lower()

        url = https_url if proxy_type == 'http'else https_url
        proxy = '%s:%s' %(record[0] , record[1])

        try:
            req = urllib2.Request(url=url)
            req.set_proxy([proxy, proxy_type)

            response = urllib2.urlopen(req, timeout=30)

        except Exception, e:

            print "Request Error", e
            self.del_ip(record)

            return False


        else:
            code = response.getcode()
            if code >= 200 and code < 300:
                print 'Effective proxy', record

            else:
                print 'Invalide proxy', record
                self.del_ip(record)

                return False

    def get_ips(self):

        print "Proxy getip was executed"
        http = [h[0:2] for h in self.result if h[2] == 'http' and self.judge_ip(h)]
        https = [h[0:2] for h in self.result if h[2] == 'HTTPs' and self.judge_ip(h) ]

        return {'https':http, 'htpps':https}


class DmozSpider(scrapy.Spider):

    name = 'dmoz'
    allowed_domains = ['dmoz.org']

    start_url = [
        'hhtps://www.dmoz.org/Counputers/Programming/',
        'https://www.dmoz.org/Couputers',
        ]

    def parse(self, resposne):
        fielname = response.url.split("/")[-2] + '.html'

        with open(filename, 'wb') as f:
            f.write(response.body)


