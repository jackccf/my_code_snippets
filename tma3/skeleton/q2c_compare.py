import random
import timeit

SETUP_QUICKSORT = '''
from q2c import quickSort
from __main__ import bList'''
      
TEST_QUICKSORT = '''quickSort(bList)'''

for N in (100,200,400,800): 
    
    aList = []
    # GENERATE A RANDOM LIST OF N floating point numbers (range 0 to 10000) in aLsit

    bList = aList.copy() # MAKE A COPY for TESTING
    print("Random order")
    print("Size: ", len(aList))
    # COMPLETE THE IMPLEMENTATION for CALLING timeit


for i in (100,200,400,800):

    aList = []
    # GENERATE A  LIST OF reversed sorted N floating point numbers (range 0 to 10000) in aLsit
    bList = aList.copy() # MAKE A COPY for TESTING
    print("Reverse order")
    print("Size: ", len(aList))
    # COMPLETE THE IMPLEMENTATION for CALLING timeit    