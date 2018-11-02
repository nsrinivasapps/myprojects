#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:44:46 2018

@author: shrinivaass
"""
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def bubbleSort(A):
    if len(A) == 0:
        return
    swapped='N'
    for i in range(len(A)):
        print i
        if swapped == 'N' and i > 0:
            return
        swapped ='N'
        for j in range(len(A)-1):
            if A[j+1] < A[j]:
                swap(A,j+1,j)
                swapped ='Y'
            print A                
                
                


A = [534,246,933,127,277,321,454,565,220]

bubbleSort(A)
#print A
                