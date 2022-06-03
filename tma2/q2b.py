# assignment q2b
# purpose: a python program that generate K entries of N numbers each where K,N are user input
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q2b (comp-s258, 2021Autumn)

import random


mark6Pool = list(range(1, 50))  # create list to store all mark6 numbers
lenPool = len(mark6Pool)

# get number of numbers in each entry from input
N = int(input('Enter how many numbers in each entry (N): '))

# validate the number input
while N < 6 or N > 8:
    N = int(input('Enter how many numbers(6 ~ 8) in each entry (N): '))

# get number of entry from input
K = int(input('Enter how many entries (K): '))

# validate the entry input
while K < 1 or K > 6:
    K = int(input('Enter how many(1 ~ 6) entries (K): '))

# create list to store generated numbers and initialize all items to 0
entries = [[0] * N for i in range(K)]

# generate values based on inputted numbers and entries
for i in range(K):
    for e in range(N):
        # pick numbers randomly from the changing pool
        temp = random.randrange(lenPool)
        entries[i][e] = mark6Pool[temp]  # store picked items to entries list
        # remove picked items from original pool
        mark6Pool.remove(entries[i][e])
        # re-assign the changed pool size for next picking
        lenPool = len(mark6Pool)


print(f'The {K} entries generated: ', *entries, sep='\n')

# help to display result after executing the program
input()
