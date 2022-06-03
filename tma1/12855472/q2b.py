# assignment q2b
# purpose: to calculate number of months to reach targeted amount 
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q2b (comp-s258, 2021Autumn)

# main code starts
currentAmount = 10000.0
increase = 1.15
counterOfMonth = 0

targetAmount = float (input ("Enter target ($): "))

while currentAmount < targetAmount :
    currentAmount *= increase
    counterOfMonth += 1
    print ("After", counterOfMonth, "months saving is", currentAmount)

print ("Reached $", targetAmount, " after ", counterOfMonth, " months", sep="" )

# for the purpose of displaying/seeing executing result
input ()

