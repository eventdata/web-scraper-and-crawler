from newspaper import Article
from pymongo import MongoClient
import urllib
from NewspaperTextExtractor import NewspaperTextExtractor
import requests


issue_count = 0
article_count = 0

extractor = NewspaperTextExtractor(language="es")


response = requests.get("http://caracol.com.co/emisora/2017/09/08/sincelejo/1504868022_942997.html")

print response.content

article = extractor.extractAll(response.content)

# article = Article("http://caracol.com.co/emisora/2017/10/27/bogota/1509106310_741399.html", language="es")
#
# article.download()
#
# article.parse()
print type(response)

if article.publish_date is  None:
    print "Date missing"
else:
    print article.publish_date



print "Number of Issues", str(issue_count)