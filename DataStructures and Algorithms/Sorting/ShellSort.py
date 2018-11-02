#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:03:44 2018

@author: shrinivaass
"""
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp
    
def shellSort(A):
    gap = len(A)//2
    while gap >= 1:
        print gap
        for i in range(len(A)):
            if i+gap < len(A):
                if A[i] > A[i+gap]:
                    swap(A,i,i+gap)
                print A            
        gap = gap//2


A = [534,246,933,127,277,321,454,565,220]
print A
B=[12,34,54,2,3]
shellSort(A)                
#print A

'''
def shellSort(A):
    n = len(A)
    gap = n//2
    while gap >= 1:
        print gap
        for i in range(gap,n):
            j = i
            temp = A[i]
            while j >= gap and A[j-gap]  > temp:
                A[j] = A[j-gap]
                j-=gap
            A[j] = temp
        
            #if i+gap < len(A):
             #   if A[i] > A[i+gap]:
              #      swap(A,i,i+gap)
            print A            
        gap = gap//2


A = [534,246,933,127,277,321,454,565,220]
print A
B=[12,34,54,2,3]
shellSort(A)                
#print A
'''