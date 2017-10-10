# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #文章标题
    title = scrapy.Field()
    #文章作者
    author = scrapy.Field()
    #文章发布时间
    time = scrapy.Field()
    #评论数
    comment = scrapy.Field()
    #阅读数
    read_num = scrapy.Field()
    #文章内容
    content = scrapy.Field()

    # 获取UTC时间
    crawled = scrapy.Field()
    # 爬虫名
    spider = scrapy.Field()
