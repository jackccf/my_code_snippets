# assignment q2a
# purpose: a python function that returns 'True" for good name or 'False' for bad name based on given rules
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q2a (comp-s258, 2021Autumn)

def isGoodFortune(name):
    evilLetters = ('E', 'V', 'I', 'L', 'e', 'v', 'i', 'l')
    badLetters = ('B', 'A', 'D', 'b', 'a', 'd')

    countEvil = 0
    countBad = 0
    countEmpty = 0

    if not isinstance(name, str):   # if input is not string, return None
        return None
    else:
        nameList = list(name)   # convert string to list type
        lenName = len(nameList)

        for i in nameList:
            if i in evilLetters:    # count number of evil and bad letters at the name
                countEvil += 1
                countBad += 1
            elif i in badLetters:   # further count number of bad letters
                countBad += 1
            elif i == ' ':  # count the space letter
                countEmpty += 1

        countGood = lenName - countBad - countEmpty  # count number of good letters

        if countEvil > 0:   # return False if any evil letters exist
            return False
        elif countGood - countBad <= 0:  # return False if good letters is less or equal than bad letters
            return False
        else:   # return True otherwise
            return True


# dummy checking statements
print(isGoodFortune(None))
print(isGoodFortune(""))
print(isGoodFortune("GG"))
print(isGoodFortune("GGE"))
# print(isGoodFortune("bad good good good e "))

# help to display result after executing the program
input()
