#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:39:29 2018

@author: shrinivaass
"""

def recSumFirstN(n):
    if n == 0:
        return 0
    return recSumFirstN(n-1) + n
    
def main():
    x = int(input("Please enter a non-negative integer: "))
    s = recSumFirstN(x)
    print("The sum of the first", x, "integers is", str(s)+".")

if __name__ == "__main__":
    main()
    

    
    