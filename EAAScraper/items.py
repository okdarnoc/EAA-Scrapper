# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EaascraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    licenceNo = scrapy.Field()
    name = scrapy.Field()
    businessName = scrapy.Field()
    effectiveDate = scrapy.Field()
    expiryDate = scrapy.Field()
    relatedLicence = scrapy.Field()
    disciplinarySearch = scrapy.Field()
    condition = scrapy.Field()


    
