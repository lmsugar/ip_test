# -*- coding: utf-8 -*-
import scrapy


class IpGetXiciSpider(scrapy.Spider):
    name = 'ip_get_xici'
    allowed_domains = ['http://www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        pass
