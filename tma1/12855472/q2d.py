# assignment q2d
# purpose: write a program to generate a square pattern with given size
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q2d (comp-s258, 2021Autumn)

# main code starts

sqrSize = int (input ("Enter the size of the pattern: "))

# check the input validity in btw 1 and 20, inclusive.
if sqrSize <= 0 or sqrSize > 20 :
    print ("The entered size should fall between 1 to 20")

# print square pattern
else :
    for r in range (sqrSize) : 
        for c in range (sqrSize) :
            if c == 0 or c == sqrSize -1 :
                print ('$', end='')
            else :
                print ('+', end='')
        print ('')
         

# for the purpose of displaying/seeing executing result
input ()