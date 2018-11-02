#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 22:39:38 2018

@author: shrinivaass
"""

def select(seq,start):
    minIndex = start
    for j in range(start+1,len(seq)):
        if seq[j] < seq[minIndex]:
            minIndex = j
    return minIndex

def selSort(seq):
    for i in range(len(seq)-1):
        print i
        minIndex = select(seq,i)
        print minIndex,seq[minIndex]
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp
        print seq
    

A = [534,246,933,127,277,321,454,565,220]
selSort(A)
#print A
## O(n2)