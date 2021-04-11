# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BcyItem(scrapy.Item):
    # define the fields for your item here like:

    #照片url
    urlid = scrapy.Field()


    jpg_name = scrapy.Field()


    file_name = scrapy.Field()

    biaoti = scrapy.Field()
    bcy_name = scrapy.Field()
    jpg_num = scrapy.Field()
    dz_num = scrapy.Field()







