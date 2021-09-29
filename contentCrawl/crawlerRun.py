from scrapy.crawler import CrawlerProcess
from contentCrawl.spiders.DetailCrawl import CrawlSpider
import datetime

process = CrawlerProcess()

begin_date = datetime.date(2021, 9, 19)
end_date = datetime.date(2021, 9, 21)

process.crawl(CrawlSpider, begin_date, end_date)
process.start()
