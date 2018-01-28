#!/usr/bin/env python3

from datetime import datetime as dt
from time import sleep

import scrapy
from bs4 import BeautifulSoup as bs

from EAAScraper.rangeGenerator import range_generator
from EAAScraper.items import EaascraperItem

class EAASpider(scrapy.Spider):
    name = "eaa"

    def __init__(self, *args, **kwargs):
        self.start_urls = ['http://www.eaa.org.hk/en-us/licence-search']
        self.download_delay = 2 # be a good netizen

    def parse(self, response):
        return self.brute_force(response)

    # use scrapy.FormRequest.from_response because the site requires hidden params from GET response
    def brute_force(self, response):
        for num in range_generator():
            yield scrapy.FormRequest.from_response(
            response,
            formdata={"dnn$ctr2496$LicenceSearch$btnLicenceSearch": 'Search', "dnn$ctr2496$LicenceSearch$txtLicNo":num },
            callback=self.extract
            )
            sleep(2)    # avoid too many requests taking up the RAM or hard disk swap

    def extract(self, response):
        # display number of pages crawled
        self.crawler.stats.inc_value('page_count')
        self.logger.info('Crawled %s ' % self.crawler.stats.get_stats()['page_count'])
        soup = bs(response.body.decode('utf-8'), 'html.parser')

        val = soup.find('input', {'id':"dnn_ctr2496_LicenceSearch_txtLicNo"})['value']
        if "No matching record(s) found." in response.body.decode('utf-8'):
            self.logger.info("No matching record(s) found for %s" % val)
            return

        # find the table containing the result
        table = soup.find('table', {'id':"dnn_ctr2496_LicenceSearch_gdvLicenceAndSPOBResult"})

        rows = table.find_all('tr')
        for row in rows:
            if 'class' not in row:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                # if row is not the header of the table and not empty
                if len(cols) >= 5:
                    
                    date = dt.strptime(cols[4], "%d/%m/%Y")
                    # get company if it is still registered
                    if date > dt.now():
                        item = {}
                        item['licenceNo'] = cols[0]
                        item['name'] = cols[1]
                        item['businessName'] = cols[2]
                        item['effectiveDate'] = cols[3]
                        item['expiryDate'] = cols[4]
                        item['relatedLicence'] = cols[5]
                        item['disciplinarySearch'] = cols[6]
                        item['condition'] = cols[7]

                        yield EaascraperItem(item)
        
        
