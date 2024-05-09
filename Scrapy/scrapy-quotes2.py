from typing import Any
import scrapy
from scrapy.http import Response

class QuotesSpider(scrapy.Spider):
    name='QuotesSpider'
    start_urls = ['https://www.eletrogate.com/placas-arduino']

    def parse(self, response):
        list = response.xpath('*//li[@class="span4"]')
        
        for item in list:
            yield {
                'produto':item.xpath('.//li[@class="span4"]/div/div/a[@class="nome-produto cor-secundaria"]/text()').get(),
                'boleto':item.xpath('.//strong[@class="preco-promocional cor-principal titulo"]/text()').get()
            }


#        nextpage = response.xpath('*//li[@class="next"]/a/@href').get()
        
#        if nextpage is not None:
#            yield scrapy.Request(response.urljoin(nextpage), callback=self.parse)
        
            
            
