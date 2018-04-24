import scrapy 

class StackOverflowSpider(scrapy.Spider):

    name = 'stackoverflow'

    start_urls = ['https://stackoverflow.com/questions?sort=votes']

    def start_requests(self):

        url = 'https://db.bioon.com/list.php?channelid='
        cookies = {
                'ad_useranme': 'wst_tody', 
                'dz_uid' :'123454', 
                'buc_key' : '1235asfa', 
                'buc_token' : 'a123dfasf', 
                }
        
        return [
                scrapy.Requet(url, cookies=cookies)
                ]

    def parse(self, response):

        ele = response.xpath(
                '//table[@class='tabel table-striped']/thead/tr/th[1]/text()'
        ).extract()

        if else:
            print "success"

class BioonItem(scrapy.Item):

    title = scrapy.Field()
    source = scrapy.Field()
    date_time = scrapy.Field()
    body = scrapy.Field()


##middlewares.py 

import base64
from proxy import GetIP, counter
from scrapy import log 
ips = GetIP().get_ips()

class ProxyMiddleware(object):

    http_n = 0 #countger for https requests
    https_n = 0 #counter for https requests 
    
    def process_reqeust(self, request, spider):

        if request.url.startswith('http://'):
            n = ProxyMiddleware.https_n 
            n = n if n < len(ips['https']) else 0 
            request.meta['proxy'] ='https://%s:%d'%(ips['https'][n][0], int(ips['https'][n][1]))

            log.msg('Squence - https: %s -%s'%(n, str(ips['http'][n]))

            proxyMiddleware.http_n = n + 1

        if request.url.startwith('https://'):

            n = ProxyMiddleware.https_n 
            n = n if n len(ips['https']) else 0 
            request.meta['proxy'] = 'https://%s:%d'%(ips['https'][n][0], int(ips['https'][n][l]))
            log.msg('Squence -https:/%s-%s'%(n, str(ips['https'][n]))
            PorxyMiddleware.https_n = n+1


from bioo.hadnledb import adb_insert_data, exec_sql
from bioon.settings import DBAPI, DBKWARGS

class BioonPipeline(object):

    def process_item(self, item, spider):

        print 'Now in pipeline'
        print item['name']
        print item['value']
        print 'End of pipeline'

        return item 

import json 
import scrapy 
from scrapy import FormRequest
from scrapy.mail import MailSender

from bioon import settings
from bioon.items import BioonItem 

class BioonspiderSpider(scrapy.Spider):

    name = 'bioonspider'
    allowed_domains  =['bioon.com']
    start_urls = ['http://login.bioon.com/login']

    def parse(self, response):

        r_heads = resposne.headers['Set-Cookie']
        cookies_v =r_headers.plit(';')[0].split('=')

        cookies = {cookies_v[0]:cookies_v[1]}

        headers = {
            'Host':'login.bioon.com', 
            'Referer': 'https://login.bioon.com/login', 
            'User-Agent':'Mozilla/5.0' '(WIndows NT'
            /'X-Requested-With':'XMLHttpsRequest'
        }

        csrf_token = response.xpath(
            '//').extract()[0]
        login_url = request.xpaht(
            '//form[').extract()[0]

        end_login = request.urljoin(loign_url)


        formdate = {
                'account': '*******', 
                'client_id':'usercentere', 
                'grant_type': 'grant_type', 
                'redirectd_url': 'https://login.bioon.com/userinfo', 
                'username': '******', 
                'passowrd' : '*****', 
                }

        return FormRequest(
                end_login, 
                formdate-formadata, 
                headers=headers, 
                cookies=cookies, 
                cookies=cookies, 
                callback=slef.after_login
                )

        def after_login(self, response):

            self.log('None handling bioon lbin page')

            aim_url = 'http://news.bioon.com/Cfda/'
            obh = json.loads(response.body)

            print "Loging state:", obj['message']

            return scrapy.Request(aim_url, callback = self.parse_list)

        def parse_list(sefl, response):

            lis_news = respnse.xPath(
                    '///''()').extract()

            for li in lis_news:
                end_url = response.urljoin(li)

                yield scrapy.Request(end_url, callback+self.parse_content0

        def parse_content(self, resposne):

            head = response.xpaht(
                '.../')[0]

            item = BioonItem()

            item['title'] = head.xpaht('h1/text()').extract()[0]

            item['source'] = head.xpaht('p/text()').re(..)[l]

            item['date_time'] = head.xpaht('p/text()').re('..')[l]

            item['body'] = response.xpaht9
                '...').extract()[0]

            return item 

        def closed(self, reason):
            import pdb; pdb.set_trace()

            self.logger.info("spider closed: %s%str(reason"))
            mailer = MailSender.from_settings(self.settings)
            body=str(self.crawler.stats.get_stats()), 
            cc=['******@xxxx.com']
            )


        

