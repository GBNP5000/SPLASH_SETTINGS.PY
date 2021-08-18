import scrapy
from scrapy_splash import SplashRequest
# from scrapy.crawler import CrawlerProcess

class GpSpider(scrapy.Spider):
    name = 'gp'

    def start_requests(self):
        url = ''
        yield SplashRequest(url)

    def parse(self, response):
        yield {
                '': response.css('::()').get(),
       }


# process = CrawlerProcess()
# process.crawl(GpSpider)
# process.start()
