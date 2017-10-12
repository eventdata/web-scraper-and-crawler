'''
Created on Sep 8, 2016

@author: sxs149331
'''
from Queue import Queue

class ObjectPool(object):
    '''
    classdocs
    '''
    
    type = ''

    def __init__(self):
        '''
        Constructor
        '''
    
    def wrap(self, objList=[]):
        self.queue = Queue(maxsize=len(objList))
        for obj in objList:
            self.queue.put_nowait(obj)
            self.type = type(obj)
    
    def take(self):
        print "GETTING OBJECT"
        
        print self.queue.qsize()
        return self.queue.get()
    
    def give_back(self, obj):
        if self.type == type(obj):
            self.queue.put_nowait(obj)
        else:
            raise Exception("Type Mismatch")    