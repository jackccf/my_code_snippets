# assignment q1d
# purpose: a python program that analyze a file and finds and displays the team with highest winning rate.
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q1d (comp-s258, 2021Autumn)


import os

# change cwd to where csv file is located
os.chdir(r'D:\# myKits\_indiv\hkmu\2021Autumn - s258\s258_assignments\assignment_03')


highestName = highestWinrate = 0
countLine = 0
linesList, contentList = [], []

try:    # try to handle exception
    infile = open('EPLTeams.csv', 'r')  # open file in read mode

    lines = infile.readlines()  # read file and store it as a list of strings

    infile.close()

    for i in lines:
        # convert each string content in lines seperated by comma further to a list of items
        linesList.append(i.split(','))

    for i in linesList:  # linesList is a 2D list wi
        for e in i:
            # store all item in 2D list linesList to a single 1-dimension list contentList
            contentList.append(e)

    for i in range(len(contentList)):
        if i < 3 or i % 3 != 0:  # omit first line items
            pass
        else:
            teamName = contentList[i]
            winRate = float(contentList[i+2]) / int(contentList[i+1])
            if winRate > highestWinrate:
                highestWinrate = winRate    # find the highest winrate
                highestName = teamName  # find the team has highest winrate

    # print out the result
    print(f'{highestName} has the highest winrate of {highestWinrate:.3f}!')
    print('Analysis finished')

except Exception as err:    # handle exception
    print('IO Error')

# help to display result after executing the program
input()
