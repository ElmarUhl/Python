from typing import Any
import scrapy
from scrapy.http import Response

class QuotesSpider(scrapy.Spider):
    name='QuotesSpider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('*//div[@class="quote"]')
        
        for q in quotes:
            yield {
                'title':q.xpath('.//span[@class="text"]/text()').get(),
                'author':q.xpath('.//small[@class="author"]/text()').get(),
                'tags':q.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            }
            
        nextpage = response.xpath('*//li[@class="next"]/a/@href').get()
        
        if nextpage is not None:
            yield scrapy.Request(response.urljoin(nextpage), callback=self.parse)
        
            
            
