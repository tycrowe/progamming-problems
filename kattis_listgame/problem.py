"""
DESCRIPTION:
    You are playing the following simple game with a friend:

        The first player picks a positive integer X.

        The second player gives a list of k
        positive integers Y1,…,Yk such that (Y1+1)(Y2+1)⋯(Yk+1)=X, and gets k points.

    Write a program that plays the second player.

INPUT:
    The input consists of a single integer X satisfying 103≤X≤109, giving the number picked by the first player.

OUTPUT:
    Write a single integer k, giving the number of points obtained by the second player,
    assuming she plays as good as possible.

EXAMPLES:
65536           16


127381          3

"""

import sys

for i, line in enumerate(sys.stdin):
    num = i
    print(line) 
    
iter = 0
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def funcy():
    for i in primes:
        if num % i == 0:
            num = num/i
 
while num > 0:
    if num % 2 == 0:
        num = num/2
        iter + 1
    print(iter)
    else:
        while funcy()
            
