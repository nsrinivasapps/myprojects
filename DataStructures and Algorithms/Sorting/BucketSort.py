#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:10:19 2018

@author: shrinivaass
"""
import math
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
def insertionSort(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if A[j] < A[j-1]:
                swap(A,j,j-1)

def hashing(A):
    m=A[0]
    for i in range(len(A)):
        if m < A[i]:
            m=A[i]
    return [m,int(math.sqrt(len(A)))]

def rehashing(element,hashCode):
    return int((element/hashCode[0])*(hashCode[1]-1))      
        
def bucketSort(A):
    hashCode = hashing(A)
    print hashCode
    #print buckets
    buckets = [list() for _ in range(hashCode[1])]
    for i in A:
        x=rehashing(i,hashCode)
        print i,x
        buckets[x].append(i)
    print buckets
    
    for b in range(len(buckets)):
        insertionSort(buckets[b])
    print buckets        
    j=0   
    for b in range(len(buckets)):
        for i in buckets[b]:
            A[j] = i
            j+=1      
    

A=[534, 246, 933, 127, 277, 321, 454, 565, 220]
#print A
bucketSort(A) 
print A