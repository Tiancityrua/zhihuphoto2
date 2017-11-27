# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zhihuphoto1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imageurls=scrapy.Field()
    images=scrapy.Field()
