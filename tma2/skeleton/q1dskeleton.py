import random 

# create a list of 13 zeros 
# stat[1] is the frequency of outcome of 1

# change the code so that the list can collect statistics for 3 dices instead of 2 dices
stat = [0] * 13

for e in range(0, 1000):
    
    # modify the for body to simulate 3 dices (with one cheat) instead of 2 dices
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    outcome = d1 + d2
    stat[outcome] += 1

# Add code here to print the output and bar chart
