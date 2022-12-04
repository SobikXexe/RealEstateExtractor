from scrapy.crawler import CrawlerProcess
import web_scraper.spiders.sreality as sp

if __name__ == "__main__":


    process = CrawlerProcess()
    
    process.crawl(sp.SrealitySpider)
    process.start()