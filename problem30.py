#!-*-coding=utf8 -*-

import time

"""
========================
Project Euler Problem 30
========================
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
 
def problem30():
    total=0
    fifth_powers={}
    for i in xrange(10):
        fifth_powers[str(i)]=i**5
    upper_limit=10000
    while True:    
        current_total=0    
        for n in xrange(2,upper_limit):
            if sum([fifth_powers[i] for i in str(n)])==n:
                current_total+=n
            
        if current_total == total:
            return total
        else:
            total = current_total
            upper_limit *= 10

if __name__=='__main__':
    time1=time.time()
    print problem30()
    time2=time.time()
    print time2-time1	
