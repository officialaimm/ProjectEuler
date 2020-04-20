"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largestPalindromeFromProdOfNDigits(n): 
    palindromes = []
    upper = 10**(n-1)
    lower = 10**n
    for i in range(upper,lower):
        for j in range(upper,lower):
            mul = i*j
            mulStr = str(mul)
            if mulStr==mulStr[::-1]: palindromes.append(mul)
    return max(palindromes)

print(largestPalindromeFromProdOfNDigits(3))