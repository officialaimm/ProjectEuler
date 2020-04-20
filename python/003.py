"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


import math

def largestPrime(num):
    while True:
        smallestPrimeNum = smallestPrime(num)
        if smallestPrimeNum < num:
            num //= smallestPrimeNum
        else:
            return num

def smallestPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:return i
    return num 

print(largestPrime(600851475143))