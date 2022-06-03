# assignment q1a
# purpose: a python program that generates and returns a list of given and asserted number of random integers
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q1a (comp-s258, 2021Autumn)


import random


def genRanList(N):
    randList = []   # create an empty list
    assert N > 0    # assert N must greater than 0
    for i in range(N):
        # append generated random number to list
        randList.append(random.randrange(1, 50))
    return randList


# print(genRanList(-1))  # Test N > 0 Assert
# print(genRanList(0))  # Test N > 0 Assert
print(genRanList(10))

# help to display result after executing the program
input()
