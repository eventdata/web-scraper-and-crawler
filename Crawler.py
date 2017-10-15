import json
import urllib

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item
from NewspaperTextExtractor import NewspaperTextExtractor
from newspaper.article import Article

from pymongo.mongo_client import MongoClient



class SpanishSpider(scrapy.Spider):
    name = "Spanish News Article Spider"
    allowed_domains = ['caracol.com.co']
    
    
    start_urls = ['http://caracol.com.co']
    
    linkExtractor = LinkExtractor()
    articleProcessor = NewspaperTextExtractor(language="es")
    MONGO_PORT = "3154"
    MONGO_USER = "event_reader"
    MONGO_PSWD = "dml2016"
    MONGO_SERVER_IP = "172.29.100.8"
    MONGO_PORT = "3154"

    MONGO_COLLECTION = "articles_es"
    password = urllib.quote_plus(MONGO_PSWD)
    mongo_client = MongoClient('mongodb://' + MONGO_USER + ':' + password + '@' + MONGO_SERVER_IP + ":" + MONGO_PORT)
    
    def __init__(self):
        self.db = self.mongo_client.event_scrape
        self.__load_info()


    def __load_info(self):
        entries = json.load(open("crawl_list.json","r"))
        self.allowed_domains = []
        self.start_urls = []
        for e in entries:
            self.start_urls.append(e['start_url'])
            self.allowed_domains.append(e['domain'])

        print "Loading Complete. List of website to crawl"
        print self.start_urls

        
    
    def parse(self, response):
        article= self.articleProcessor.extractAll(response.body)
        print article.title
        
        self.db.articles_es.insert(
                                {
                                 "title": article.title, 
                                 "pub_date:":article.publish_date, 
                                 "url":response.url,
                                 "content": article.text
                                })
        
        links = self.linkExtractor.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
        
    
 
 
 
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

process.crawl(SpanishSpider)

process.start()

   
                       
