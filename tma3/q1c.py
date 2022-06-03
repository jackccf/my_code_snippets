# assignment q1c
# purpose: a python program that accepts a password (as a string) as a parameter
#           and returns True if it is a lucky password, and False if otherwise based on given rules
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q1c (comp-s258, 2021Autumn)


def isLuckySeven(pwd):
    pwdToList = list(pwd)   # convert pwd of string to list
    uppercaseList = []
    for i in range(65, 91):
        # create a list to contain uppercase characters
        uppercaseList.append(chr(i))

    # create a list to contain lowercase characters
    lowercaseList = list(map(lambda x: x.lower(), uppercaseList))
    digitList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '0',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9']   # create list to contain digits and it's string form
    # create a list to contain valid punctuation
    punctuationList = ['+', '-', '*', '/']
    luckyList = uppercaseList + lowercaseList + digitList + \
        punctuationList  # create a list to contain all lucky characters
    countPunc = 0
    countDigit = 0

    if len(pwdToList) < 8 or len(pwdToList) > 32:
        return False    # return False if length of pwd is not valid

    elif "77" not in pwd:
        return False     # return False if '77' is not in pwd

    else:
        for i in pwdToList:
            if i not in luckyList:
                return False    # return false if pwd contains any non-lucky character
            if i in punctuationList:
                countPunc += 1
            if i in digitList:
                countDigit += 1
        if countDigit < 1:
            return False    # return false if pwd has no digits at all
        elif countPunc > 1:
            return False    # return false if pwd has more than one punctuation
        else:
            return True  # return true to represent a lucky pwd


# TEST CODE
testcases1 = ['ABCDEF', 'ABCDEFGH', 'ABCDabcd', 'ABCD ']
testcases2 = ['ABCDef77@', 'ABCDef77+']

for t in testcases1:
    t = str(t)
    print(isLuckySeven(t))

for t in testcases2:
    t = str(t)
    print(isLuckySeven(t))

# help to display result after executing the program
input()
