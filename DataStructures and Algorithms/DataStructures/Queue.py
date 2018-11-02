#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:21:56 2018

@author: shrinivaass
"""

import random

class Queue(object):
    def __init__(self,limit=10):
        self.items=[]
        self.tail = 0
        self.head = 0
        self.size=0
        self.limit=10

    def isEmpty(self):
        if self.head == self.tail or self.size <= 0:
            return True
        else:
            return False
        
    def isFull(self):
        if self.head == self.tail+1 or self.size >= self.limit:
            return True
        else:
            return False        
        
    def enQueue(self,element):
        if self.isFull():
            print "Overflow"
            return
        self.items.append(element)
        self.tail +=1
        self.size +=1
        
    def deQueue(self):
        print self.head,self.items[self.head]       
        if self.isEmpty():
            print "Underflow"
            return
        item = self.items[self.head]
        #del self.items[self.head]
        self.items[self.head] = None
        self.head += 1
        self.size -=1
        print self.head
        return item
    

if __name__ == '__main__':
    print 'main'
    #print random.randint(1,1000)
    q=Queue()
    for i in range(10):
        q.enQueue(random.randint(1,1000))
    print q.items
    print q.deQueue()
    print q.items
    q.enQueue(random.randint(1,1000))
    print q.items
    q.enQueue(random.randint(1,1000))
    print q.deQueue()
    q.enQueue(random.randint(1,1000))
    print q.items
    for i,j in enumerate(q.items):
        print i,j
    print q.items        
    lst2 = []
    while not q.isEmpty():
        lst2.append(q.deQueue())
        print q.items
    print lst2