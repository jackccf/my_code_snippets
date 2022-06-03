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

if __name__ == '__main__':
    pass
    # ADD YOUR CODE HERE TO FIND THE TIME TAKEN FOR RUNNING THE FUNCTIONS
 
 