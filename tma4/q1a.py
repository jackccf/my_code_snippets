# tma4 q1a
# purpose: a python program that test performance of three given functions, and then evaluate their scalability based on the empirical result.
# written by Cheung Chun Fai (s1285547)
# On 4/24/2021
# For tma4 q1a (comp-s258, 2021Autumn)

import random
import timeit
import math


def funcA(numlist):
    for i in range(len(numlist)):
        index = i
        for j in range(len(numlist)):
            if numlist[index] > numlist[j]:
                numlist[j], numlist[index] = numlist[index], numlist[j]
            k = math.factorial(500)

def funcB(numlist):
    total = 0
    for i in range(1000):
        for j in range(100):
            total += i**j

def funcC(numlist):
    count, k = 0, 0
    for i in range(len(numlist)):
        j = i
        while j > 0:
            if numlist[i] + numlist[j] == k:
                count += 1
            k = i ** j
            k += math.factorial(500)
            j = j // 2


# set the  setup and stmt parameters for timeit.timeit() funciton
TEST_SETUP = 'from __main__ import funcA, funcB, funcC, list_500, list_1000, list_2000, list_4000'

TEST_FuncA_500 = 'funcA(list_500)'
TEST_FuncA_1000 ='funcA(list_1000)'
TEST_FuncA_2000 ='funcA(list_2000)'
TEST_FuncA_4000 ='funcA(list_4000)'

TEST_FuncB_500 = 'funcB(list_500)'
TEST_FuncB_1000 ='funcB(list_1000)'
TEST_FuncB_2000 ='funcB(list_2000)'
TEST_FuncB_4000 ='funcB(list_4000)'

TEST_FuncC_500 = 'funcC(list_500)'
TEST_FuncC_1000 ='funcC(list_1000)'
TEST_FuncC_2000 ='funcC(list_2000)'
TEST_FuncC_4000 ='funcC(list_4000)'


if __name__ == '__main__':

    # create 4 list of size 500, 1000, 2000 and 4000 with random integers 
    list_500 = [random.randrange(500) for i in range(500)]
    list_1000 = [random.randrange(1000) for i in range(1000)]
    list_2000 = [random.randrange(2000) for i in range(2000)]
    list_4000 = [random.randrange(4000) for i in range(4000)]

    # get and print the processing time of each function with different input size using timeit.timeit()
    print("funcB in size of 500", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncB_500, number=1), 4))
    print("funcB in size of 1000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncB_1000, number=1), 4))
    print("funcB in size of 2000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncB_2000, number=1), 4))
    print("funcB in size of 4000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncB_4000, number=1), 4))

    print("funcC in size of 500", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncC_500, number=1), 4))
    print("funcC in size of 1000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncC_1000, number=1), 4))
    print("funcC in size of 2000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncC_2000, number=1), 4))
    print("funcC in size of 4000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncC_4000, number=1), 4))

    print("funcA in size of 500", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncA_500, number=1), 4))
    print("funcA in size of 1000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncA_1000, number=1), 4))
    print("funcA in size of 2000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncA_2000, number=1), 4))
    print("funcA in size of 4000", round(timeit.timeit(setup=TEST_SETUP, stmt=TEST_FuncA_4000, number=1), 4))
    
 
    # help to display result after executing the program
    input()

    

 
 