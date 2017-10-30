from newspaper import Article
from pymongo import MongoClient
import urllib
from NewspaperTextExtractor import NewspaperTextExtractor
import requests
import scrapy
from time import sleep


url = "http://caracol.com.co/radio/2017/05/22/nacional/1495474619_093166.html"

issue_count = 0
article_count = 0

extractor = NewspaperTextExtractor(language="es")

def parse(response):
    print type(response)
    # print response.body
    article = Article(url=response.url, language="es")
    article.set_html(response.body)
    # article = self.articleProcessor.extractAll(response.body)
    print article.title
    print article.publish_date
    print response.url

scrapy.Request(url, callback=parse)

response = requests.get("http://caracol.com.co/radio/2017/05/22/nacional/1495474619_093166.html")

#print response.content

article = extractor.extractAll(response.content)

article = Article("http://caracol.com.co/radio/2017/05/22/nacional/1495474619_093166.html", language="es")


article.set_html(response.content)

article.parse()
print type(response)

if article.publish_date is None:
    print "Date missing"
else:
    print article.publish_date

sleep(5)



print "Number of Issues", str(issue_count)