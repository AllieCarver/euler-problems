#! -*- coding=utf-8 -*-
"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| 

is minimised; what is the value of D?
"""
from itertools import combinations as comb
import math
import time

def pentagonal(n):
    if ((math.sqrt(float(24*(n)+1))+1)/6)%1==0:
        return True
def problem44():
    set_a=set(n*(3*n-1)/2 for n in xrange(2500) if pentagonal(n*(3*n-1)/2))
    set_b=set_a
    for a in set_a:
        for b in set_b:
            if b>a:
                if pentagonal(abs(b-a)) and pentagonal(a+b):
                    return abs(b-a)
                

time1=time.time()
print problem44()
time2=time.time()
print time2-time1

def problem44b():
    answer=None
    limit=1000
    while not answer:        
        set_a=set(n*(3*n-1)/2 for n in xrange(limit) if pentagonal(n*(3*n-1)/2))
        set_b=set_a
        for a in set_a:
            for b in set_b:
                if b>a:
                    if pentagonal(abs(b-a)) and pentagonal(a+b):
                        answer= abs(b-a)
        limit+=1000
    return answer

time3=time.time()
print problem44b()
time4=time.time()
print time4-time3   

