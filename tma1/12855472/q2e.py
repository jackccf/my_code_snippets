# assignment q2e
# purpose: to generates a square pattern of a different pattern
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q2e (comp-s258, 2021Autumn)

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
                if c >= 10 :
                    print (c-10, end='')
                else :
                    print (c, end='')
        print ('')
         

# for the purpose of displaying/seeing executing result
input ()