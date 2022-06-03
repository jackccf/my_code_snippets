import random

def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)

def quickSortNew(aList, reverse=False):
    pass

def quickSortHelper(aList, first, last):
    if first < last:
        pivot_pos = partition(aList, first, last)
        quickSortHelper(aList, first, pivot_pos - 1)
        quickSortHelper(aList, pivot_pos + 1, last)

def partition(aList, first, last):
    pivot_val = aList[first]

    left = first+1
    right = last

    while left <= right:
        while left <= right and aList[left] <= pivot_val:
            left += 1
        while right >= left and aList[right] >= pivot_val:
            right -= 1
        #Swap the two elements to complete the partitioning
        if left < right:
            aList[left],aList[right] = aList[right],aList[left]

    #put the pivot in the proper position
    aList[first],aList[right] = aList[right],aList[first]

    #return the index position of the pivot value
    return right

if __name__ == '__main__':
    aList = []
    for i in range(20):
        aList.append(random.randint(1,100))
    print(aList)
    quickSort(aList)
    print(aList)
