# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from cnblog.items import CnblogItem
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule



#class CnblogsSpider(CrawlSpider):
class CnblogsSpider(RedisCrawlSpider):
    name = 'cnblogs'
    allowed_domains = ['www.cnblogs.com']
    #start_urls = ['https://www.cnblogs.com/']
    redis_key = "cnblogs:start_urls"

    

    #第一层页面
    page_1x = LinkExtractor(allow=(r"sitehome/p/\d+"))
    #第二层页面
    page_2x = LinkExtractor(allow=(r"www.cnblogs.com/\S+/p/\d+.html$"))

    rules = (
        Rule(page_1x),
        Rule(page_2x,callback='parse_page',follow=False)
        )
    def parse_page(self,response):
        
        item = CnblogItem()
        item['title'] = response.xpath('//h1[@class="postTitle"]/a/text()').extract()
        item['author'] = response.xpath('//div[@class="postDesc"]/a[1]/text()').extract()
        item['time'] = response.xpath('//div[@class="postDesc"]/span[@id="post-date"]/text()').extract()
        item['comment'] = response.xpath('//div[@class="postDesc"]/span[@id="post_comment_count"]/text()').extract()
        item['read_num'] = response.xpath('//div[@class="postDesc"]/span[@id="post_view_count"]/text()').extract()
        item['content'] = response.xpath('//div[@id="cnblogs_post_body"]//p/text()').extract()
        yield item
        
