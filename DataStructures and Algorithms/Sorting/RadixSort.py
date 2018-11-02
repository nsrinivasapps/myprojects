#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:16:20 2018

@author: shrinivaass
"""

def radixSort(A):
    RADIX = 10
    placement = 1    
    #print buckets
    maxlength = False
    while not maxlength:
        maxlength = True
        buckets = [list() for _ in range(RADIX)]
        for i in A:
           tmp = i / placement
           buckets[tmp%RADIX].append(i)
           if maxlength and tmp > 0:
               maxlength = False
        a=0
        print buckets
        for b in range(RADIX):
            print "b",buckets[b]
            for i in buckets[b]:
                A[a] = i
                a+=1
        print "a",A               
        placement = placement *  RADIX               
                
        
    

A=[534, 246, 933, 127, 277, 321, 454, 565, 220]
#print A
radixSort(A)    