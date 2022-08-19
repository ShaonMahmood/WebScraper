# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sys
import pymongo
from itemadapter import ItemAdapter
from .items import EbayProductItem


class WebCrawlerPipeline:

    def __init__(self, mongodb_host, mongodb_port, mongodb_db, mongodb_collection):
        self.mongodb_host = mongodb_host
        self.mongodb_port = mongodb_port
        self.mongodb_db = mongodb_db
        self.mongodb_collection = mongodb_collection
        if not self.mongodb_host: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_host=crawler.settings.get('MONGO_HOST'),
            mongodb_port=crawler.settings.get('MONGO_PORT'),
            mongodb_db=crawler.settings.get('MONGO_DB_NAME'),
            mongodb_collection=crawler.settings.get('MONGO_COLLECTION_NAME'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_host, self.mongodb_port)
        self.db = self.client[self.mongodb_db]
        # Start with a clean database
        self.db[self.mongodb_collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(EbayProductItem(item))
        self.db[self.mongodb_collection].insert_one(data)
        return item
