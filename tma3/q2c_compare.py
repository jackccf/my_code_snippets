# assignment q2c_compare
# purpose: a python program that compare the running time of 2 sorting functions from q2c.py
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q2c_compare (comp-s258, 2021Autumn)

import random
import timeit

SETUP_QUICKSORT = '''
from q2c import quickSort
from __main__ import bList'''

TEST_QUICKSORT = '''quickSort(bList)'''


SETUP_QUICKSORTNEW = '''
from q2c import quickSortNew
from __main__ import bList'''

TEST_QUICKSORTNEW = '''quickSortNew(bList)'''

for N in (100, 200, 400, 800):

    # GENERATE A RANDOM LIST OF N floating point numbers (range 0 to 10000) in aLsit
    aList = [random.uniform(0, 10000) for i in range(N)]

    bList = aList.copy()  # MAKE A COPY for TESTING
    print("Random order")
    print("Size: ", len(aList))

    # COMPLETE THE IMPLEMENTATION for CALLING timeit
    print('quick sort: ', timeit.timeit(
        setup=SETUP_QUICKSORT, stmt=TEST_QUICKSORT, number=1))
    print('randomized quick sort: ', timeit.timeit(
        setup=SETUP_QUICKSORTNEW, stmt=TEST_QUICKSORTNEW, number=1))

print('\n')  # just for readiblity

for i in (100, 200, 400, 800):

    # GENERATE A  LIST OF reversed sorted N floating point numbers (range 0 to 10000) in aLsit
    aList = [random.uniform(0, 10000) for j in range(i)]
    aList.sort(reverse=True)

    bList = aList.copy()  # MAKE A COPY for TESTING
    print("Reverse order")
    print("Size: ", len(aList))

    # COMPLETE THE IMPLEMENTATION for CALLING timeit
    print('quick sort: ', timeit.timeit(
        setup=SETUP_QUICKSORT, stmt=TEST_QUICKSORT, number=1))

    print('randomized quick sort: ', timeit.timeit(
        setup=SETUP_QUICKSORTNEW, stmt=TEST_QUICKSORTNEW, number=1))
