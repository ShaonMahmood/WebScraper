from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from web_crawler.spiders.products import ProductsSpider 
 

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(ProductsSpider)
    process.start()