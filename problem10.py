#!/usr/bin/env python2
import math
import time

def check_prime(n):
	for i in xrange(3, int(math.sqrt(n))+1,2):
			if float(n)/i%1==0:
				return False
	else:
		return True
def question10():
	primesum=0
	x=2
	while x<2000000:
		if check_prime(x):
			primesum+=x
		if x==2:
			x+=1
		elif x >= 3:
			x+=2
	print primesum
time3=time.time()
question10()		
time4=time.time()
print time4-time3
def ero_sieve(n):
    primes=set(i for i in xrange(3,n+1,2))
    for i in set(primes):
        j=2
        while i*j<n:
            primes.discard(i*j)
            j+=1 
    primes.add(2)
    return primes

time1=time.time()    
print sum(ero_sieve(2000000))
time2=time.time()
print time2-time1
