import scrapy 

class TopgoodItem(scrapy.Item):

    GOODS_PRICE = scrapy.Field()
    GOOD_NAME = scrapy.Field()
    GOOD_URL = scrapy.Field()
    SHOP_NAME = scrapy.Field()
    COMPANY_NAME = scrapy.Field()
    COMPANY_ADDRESS = scrapy.Field()



class TopgoodsPipeline(object):

    def process_item(self, item, spider):

        return item 

#pipelines.py

class TopgoodsPipeline(object):
    def process_item(self, item, spider):
        return item 


## tm_goods.py

import scrapy 
from topgoods.items import TopgoodsItem 

class TMGoodsSpider(scrapy.Spider):

    name = "tm_goods"
    allowed_domains = ['https://www.tmall.com']

    start_urls = ('
            https://list', 
            )
    count = 0 

    def parse(self, response):

        TmGoodsSpider.count += 1

        divs = response.xpath('....')

        if not divs:
            self.log("List Page error--%s"%response.url)

        for div in divs:
            item['GOO_PPRICE'] = div.xpath('...')
            item['GOOD_Name'] = div.xpaht('...')
            pre_goods_url = div.xpaht('...')

            item['GOODs_RUL'] = pre_goods_url if 'https' in pre_goods_url

            yield scrapy.Reqeust(url=item['GOOD_URL'], meta={'item':item},
                    callback=self.parse_detail , 
                    dont_filter=True)
    def parse_detail(self, response):

        div = response.xpath('//div[@class="extend"]/ul')

        if not div:
            self.log('Detail Page error---%s' %response.url)

        item = response.meta['item']

        item =response.meta['item'] 

        item['SHOP_NAME'] =div.xpath('li[1]/div/a/@href')[0].extract()

        yield item




