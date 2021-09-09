import scrapy
import re
import datetime
import pymongo


class CrawlSpider(scrapy.Spider):
    name = 'dtSpider'
    custom_settings = {'FEED_EXPORT_ENCODING': 'utf-8'}
    start_urls = []
    begin_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["scrapedLink"]
    collection = db["link"]

    for item in collection.find():
        link = item['link']
        start_urls.append(link)

    def __init__(self):
        super(CrawlSpider, self).__init__()
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['scrapedContent']
        self.collection = db['content']

    def parse(self, response):
        # Get date from article
        date_extract = response.css('span.date ::text').get()
        match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', date_extract)
        date = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()

        # Check date
        if self.end_date >= date >= self.begin_date:
            title = response.css('h1.title-detail ::text').get()
            desc = ""
            for text in response.css('p.description ::text'):
                desc = desc + text.get() + " "

            # Check article type (photo article or text article)
            if response.css('section.section.page-detail.detail-photo').get():
                # Photo article
                items = []
                for itm in response.css('article.fck_detail div.item_slide_show'):
                    image = itm.css('div.block_thumb_picture picture source ::attr(data-srcset)').get()
                    img_desc = ""
                    for p in itm.css('div.desc_cation p.Normal ::text'):
                        img_desc = img_desc + p.get() + " "

                    item = {
                        'image': image,  # a set of 2 images NOT 1 image link
                        'image description': img_desc
                    }
                    items.append(item)

                content = {
                    'title': title,
                    'summary': desc,
                    'article': items,
                    'date': date.strftime("%Y/%m/%d")
                }
                self.collection.insert(dict(content))

            else:
                # Text article
                image = response.css('div.fig-picture picture source ::attr(data-src)').get()
                article = ""
                for p in response.css('article.fck_detail p.Normal ::text'):
                    article = article + p.get() + " "

                content = {
                    'title': title,
                    'summary': desc,
                    'image': image,  # only 1 image link
                    'article': article,
                    'date': date.strftime("%Y/%m/%d")
                }
                self.collection.insert(dict(content))
