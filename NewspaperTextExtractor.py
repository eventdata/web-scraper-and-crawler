
from newspaper import Article


class NewspaperTextExtractor:
    
    article_lang = "en"
    
    def __init__(self, language="en"):
        self.article_lang = language
    
    def extract(self, raw_html):
        article  = Article("http://www.dummy.com", language=self.article_lang)
        article.set_html(raw_html)
        article.parse()
        
        
        return article.text, article.title
    
    def extractAll(self, raw_html):
        article  = Article("http://www.dummy.com", language=self.article_lang)
        article.set_html(raw_html)
        article.parse()
        
        
        return article
        
 
            
        
        