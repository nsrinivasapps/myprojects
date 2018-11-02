#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:02:49 2018

@author: shrinivaass
"""

def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def insertionSort(A):
    for i in range(len(A)):
        print i,A[i]
        for j in range(i,0,-1):
            if A[j] < A[j-1]:
                swap(A,j,j-1)
        print A
                
A = [534,246,933,127,277,321,454,565,220]

B = [6,8,1,4,5,3,7,2]

insertionSort(B) 


#print A 

#6 8 l 4 5 3 7 2 (Consider index 0)
#6 8 I 4 5 3 7 2 (Consider indices 0 - I )
#1 6 8 4 5 3 7 2 (Consider incl ice~ 0 - 2: inscrLion plt1ccs l in front of 6 and 8)
#1 4 6 8 5 3 7 2 (Process some as above is rcpcutcd until urruy is sorted)
#14568 372
#1345678 2
#1 2 3 4 5 6 7 8 (The array is sorted!)              
                