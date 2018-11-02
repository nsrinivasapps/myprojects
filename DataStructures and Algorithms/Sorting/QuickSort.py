#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:41:45 2018

@author: shrinivaass
"""

import sys
sys.setrecursionlimit(10000)
import random

def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


    
def partitionRand(A,start,stop):
    i=start-1
    pivot = random.randint(start,stop)
    swap(A,pivot,stop)
    pivotElement=A[stop]
    for j in range(start,stop):
        if A[j] <= pivotElement:
            i+=1
            swap(A,i,j)
            #temp = A[j]
            #A[j] = A[i]
            #A[i] = temp
    swap(A,i+1,stop)
    #temp1 = A[stop]
    #A[stop] = A[i+1]
    #A[i+1] = temp1
    return i+1    

def partition(A,start,stop):
    i=start-1
    pivotElement=A[stop]
    for j in range(start,stop):
        if A[j] <= pivotElement:
            i+=1
            swap(A,i,j)
            #temp = A[j]
            #A[j] = A[i]
            #A[i] = temp
    swap(A,i+1,stop)
    #temp1 = A[stop]
    #A[stop] = A[i+1]
    #A[i+1] = temp1
    return i+1            
            
    
def quickSort(A,start,stop):
    print start,stop,len(A[start:stop+1])
    if start >=stop:
        #print "1==1"
        #print A[start]
        return
    #p=partition(A,start,stop)
    p=partitionRand(A,start,stop)
    print p
    print A
    #p=rand_partition(A,start,stop)
    quickSort(A,start,p-1)
    #print s1
    quickSort(A,p+1,stop)
    #return s1+[p]+s2

A=[534, 246, 933, 127, 277, 321, 454, 565, 220]
print A
quickSort(A,0,len(A)-1)
print A