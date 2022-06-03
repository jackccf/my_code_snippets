# assignment q2a
# purpose: a python program that have a recursive function returns the value of pi**2 given a certain N as parameter
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q2a (comp-s258, 2021Autumn)

import math
import sys


def find_pi_square(N):
    try:    # check if or not N is a integer
        N = int(N)
        if N <= 500 and N > 0:  # check if or not N is a positive integer <= 500
            if N == 1:  # base case for N == 1
                return 1 * 8
            elif N == 2:  # base case for N == 2
                return (1 + 1 / 3 ** 2) * 8
            elif N == 3:  # base case for N == 3
                return (1 + 1 / 3 ** 2 + 1 / 5 ** 2) * 8
            elif N == 4:  # base case for N == 4
                return (1 + (1 / 3 ** 2) + (1 / 5 ** 2) + (1 / 7 ** 2)) * 8
            else:
                last_item = (1 / (N * 2 - 1) ** 2) * 8
                result = last_item + find_pi_square(N - 1)  # general case
            return result
        else:
            return -1   # returns -1 if N is not a positive integer <= 500
    except Exception as err:
        return -1   # returns -1 if N is not a integer


if __name__ == '__main__':
    # change parameter N of "find_pi_square(N)" below to test the program
    pi_square = find_pi_square(500)
    try:
        pi = math.sqrt(pi_square)
        print(f'PI is found to be {pi}')
    except:
        print('N should be a positive integer <= 500')

    # help to display result after executing the program
    input()
