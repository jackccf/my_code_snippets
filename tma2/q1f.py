# assignment q1f
# purpose: write and test 2 functions having list as parameters
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q1f (comp-s258, 2021Autumn)


# function to return the sum of positive numbers in a list

def sumPos(numlist):
    countPos = 0
    sum = 0

    for i in numlist:
        if i > 0:
            countPos += 1   # count the number of positive number
            sum += i    # calculate sum of positive number

    if countPos == 0:
        return None  # return None if no positive number
    else:
        return sum  # return sum


# function to return True if any number in parameter list 'check"
# is larger than any number in paramerter list 'numlist'


def checkLarger(numlist, check):
    if max(check) > max(numlist):
        return True
    else:
        return False


print(sumPos([1, 2, 3, 4, 5]))
print(sumPos([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5]))
print(sumPos([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 0]))
print(sumPos([]))

numlist = [1, 9, 6, 3, 4, 6, 2, 4]
print(checkLarger(numlist, [0, 0, 0]))  # False
print(checkLarger(numlist, [9, 0, 0]))  # False
print(checkLarger(numlist, [0, 0, 9]))  # False
print(checkLarger(numlist, [0, 9, 0]))  # False
print(checkLarger(numlist, [10, 0, 0]))  # True
print(checkLarger(numlist, [0, 0, 10]))  # True
print(checkLarger(numlist, [0, 10, 0]))  # True
