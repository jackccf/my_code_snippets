def sumPos(numlist):
    pass
    # Add your code here


def checkLarger(numlist, check):
    pass
    # Add your code here


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
