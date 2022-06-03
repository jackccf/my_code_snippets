# assignment q1e
# purpose: a python program that reads in 5-day bitcoin rates and gives advice accordingly
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q1e (comp-s258, 2021Autumn)


ratelist = [0] * 5  # create a new list and fill in 5 zeros
highest = lowest = None
average = 0
BENCHMARK = 0.2
advice = ''

# get bitcoin rates from input
for i in range(5):
    bitcoinRate = int(input(f"Enter Bitcoin rate of day {i+1} (USD): "))

    # validate input not to be negative
    while bitcoinRate < 0:
        print("Bitcoin rate cannot be negative, please re-enter: ")
        bitcoinRate = int(input(f"Enter Bitcoin rate of day {i+1} (USD): "))

    # store input into list
    ratelist[i] = bitcoinRate

# caculate the average
average = sum(ratelist)/float(len(ratelist))

# come up with advice accordingly
diff = (ratelist[4] - average) / average
if diff >= 0 and diff < BENCHMARK:
    advice = 'BUY'
elif diff >= BENCHMARK:
    advice = 'SELL'
else:
    advice = 'HOLD'

# print out the results
print('The highest rate is {}'.format(max(ratelist)))
print('The lowest rate is {}'.format(min(ratelist)))
print('The average rate is {}'.format(average))
print(advice)

# help to display result after executing the program
input()
