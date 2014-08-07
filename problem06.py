#!/usr/bin/env python2
#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 06
========================


The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
	

def problem06():
    return (sum([i for i in xrange(101)]))**2-sum([i*i for i in xrange(101)]) 
    

if __name__=='__main__':
    time1=time.time()
    print problem06()
    time2=time.time()
    print time2-time1
