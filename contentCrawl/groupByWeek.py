from dateutil import parser
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["scrapedContent"]
collection = db["content"]
collection2 = db["groupByWeek"]

contents = []

for item in collection.find():
    contents.append(item)

grouped = {}
keys = set()
for content in contents:
    date = parser.parse(content['date'])
    key = tuple(date.isocalendar()[:2]).__str__()
    keys.add(key)
    grouped.setdefault(key, []).append(content)

for key in keys:
    collection2.insert_one(dict({
        key: grouped[key]
    }))

client.close()
