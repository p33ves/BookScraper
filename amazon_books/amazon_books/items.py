# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary containers (items) -> Storing in database

import scrapy


class AmazonBooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    binding = scrapy.Field()
    current_price = scrapy.Field()
    listed_price = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
