#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:27:32 2018

@author: shrinivaass
"""

def countingSort(A,maxValue):
    n=len(A)
    B=[0 for i in A]
    C=[0 for i in range(maxValue)]
    print len(C)
    print B
    for i in range(n):
        C[A[i]] += 1
    
    for i in range(1,len(C)):
        C[i] = C[i] + C[i-1]       
    #print C

    for j in range(n-1,-1,-1):
        print j,A[j],C[A[j]]
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
        print B
        
    return B        
        


A=[534, 246, 933, 127, 277, 321, 454, 565, 220]
#print A
B=countingSort(A,1000)
#print B        