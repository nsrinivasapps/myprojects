#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:45:54 2018

@author: shrinivaass
"""

def isSortedOrder(arr):
    if len(arr)==1:
        return True
    return arr[0]<=arr[1] and isSortedOrder(arr[1:])

A= [1127, 220, 246, 277, 321, 454, 534, 565, 9331]
print isSortedOrder(A)

A= [220, 246, 277, 321, 454, 534,565,1127, 9331]
print isSortedOrder(A)