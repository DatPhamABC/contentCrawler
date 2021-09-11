from scrapy.crawler import CrawlerProcess
from contentCrawl.spiders.DetailCrawl import CrawlSpider

process = CrawlerProcess()

process.crawl(CrawlSpider)
process.start()