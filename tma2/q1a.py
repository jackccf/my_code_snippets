# assignment q1a
# purpose: a python program to print a square of user-inputted size with specified pattern
# written by Cheung Chun Fai (s1285547)
# written on 3/29/2021
# For Assignment_02 q1a (comp-s258, 2021Autumn)

size = int(input('Enter size of pattern: '))

# to print the required pattern using for loop
for i in range(size):
    print('$' * (size-i) + '+' * i)

# help to display result after executing the program
input()
