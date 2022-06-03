# Complete the following function that returns True if all numbers in a list between the starting index (in parameter startindex) 
# and the ending index (in parameter endindex) are all negative (below zero). It returns False if otherwise. Both indices are inclusive, 
# that is, the numbers to check include the startindex and the endindex.

# def isNegative(numlist, startindex = 0, endindex = None):

# Notes
# • The list is given in the parameter numlist
# • The parameter startindex has a default value 0. If this parameter is not given, then the range of checking starts from the first number in the list. 
# Assume that this parameter is valid.
# • The parameter endindex has a default value None. If this parameter is not given or is larger than the end of the list, then the range of checking 
# ends at the end of the list.
# • The function should return None if endindex is smaller than startindex.

def isNegative(numList, startIndex = 0, endIndex = None):
    if endIndex == None or endIndex > len(numList) or endIndex < startIndex:
        endIndex = len(numList)
    for i in range(startIndex-0, endIndex):
        if numList[i] >= 0:
            return False
    return True

if __name__ == "__main__":
    aList = [j for j in range(-5, 5)]
    print(aList)
    print(isNegative(aList, endIndex=-1))