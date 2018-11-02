#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:00:24 2018

@author: shrinivaass
"""

import random

class Stack(object):
    def __init__(self):
        self.items=[]
        self.top = -1

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False
        
    def push(self,element):
        self.top +=1
        self.items.append(element)
        
    def pop(self):        
        if self.isEmpty():
            print "underflow"
        else:
            item = self.items[self.top]
            del self.items[self.top]
            self.top -= 1
            return item
        
   
        

if __name__ == '__main__':
    print 'main'
    #print random.randint(1,1000)
    s=Stack()
    for i in range(10):
        s.push(random.randint(1,1000))
    print s.items
    print s.top
    print s.pop()
    print s.top
    print s.items
    s.push(random.randint(1,1000))
    print s.items
    lst2 = []
    while not s.isEmpty():
        lst2.append(s.pop())
    print lst2        
    
        
            