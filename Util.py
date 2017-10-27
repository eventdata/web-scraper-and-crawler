import datetime
import os
import urllib2
import pattern.web
import shelve

counter_map={}
batch_counter_map = {}

current_datestr = ""

def create_doc_id_batch(document):
    date_string = document["date_added"].strftime('%Y%m%d')
    if date_string not in batch_counter_map:
        batch_counter_map[date_string] = {}
    source_map = batch_counter_map[date_string]
    if document["source"] not in source_map:
        source_map[document["source"]] = 1
    counter_str = "%04d" % source_map[document["source"]]
    source_map[document["source"]] = source_map[document["source"]] + 1
    return document["source"] + date_string + "." + counter_str


def create_doc_id(document):


    global current_datestr
    date_string = document["date_added"].strftime('%Y%m%d')

    if current_datestr != date_string:
        current_datestr = date_string
        counter_map.clear()

    if counter_map.get(document["source"], 1) == 1:
        counter_map[document["source"]] =  1

    counter_str = "%04d" % counter_map[document["source"]]

    counter_map[document["source"]] = counter_map[document["source"]] + 1



    return document["source"]+date_string +"."+counter_str


def convert_to_SGML(document):

    sgml_buf = "<DOC id=\""+create_doc_id(document)+"\" type=\"story\">"
    sgml_buf = sgml_buf+  "<HEADLINE>"+document["title"]+"</HEADLINE>"
    sgml_buf = sgml_buf+ "<DATELINE>"+ str(document["date"])+"</DATELINE>"
    sgml_buf = sgml_buf+ "<TEXT>"+document["content"]+"</TEXT></DOC>"

    return sgml_buf

def json_toSGML(document):
    sgml_str = "<DOC id=\""+document['doc_id']+"\" type=\"story\">"
    sgml_str = sgml_str + "<HEADLINE>"+document["head_line"]+"</HEADLINE>"
    sgml_str = sgml_str + "<DATELINE>" + document["date_line"] + "</DATELINE>"
    sgml_str = sgml_str + "<TEXT>"

    for sentence in document['sentences']:
        sgml_str = sgml_str + sentence['sentence'] + " "
    sgml_str = sgml_str + "</TEXT></DOC>"
    return sgml_str


if __name__ == '__main__':
    document = {"_id":1234, "language":"english","title":"Sample Title", "date_added":datetime.datetime.utcnow(),"content":"Sample TEXT all over again" , "source":"AFP" }

    print create_doc_id(document)

    results = pattern.web.Newsfeed().search("http://www.potatopro.com/rss-all-news-spanish", count=100,
                                                cached=False, timeout=30)
    print results

    urllib2.urlopen("http://www.typicallyspanish.com/news-spain/national_rss.xml")

    print "Success"