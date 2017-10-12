from datastore import KafkaDataSink
from objectpool import ObjectPool
 
kafkaObjects = []
for i in range(10):
    obj1 = KafkaDataSink.KafkaDataSink(host="dmlhdpc1", topic="test")
    kafkaObjects.append(obj1)
 
print len(kafkaObjects)
     
kafkaPool = ObjectPool.ObjectPool()
kafkaPool.wrap(kafkaObjects)
 
print "OBJECT ADDED"
obj1 = kafkaPool.take()
obj2 = kafkaPool.take()
 
print "OBJECT TAKEN"
 
obj1.send("TEST")
obj2.send("TEST2")
 
kafkaPool.give_back(obj1)
kafkaPool.give_back(obj2)