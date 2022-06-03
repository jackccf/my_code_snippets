# Write a program that should read in an integer (size) and then print a square of the given size and of a pattern 
# shown in the following examples. The examples below show two executions of the same program. The first example 
# shows a pattern of size 5 and the second example shows one of size 8.

# Enter size: 5
# *****
# *   *
# *   *
# *   *
# *****
# Enter size: 8
# ********
# *      *
# *      *
# *      *
# *      *
# *      *
# *      *
# ********

size = int(input("Enter size: "))

for i in range(size):   # i=row, j=col
    for j in range(size):
        if i == 0 or i == size-1:
            if j == size - 1:
                print("*")
            else:
                print("*", end="")

        else:
            if j == 0:
                print("*", end="")
            elif j == size - 1:
                print("*")
            else:
                print(" ", end="")