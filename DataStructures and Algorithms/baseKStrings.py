#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:31:50 2018

@author: shrinivaass
"""

##Generate all the strings of length n drawn from 0 ... k - 1.

def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result
    
def baseKStrings(n,k):
    if n == 0 : return []
    if n == 1: return rangeToList(k)
    return [digit+bitstring for digit in baseKStrings(1 ,k)
            for bitstring in baseKStrings(n-1,k)]

print baseKStrings(3,3)
