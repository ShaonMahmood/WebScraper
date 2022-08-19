import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.ebay.com']
    start_urls = ['http://www.ebay.com/']

    def parse(self, response):
        pass
