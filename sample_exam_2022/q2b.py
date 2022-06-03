# Write a complete program that calculates the number of free cans of a soft drink given to customers in a promotion campaign. 
# The number of free cans is calculated from the cans of the soft drink purchased. The details are described below.
#  One (1) free can is given for every 5 cans purchased.
#  Two (2) extra free cans are given if purchasing 20 cans or more.
# For example, if 10 cans are purchased, 2 free cans are given. If 20 cans are purchased, 6 free
# cans are given. The program should read in the number of cans purchased, perform the calculation, and then print the result to the screen.


cans_purchased = int(input("The number of cans purchased: "))

free_5 = cans_purchased // 5
free_20 = cans_purchased // 20 * 2

total = cans_purchased + free_5 + free_20

print("total cans: ", total)
