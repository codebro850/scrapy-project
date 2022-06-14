# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import settings
from scrapy.exceptions import DropItem
# from scrapy import log

from collections import defaultdict
class MongoDBPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
            "localhost",
            27017
        )
        self.db = connection["scrawled"]
        self.collection_name = self.db["classes"]
    

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            
            self.db["classes"].insert_one(dict(item))
                # log.msg("Question added to MongoDB database!",
                #         level=log.DEBUG, spider=spider)
        return item
  
