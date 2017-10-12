

import json
from StringIO import StringIO
import sys
from time import sleep

from kafka.producer.kafka import KafkaProducer

import Util


reload(sys)
sys.setdefaultencoding('utf8')
producer = KafkaProducer(bootstrap_servers='dmlhdpc1')
duration = [0, 480, 480, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
input_file = open("/Users/sxs149331/Desktop/window_all_sgml.txt")
count = 0
dur_index = 0
for line in input_file:
    count = count + 1
    if line.startswith("#"):
        sleep(duration[dur_index])
        dur_index = dur_index + 1
        print "Sending Window Marker"
        producer.send("petrarch", line.encode('utf-8'))
    else:
        producer.send("test", line.encode('utf-8'))
        print "Sent "+str(count)



print count
input_file.close()




