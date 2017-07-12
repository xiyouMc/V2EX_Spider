# coding:utf-8

from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from V2EX.items import V2ExItem


class Spider(CrawlSpider):
    name = 'v2exSpider'
    host = 'https://www.v2ex.com'
    start_urls = ['https://www.v2ex.com/']

    def parse(self, response):
        print 'xxxxxxxxxxxxxxx=====================>'
        selector = Selector(response)
        divs = selector.xpath("//div[@class='cell item']")
        print len(divs)
        for div in divs:
            v2Item = V2ExItem()
            '''
            用户地址
            '''
            author_url = div.xpath(
                'table/tr/td[@align="center"]/a/@href').extract_first()
            v2Item['author_url'] = self.host + author_url
            '''
            头像地址
            '''
            author_avatar_url = div.xpath(
                'table/tr/td[@align="center"]/a/img/@src').extract_first()
            v2Item['author_avatar_url'] = 'http:' + author_avatar_url
            '''
            文章地址
            '''
            article_url = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="item_title"]/a/@href'
            ).extract_first()
            v2Item['article_url'] = self.host + article_url
            '''
            文章标题
            '''
            article_title = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="item_title"]/a/text()'
            ).extract()
            v2Item['article_title'] = article_title
            '''
            所属节点    
            '''
            node = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="small fade"]/a/text()'
            ).extract()
            v2Item['node'] = node
            '''
            节点地址
            '''
            node_url = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="small fade"]/a/@href'
            ).extract_first()
            v2Item['node_url'] = self.host + node_url
            '''
            作者昵称 和 回复者昵称
            '''
            names = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="small fade"]/strong/a/text()'
            ).extract()
            print names
            author_name = names[0]
            v2Item['author_name'] = author_name
            if len(names) == 2:
                last_reply_name = names[1]
                v2Item['last_reply_name'] = last_reply_name
            '''
            作者地址 和回复者地址
            '''
            urls = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="small fade"]/strong/a/@href'
            ).extract()
            if len(urls) == 2:
                last_reply_url = urls[1]
                v2Item['last_reply_url'] = self.host + str(last_reply_url)
            '''
            最后一次回复的时间
            '''
            last_reply_time = div.xpath(
                'table/tr/td[@valign="middle"]/span[@class="small fade"]/text()'
            ).extract()
            v2Item['last_reply_time'] = last_reply_time
            yield v2Item