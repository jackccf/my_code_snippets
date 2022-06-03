# tma4 q1c
# purpose: a python program that reads in data from a csv file and print findings based on requirement.
# written by Cheung Chun Fai (s1285547)
# On 4/24/2021
# For tma4 q1c (comp-s258, 2021Autumn)

import sys, os
from csv import DictReader 

os.chdir(r'D:\HKMU\2021Autumn - s258\s258_assignments\assignment_04')

# validate input and handle IOError
fname = input('Enter CSV filename (Enter to quit): ')
while True:
    if fname == "":
        exit(2)

    try:
        # fname = 'EnglishLeagueAllTime.csv'
        in_csv = DictReader(open(fname, 'r', encoding="utf-8-sig"))  

    except IOError as err:
        # print(err)
        fname = input('Enter CSV filename (Enter to quit): ')
    
    else: 
        break

# convert read file to list and sort reversely by Points 
lis_csv = list(in_csv)
lis_csv.sort(key=lambda i:int(i["Points"]), reverse=True)

# find and print result of c1
print("top 5 teams with the highest points: ")
count_line = 0
for row in lis_csv:
    if count_line < 5:
        print(row["Team"], row["Points"])
        count_line += 1
    else:
        break

# find and print result of c2
print("The number of teams with name containing 'United' and won fewer than 500 games: ")
count_c2 = 0
for row in lis_csv:
    if ("United" in row["Team"]) and (int(row["Win"]) < 500) :
        count_c2 += 1
print(count_c2)

# find and print result of c3
print("The number of teams that have played over 2000 games and scored over 5000 goals: ")
count_c3 = 0
for row in lis_csv:
    if (int(row["Play"])>2000) and (int(row["For"]) > 5000) :
        count_c3 += 1
print(count_c3)


# help to display result after executing the program
input()



