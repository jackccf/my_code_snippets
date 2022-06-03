# assignment q1b
# purpose: a python program to print a square of user-inputted size with specified pattern
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q1b (comp-s258, 2021Autumn)

size = int(input('Enter size of pattern: '))

# create a function to get the number part of each row of the pattern and store it to a list


def getNum(index, size):
    sizeValue = size
    list = []
    if index == 0:
        list = []
    else:
        for i in range(index):
            sizeValue += i
            if sizeValue >= 10:
                sizeValue %= 10
            list.append(sizeValue)
            sizeValue = size
    return list


# to print the required pattern using for loop
for i in range(size):
    getList = getNum(i, size)
    print('$' * (size-i), *getList, sep='')

# help to display result after executing the program
input()
