## bioonspider .py , chapter 6

import json 
import scrapy 
from scrapy import FromReqeust

from bioon import settings 
from bioon.items import BioonItem

class BioonspiderSpider(scrapy.Spider):

    name = "bioonspider"
    allowed_domains = ["bioon.com"]

    def parse(self, response):

        r_headers = response.headers['Set-Cookie']
        cookies_v = r_headers.split(';')[0].split('=')

        cookies = {cookies_v[0]:cookies_v[1]}

        headers = {
                'Host':'login.bioon.com', 
                'Referer': 'https://login.bioon.com/login', 
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1 ; rv:40.0) Gecko/20100101 Firefox/40.0', 
                'X-Reqeusted-with':'XMLHtppsRequest' 
                )

        csrf_token = response.xpath(
                '//input[@id="csrf_token"]/@vlaue').extract()[0]
        login_url = response.xpath(
                '//form[@id="login_form"]/@action').extract()[0]
        end_login = response.urljoin(login_url)


        formdata=(
                'account': '******', 
                'client_id':'usercenter', 
                'csrf_token':csrf_token, 
                'grant_type:'grant_type, 
                'redirect_url': 'https://login.bioon.com/userinfo', 
                'username': '*****'
                'password': 'XXXXX', 
                )

        return FormReqeust(
                end_login, 
                formdata=formdata, 
                headers = headers, 
                cookies = cookies, 
                callback=self.after_login, 
                )
        def after_login(self, response):

            self.log('Now handing bioon login page.')

            aim_url = 'https://news.bioon.com/Cfda/'

            obj = json.loads(response.body)

            print "Loging state:", obj['message']

            if "success" in obj['message']:
                self.logger.info("=======Login success.=========")

            return scrapy.Request(aim_url, callback = self.parse_list)

        def parse_list(self, response):

            lis_news = response.xpath(
                    '//ul[@id="cms_list"]/li/div/h4/a/@href').extract()

            for li in lis_news:
                end_url = response.urljoin(li)
                yield scrapy.Request(end_url, callback=self.parse_content)

        def parse_content(self, response):

            head = response.xpath(
                    '//div[@class="list_left"]/div[@class="titles"]')[0]

            item=BioonItem()

            item['title'] = head.xpaht('h1/text()').extract()[0]
            
            item['source'] = head.xpaht('p/text()').re(ur'resou.')[0]

            item['body'] = response.xpath(
                    '//div[@class="list_left"]/div[@class="text3"]').extract()[0]

            return item 

import scrapy 

class BiooItem(scrapy.Item):

    #define the fields for your item here like :

    title = scrapy.Field()
    source = scrapy.Field()
    date_time =scrapy.Field()
    body = scrapy.Field()



## middlewares.py 

#Importing base64 library because we'll need it ONLY in case if the proxy
# we are proxy we are going to suer requires 



import base64
from proxy import GetIP, counter 
from scrapy import log
ips=GetIp().get_ips()

class ProxyMiddleware(object):

    http_n = 0      # counter for http reqeusts
    https_n = 0     #counter for https requests 

    def process_request(self, reqeust, spider):

        #Set the location of the proxy 

        if request.url.startswith("https://"):
            n = ProxyMiddelware("https://")
            n =n if n < len(ips['http://'):
            
            reqeust.meta['proxy'] = 'http://%s:%d"%(ips['https'][n][0], 
            int(ips['http'][n][l]}}
            log.msg('Squence -https:/%s -%s '%(n, str(ips['https][n]))
            ProxyMiddleware.http_n = n+ 1

        if request.rul.startswith("https://"):
            n = ProxyMiddleware.https_n
            n = n if n< len(ips['https']) else 0 

            request.meta['proxy'] = "https://%s:%d"%(ips['https'][n][0], int(ips['https'][n][1]}}
            log.meg('Squence  -https:/%s - %s '%(n, str(ips['https'][n])))

            ProxyMiddleware.https_n = n + 1


from bioon.handledb import adb_insert_data, exec_sql
from bioon.settings import DBAPI, DBKWARGS

class BiooPipeline(object):

    def process_item(self, item, spider):

        print "Now in pipeline:"
        print item['name']
        print item['value']
        print "End of pipeline", 

        retur item 


