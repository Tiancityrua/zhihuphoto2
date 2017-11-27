# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from zhihuphoto1 import settings
class Zhihuphoto1Pipeline(object):
    def process_item(self, item, spider):
        if 'imageurls' in item:
            images=[]

            for imageurl in item['imageurls']:
                us=imageurl[28:38]
                imagefilename=us+'.jpg'
                filepath='%s/%s' % ('/home/tian/PycharmProjects/zhihuphoto1/zhihuphoto1/photo', imagefilename)
                images.append(filepath)
                if os.path.exists(filepath):
                    continue
                with open(filepath,'wb') as handle:
                    response=requests.get(imageurl).content
                    handle.write(response)