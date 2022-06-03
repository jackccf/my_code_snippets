# assignment q1d
# purpose: a python program that collects statistics of 1000 3-dice rolling with one detect dice and print the frequency and corresponding graph
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q1d (comp-s258, 2021Autumn)


import random


# create a list of 19 zeros (the first 3) to represent all possible number of outcomes of 3-dice rolling
# 16 outcomes in total, the first 3 item in the list will be left unused
stat = [0] * 19

# roll 3 dices 1000 times
for e in range(0, 1000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 5)

    # caculate the outcome
    outcome = d1 + d2 + d3

    # count frequency of each outcome
    stat[outcome] += 1

    # reset the outcome for next rolling
    outcome = 0

# print the title
print('{:>2} {:>5}'.format('sum', 'freq'), end='\n')

# print stats
for i in range(len(stat)):
    if i >= 0 and i < 3:
        continue
    else:
        print('{:>2} {:>6} {:<}'.format(
            i, stat[i], '*' * int(stat[i]/10)), end='\n')

# help to display result after executing the program
input()
