#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:31:47 2018

@author: shrinivaass
"""

def TowersOfHanoi(numberOfDisks, startPeg= 1, endPeg=3):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg)
        print "Move:: disk %d from peg %d to peg %d" % (numberOfDisks, startPeg, endPeg)
        TowersOfHanoi(numberOfDisks-1, 6-startPeg-endPeg, endPeg)

#TowersOfHanoi(numberOfDisks=4)



def TowersOfHanoi1(numberOfDisks, startPeg= 1,auxpeg =2, endPeg=3):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks-1, startPeg, auxpeg)
        print "Move:: disk %d from peg %d to peg %d" % (numberOfDisks, startPeg, endPeg)
        TowersOfHanoi(numberOfDisks-1,auxpeg, endPeg)

TowersOfHanoi1(numberOfDisks=4)