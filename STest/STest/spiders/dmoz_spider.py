import scrapy

from STest.items import DomzItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://www.w3school.com.cn/"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            '''
            item = DomzItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
            '''
            res = sel.xpath('//p').extract()
            if len(res) > 0:print res[0]
            #if len(res) > 0:print res[0]
            #print sel.xpath('a/text()').extract()
            #print sel.xpath('a/@href').extract()
            #print sel.xpath('text()').extract()
