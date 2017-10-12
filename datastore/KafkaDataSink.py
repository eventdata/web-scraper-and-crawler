'''
Created on Sep 8, 2016

@author: sxs149331
'''
from datastore.DataSink import DataSink
from kafka.client import KafkaClient
from kafka.producer.simple import SimpleProducer
from kafka.producer.kafka import KafkaProducer

class KafkaDataSink(DataSink):
    '''
    classdocs
    '''
   

    def __init__(self, host="localhost", port=9092, topic="test"):
        '''
        Constructor
        '''
        #kafka = KafkaClient(host+':'+str(port))
        self.producer = KafkaProducer(bootstrap_servers=host)
        #self.producer = SimpleProducer(self.kafka)
        self.topic = topic
        
    def send(self, data):
        return self.producer.send(self.topic, data).get()