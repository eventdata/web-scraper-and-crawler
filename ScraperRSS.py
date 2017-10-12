from scrapy.settings import Settings
from scrapy.spiders import XMLFeedSpider
from  NewspaperTextExtractor import NewspaperTextExtractor
from pymongo.mongo_client import MongoClient
import scrapy
from scrapy.crawler import CrawlerProcess, Crawler

from RSSItem import RSSItem


class RSSSpider(XMLFeedSpider):
    name = 'RSS Feed Collector'
    start_urls = []
    visited_urls = {}
    iterator = 'xml'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    articleProcessor = NewspaperTextExtractor(language="en")
    #mongo_client = MongoClient(host="dmlhdpc10")
    logger_file = open('logs.txt', "w+")
    def __init__(self, name=None, **kwargs):
        XMLFeedSpider.__init__(self, name=name, **kwargs)
        whitelistFile = open('whitelist_urls_test.csv')
        for line in whitelistFile:
            feed_url = line.split(',')[1]
            self.start_urls.append(feed_url)
            self.visited_urls[feed_url] = {}

        self.logger_file.write("Started")

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
        #self.logger_file.write(''.join(node.extract()))
        self.logger_file.write('FOUND')
        article_url = node.select('link/text()').extract()[0]
        #self.logger.info(article_url)
        feed_url = response.url
        if article_url in self.visited_urls[feed_url]:
            self.logger.info("Duplicate Entry Found")
        else:
            yield scrapy.Request(article_url, callback=self.process_article)

    def process_article(self, response):
        self.logger.info(response.body)





process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

process.crawl(RSSSpider)

process.start()


