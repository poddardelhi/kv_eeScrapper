# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KvScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    description = scrapy.Field()
    link=scrapy.Field()
    no_rooms = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    per_m_sq = scrapy.Field()
    name = scrapy.Field()

    pass
