from newspaper import Article
from pymongo import MongoClient
import urllib

from multiprocessing import Pool

MONGO_PORT = "3154"
MONGO_USER = "event_reader"
MONGO_PSWD = "dml2016"
MONGO_SERVER_IP = "172.29.100.8"
MONGO_PORT = "3154"

MONGO_COLLECTION = "articles_es"
password = urllib.quote_plus(MONGO_PSWD)
mongo_client = MongoClient('mongodb://' + MONGO_USER + ':' + password + '@' + MONGO_SERVER_IP + ":" + MONGO_PORT)

db = mongo_client.event_scrape

articles = db.articles_es.find({})

issue_file = open("es_articles.txt", "a+")

issue_count = 0
article_count = 0


def update_article(mongo_article):
    global issue_file
    global issue_count

    article = Article(mongo_article["url"], language="es")

    article.download()

    article.parse()

    if article.publish_date is not None:
        db.articles_es.update({"_id": mongo_article["_id"]}, {"$set": {"pub_date": article.publish_date}})

    else:
        issue_str = str(mongo_article["_id"]) + " " + (mongo_article["url"]) + ": " + mongo_article["title"]
        issue_file.write(issue_str.encode("utf-8") + "\n")
        issue_count += 1


process_pool = Pool(5)

process_pool.map(update_article, articles)

process_pool.join()

issue_file.close()

print "Number of Issues", str(issue_count)