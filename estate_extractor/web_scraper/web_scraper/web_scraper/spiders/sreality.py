import scrapy


class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    def parse(self, response):
        pass
