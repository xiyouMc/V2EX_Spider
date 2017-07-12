# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class V2ExItem(Item):
    author_url = Field()
    author_avatar_url = Field()
    article_url = Field()
    article_title = Field()
    node = Field()
    node_url = Field()
    author_name = Field()
    last_reply_name = Field()
    last_reply_url = Field()
    last_reply_time = Field()
