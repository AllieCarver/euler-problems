# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 00:50:27 2015

@author: killerdigby
"""

import time
from itertools import combinations, permutations
from eulertools import ero_sieve

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

FIRST_1000 = ero_sieve(100000)
FIRST_1000.remove(2)


def problem60():
    prime_sets = []
    for prime_set in combinations(FIRST_1000,5):
        count = 0
        for perm in permutations(prime_set,2):
            if not is_prime(int(str(perm[0]) + str(perm[1]))):
                break
            else:
                count += 1
        #if count == 12:
        if count == 20:
            return sum(prime_set),prime_set
            #prime_sets.append((sum(prime_set),prime_set))
   # return min(prime_sets)

if __name__=='__main__':
    time1=time.time()
    print problem60()
    time2=time.time()
    print time2-time1
"""
x = [0,1,2,3,4]

y = permutations(x,2)
count = 0
for i in y:
    count+=1
    print i
    print count"""

