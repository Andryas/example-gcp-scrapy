# -*- coding: utf-8 -*-
import scrapy

from src.settings import *
from src.utils.lubridate import now

class TestGCPSpider(scrapy.Spider):
    name = 'test_gcp'

    custom_settings = {
        'ITEM_PIPELINES': {
            'src.pipeline.JsonWriterPipeline': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'created_at': now(False),
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }

       

       