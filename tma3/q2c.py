# assignment q2c
# purpose: a python program that implements two sorting functions, quickSort and quickSortNew
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q2c (comp-s258, 2021Autumn)


import random


def quickSort(aList):
    quickSortHelper(aList, 0, len(aList)-1)


def quickSortNew(aList, reverse=False):
    # select a random value as the pivot
    pivot_rand = random.randrange(len(aList))
    if pivot_rand != 0:
        # swap the random item with the first item
        aList[0], aList[pivot_rand] = aList[pivot_rand], aList[0]

    if reverse:  # for decending sort
        quickSortHelper(aList, 0, len(aList)-1, reverse=True)

    else:   # for acending sort
        quickSort(aList)


def quickSortHelper(aList, first, last, reverse=False):
    if first < last:
        if reverse:  # for decending sort
            pivot_pos = partition(aList, first, last, reverse)
            quickSortHelper(aList, first, pivot_pos - 1, reverse)
            quickSortHelper(aList, pivot_pos + 1, last, reverse)
        else:   # for acending sort
            pivot_pos = partition(aList, first, last)
            quickSortHelper(aList, first, pivot_pos - 1)
            quickSortHelper(aList, pivot_pos + 1, last)


def partition(aList, first, last, reverse=False):

    pivot_val = aList[first]    # select the swapped random item as pivot

    left = first+1
    right = last

    while left <= right:
        if reverse:
            while left <= right and aList[left] >= pivot_val:
                left += 1
            while right >= left and aList[right] <= pivot_val:
                right -= 1
            # Swap the two elements to complete the partitioning
            if left < right:
                aList[left], aList[right] = aList[right], aList[left]
        else:
            while left <= right and aList[left] <= pivot_val:
                left += 1
            while right >= left and aList[right] >= pivot_val:
                right -= 1
            # Swap the two elements to complete the partitioning
            if left < right:
                aList[left], aList[right] = aList[right], aList[left]

    # put the pivot in the proper position
    aList[first], aList[right] = aList[right], aList[first]

    # return the index position of the pivot value
    return right


if __name__ == '__main__':
    aList = []
    for i in range(20):
        aList.append(random.randint(1, 100))

    print(aList)    # print original list
    quickSort(aList)  # test acending-sorted list
    print(aList)
    quickSortNew(aList, True)  # test decending-sorted list
    print(aList)

    # help to display result after executing the program
    input()
