# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Restaurant(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    tag1 = scrapy.Field()
    tag2 = scrapy.Field()
    tag3 = scrapy.Field()
    street = scrapy.Field()
    postcode = scrapy.Field()
    tele = scrapy.Field()
    date_accessed = scrapy.Field()
