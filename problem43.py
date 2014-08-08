#! -*- utf-8 -*-
from itertools import permutations as perm
import time

"""
========================
Project Euler Problem 43
========================
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 

but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def problem43():

    nums=set(int(''.join(i)) for i in perm("0987654321")if i[5]=='5' and int(''.join(i[1:4]))%2==0 and int(''.join(i[7:]))%17==0
        and int(''.join(i[6:9]))%13==0 and int(''.join(i[5:8]))%11==0 and int(''.join(i[4:7]))%7==0 
        and int(''.join(i[2:5]))%3==0)
           
    return sum(nums)  

if __name__=='__main__':
    time1=time.time()
    print problem43()
    time2=time.time()
    print time2-time1	
