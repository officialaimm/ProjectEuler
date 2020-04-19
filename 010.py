"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math

def isPrime(num):
    if num>2:
        return all(num%i for i in range(2,int(math.sqrt(num))+1))
    return num==2

sumOfPrimesBelow = lambda n:sum([i*isPrime(i) for i in range(n)])

print(sumOfPrimesBelow(2000000))