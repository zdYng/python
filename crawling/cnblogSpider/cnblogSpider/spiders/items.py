# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    #
    # file_urls = scrapy.Field()
    # files = scrapy.Field()
    #

    cimage_urls = scrapy.Field()
    cimages = scrapy.Field()
#创建CnblogspiderItem对象
# item = CnblogspiderItem(title="Python爬虫",content='爬虫开发')
# #获取字段的值
# print item['title']
# print item.get('title')
# #设置字段的值
# item['title'] = "爬虫"
# #获取所有的键和值
# print item.keys()
# print item.items()
#Item的复制
# item2 = CnblogspiderItem(item)
# item3 = item.copy()
# #dict与item的转化
# dict_item = dict(item)
# item = CnblogspiderItem({'title':'爬虫','content':'开发'})


# class newCnblogItem(CnblogspiderItem):
#     body =scrapy.Field()


