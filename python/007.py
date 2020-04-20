"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


import math

def isPrime(num):
    if num>2:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:return False
        return True
    return num==2

def nthPrime(n):
    num = 1
    primes = 0
    while True:
        if(isPrime(num)):
            primes+=1
            if primes==n:break
        num+=1
    return num

print(nthPrime(10001))