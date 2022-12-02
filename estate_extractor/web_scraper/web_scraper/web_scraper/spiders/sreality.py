import scrapy
from scrapy_playwright.page import PageMethod
class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    _base_url = 'https://www.sreality.cz/'
    _relative_address = 'hledani/prodej/byty'
    properties_count = 0


    def start_requests(self):

        yield scrapy.Request(self._base_url + self._relative_address,
                            callback=self.parse,
                            meta={"playwright": True
                                })


    async def parse(self, response):
        title : str
        img : str
        for item in response.css('div.property.ng-scope'):
            self.properties_count += 1
            title = item.css('span.name.ng-binding::text').get()
            print(title)
        print(self.properties_count)

        
