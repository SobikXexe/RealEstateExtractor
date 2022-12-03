import scrapy
from scrapy.crawler import CrawlerProcess
import spiders.sreality as sp
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    # parser.add_argument(
    #     "-l",
    #     "--listen",
    #     default="localhost",
    #     help="Specify the IP address on which the server listens",
    # )
    # parser.add_argument(
    #     "-p",
    #     "--port",
    #     type=int,
    #     default=9091,
    #     help="Specify the port on which the server listens",
    # )
    # args = parser.parse_args()
    # run(addr=args.listen, port=args.port)

    process = CrawlerProcess()
    
    process.crawl(sp.SrealitySpider)
    process.start()