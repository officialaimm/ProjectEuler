"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def longestCollatzChainUnder(n):
    collatzDict = {}
    for i in range(1,n):
        current=i
        length = 0
        while current>1:
            if current in collatzDict:
                length += collatzDict[current]
                break
            if current%2: current=3*current+1
            else: current=current//2
            length+=1
        collatzDict[i] = length
    return max(collatzDict,key=collatzDict.get)

print(longestCollatzChainUnder(1000000))