"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""


import math

"""
For n=2, Imagine a 2*2 grid.

A------B------C
|      |      |
|      |      |
D------E------F
|      |      |
|      |      |
G------H------I

we need to reach A to I. Now there are several paths to reach there
but one thing is evident that we need to take 2(same as n) down and
2(same as n) right moves regardless. Lets represent the down by D,
and right by R. The possible paths are:
RRDD, RDRD, RDDR, DRDR, DRRD, DDRR
That is there are 4(2*n) places to be filled by 2 items: R and D.
Let's just forget D for a while. 2(n) Rs can be fill 4(2*n) places
and the order does not matter since RR__ and RR__ are same regardless
of which R take place. Thus it is a combination scenario. (Ds will be
forced to just fill the remaining places.)
C(n,r) [where n=2*n and r=n]
= n!/(r!*(n-r)!)
= fact(2n)/(fact(n)*fact(2*n-n))
"""
def pathsToTraverseASquareGrid(n):
	factorial  = math.factorial
	return factorial(2*n)//factorial(n)**2

print(pathsToTraverseASquareGrid(20))