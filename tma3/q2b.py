# assignment q2b
# purpose: a python program that prints a series of fibonacci numbers specified by input value
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q2b (comp-s258, 2021Autumn)

import timeit
import sys
from functools import lru_cache


# cache called results of Fib(N) function (for q2b-ii question)
@lru_cache
def Fib(N):
    assert N >= 1
    if N == 1 or N == 2:
        return 1
    return Fib(N-1) + Fib(N-2)


if __name__ == '__main__':
    # change system recursion limit to cache more
    print(sys.setrecursionlimit(2000))
    A = int(input('Enter the start of the series (A): '))
    B = int(input('Enter the end of the series (B): '))

    for i in range(A, B+1):
        print(f'{i:<5d} {Fib(i):<5d}', sep='\n')
