#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:45:05 2018

@author: shrinivaass
"""
def merge(lefthalf,righthalf):
    i=0
    j=0
    sortedlist = []
    while i < len(lefthalf) and j <  len(righthalf):
        if lefthalf[i] < righthalf[j]:
            sortedlist.append(lefthalf[i])
            i+=1
        else:
            sortedlist.append(righthalf[j])
            j+=1
            
    while i < len(lefthalf):
        sortedlist.append(lefthalf[i])
        i+=1
        
    while j < len(righthalf):
        sortedlist.append(righthalf[j]) 
        j+=1
    #print sortedlist
    return sortedlist
        
    #for i in range(len(sortedlist)):
     #   A[start+i] = sortedlist[i]
    
    
    
def mergeSort(A):
    n=len(A)
    mid = n//2 
    #print n,mid    
    if len(A) == 1:
        return A

    lefthalf = mergeSort(A[0:mid])
    righthalf  =  mergeSort(A[mid:n])
    
    return merge(lefthalf,righthalf)

#def mergeSort(A):
 #   return mergeSortRecursive(A,0,len(A)-1)

A=[534, 246, 933, 127, 277, 321, 454, 565, 220]
print mergeSort(A)

    