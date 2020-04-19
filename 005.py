"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


import math

def smallEvenlyDivisible(upto):
    num = 1
    for i in range(2,upto+1):
        num *= i//math.gcd(i,num)
    return num

print(smallEvenlyDivisible(20))