#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:57:50 2018

@author: shrinivaass
"""
##Generate all the binary strings with n bits. Assume A[O .. n - 1] is an array of size n

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["O", "1"]
    return [digit+bitstring for digit in bitStrings(1)
                for bitstring in bitStrings(n-1)]
print bitStrings(3)