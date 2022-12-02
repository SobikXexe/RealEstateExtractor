import scrapy
from scrapy_splash import SplashRequest
import requests

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    base_url = 'https://www.sreality.cz/'
    relative_address = 'hledani/prodej/byty'
    start_urls = ['https://www.sreality.cz/']

    lua_script = """
        function main(splash)
            splash:set_result_content_type("text/html; charset=utf-8")
            assert(splash:go(splash.args.url))
            assert(splash:set_content("<html><body><h1>hello</h1></body></html>")
            return "AHA"
        end
        """

    def __init__(self) -> None:
        super().__init__()

    def start_requests(self):

        return [SplashRequest(url=self.base_url + self.relative_address, callback=self.parse,
                                endpoint="execute",
                                args={"lua_source": self.lua_script},
                                dont_filter=True)]


    def parse(self, response):
        print(response.text)
        pass

    # def prepare_for_splash(self, html : str) -> str:
    #     return html.replace('<head>', '<head><base href="https://www.sreality.cz/" /><script>window.location.assign("https://www.sreality.cz/hledani/prodej/byty")</script>')
        
