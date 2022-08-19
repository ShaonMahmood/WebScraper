import scrapy
from web_crawler.items import EbayProductItem
from web_crawler.settings import EBAY_SEARCH_ITEM, EBAY_URL

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.ebay.com']
    start_urls = [EBAY_URL]


    def __init__(self, search="lg tv 43"):
        self.search_string = EBAY_SEARCH_ITEM or search

    def parse(self, response):
        # Extrach the trksid to build a search request	
        trksid = response.css("input[type='hidden'][name='_trksid']").xpath("@value").extract()[0]       
		
		# Build the url and start the requests
        yield scrapy.Request("http://www.ebay.com/sch/i.html?_from=R40&_trksid=" + trksid +
							 "&_nkw=" + self.search_string.replace(' ','+') + "&_ipg=200", 
							 callback=self.parse_link)

        # yield scrapy.Request("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?rt=nc&_dmd=1",
        #                      callback=self.parse_link)


    # Parse the search results
    def parse_link(self, response):
		# Extract the list of products 
        results = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')

        # Extract info for each product
        for product in results:		
            name = product.xpath('.//*[@class="s-item__title"]//text()').extract_first()
            # Sponsored or New Listing links have a different class
            if name == None:
                name = product.xpath('.//*[@class="s-item__title s-item__title--has-tags"]/text()').extract_first()			
                if name == None:
                    name = product.xpath('.//*[@class="s-item__title s-item__title--has-tags"]//text()').extract_first()			
            if name == 'New Listing':
                name = product.xpath('.//*[@class="s-item__title"]//text()').extract()[1]

            # If this get a None result
            if name == None:
                name = "ERROR"

            price = product.xpath('.//*[@class="s-item__price"]/text()').extract_first()
            product_url = product.xpath('.//a[@class="s-item__link"]/@href').extract_first()

            item = EbayProductItem()

            item['product_name'] = name
            item['price'] = price
            item['product_url'] = product_url
            yield item

        # Get the next page
        next_page_url = response.xpath('//*/a[@class="x-pagination__control"][2]/@href').extract_first()

		# The last page do not have a valid url and ends with '#'
        if next_page_url == None or str(next_page_url).endswith("#"):
            self.log("eBay products collected successfully")
        else:
            print('\n'+'-'*30)
            print('Next page: {}'.format(next_page_url))
            yield scrapy.Request(next_page_url, callback=self.parse_link)
