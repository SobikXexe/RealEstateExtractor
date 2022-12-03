import scrapy
from scrapy_playwright.page import PageMethod

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    _base_url = 'https://www.sreality.cz/'
    _relative_address = 'hledani/prodej/byty'
    properties_count = 0
    items : list[list[str, str]]
    strana : int

    custom_settings = {
        'BOT_NAME' : 'web_scraper',
        'SPIDER_MODULES' : ['web_scraper.spiders'],
        'NEWSPIDER_MODULE' : 'web_scraper.spiders',
        'DOWNLOAD_HANDLERS' : {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        'TWISTED_REACTOR' : "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        'ROBOTSTXT_OBEY' : False,
        'REQUEST_FINGERPRINTER_IMPLEMENTATION' : '2.7',
        'TWISTED_REACTOR' : 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
        'LOG_ENABLED' : False
    }


    def start_requests(self):
        self.items = []
        self.strana = 1
        yield scrapy.Request(self._base_url + self._relative_address,
                            callback=self.parse,
                            meta={  "playwright": True,
                                    "playwirgth_page_methods": [PageMethod("wait_for_selector", "div.property.ng-scope"),
                                                                PageMethod("wait_for_selector", "span.name.ng-binding::text"),
                                                                PageMethod("wait_for_selector", "div.property.ng-scope img::attr(src)")]
                                })


    async def parse(self, response):
        for item in response.css('div.property.ng-scope'):
            if len(self.items) < 500:
                self.properties_count += 1
                title = item.css('span.name.ng-binding::text').get()
                img = item.css('img::attr(src)').get()
                self.items.append([title, img])
        if len(self.items) < 500:
            print(len(self.items))
            self.strana += 1
            yield scrapy.Request(self._base_url + self._relative_address + "?strana=" + str(self.strana),
                            callback=self.parse,
                            meta={  "playwright": True,
                                    "playwirgth_page_methods": [PageMethod("wait_for_selector", "div.property.ng-scope"),
                                                                PageMethod("wait_for_selector", "span.name.ng-binding::text"),
                                                                PageMethod("wait_for_selector", "div.property.ng-scope img::attr(src)")]
                                })
        else:
            print(self.items)

    
