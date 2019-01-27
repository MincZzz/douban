# -*- coding: utf-8 -*-
import pymongo
from douban.settings import mongodb_host, mongodb_port, mongodb_db_name, mongodb_db_collection


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        host = mongodb_host
        port = mongodb_port
        dbname = mongodb_db_name
        collection = mongodb_db_collection

        client = pymongo.MongoClient(host=host, port=port)
        self.post = client[dbname][collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
