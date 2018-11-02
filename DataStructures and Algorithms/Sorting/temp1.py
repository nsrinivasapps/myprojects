#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:29:21 2018

@author: shrinivaass
"""
import numpy
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
    
import numpy as np
q = np.array([1,2,3], float)
print q
print q[:, np.newaxis]
print q[np.newaxis,:]

a3 = np.array([[0,2],[3,-1],[3,5]], float)
print(a3.mean(axis=1)) 

a4 = np.array([1,3,0], float)
#print np.where(a4!=0, 1/a4 ,a4)


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:03:44 2018

@author: shrinivaass
"""

A=[1,2,3,4]
print A
swap(A,1,3)
print A

s1=[2,3,4]
s2=[7,6,6]
print s1+s2+[120]

print 123/1000

x1=[1,2,3]
x2=[[2,3,4],[4,3,4],[3,6,7]]
inputs = numpy.array(x1, ndmin=2).T
print inputs
print x2
print numpy.dot(x2,inputs)
    
