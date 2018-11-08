#!/usr/bin/python3.6
from math import sqrt, ceil
import sys

N = int(sys.argv[1])

factors = []

def is_prime(n):
     if n == 2 or n == 3:
         return True
     if n % 2 == 0 or n % 3 == 0:
         return False
     i = 5
     w = 2
     while i**2 <= n:
         if n % i == 0:
            return False
         i += w
         w = 6 - w

     return True

def all_prime(x):
    for i in x:
        if not is_prime(i):
            return False
    return True

def is_square(n):
    return sqrt(n).is_integer()

def fermat_factor(n):
    if is_prime(n):
        factors.append(n)
        return
    if n % 2 == 0:
        factors.append(2)
        factors.append(n//2)
        return
    a = ceil(sqrt(n))
    b2 = a**2 - n
    while not is_square(b2):
        a += 1
        b2 = a**2 - n
    p = int( a - sqrt(b2) )
    q = int( a + sqrt(b2) )
    factors.append(p)
    factors.append(q)
    return

fermat_factor(N) # first pass

while not all_prime(factors):
    for i in factors:
        if not is_prime(i):
            factors.remove(i)
            fermat_factor(i)

print(' * '.join(str(x) for x in factors))
