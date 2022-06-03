# assignment q1h
# purpose: to calculate the cost of name cards
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q1h (comp-s258, 2021Autumn)

# main code starts

# create list of given papertype and color
paperTypeList = ['A', 'B', 'C', 'a', 'b', 'c']
colourList = [1, 2, 4]

# create price for each combination
typeA1 = 140.0
typeA2 = 180.0
typeA4 = 250.0

typeB1 = 100.0
typeB2 = 120.0
typeB4 = 160.0

typeC1 = 80.0
typeC2 = 90.0
typeC4 = 120.0

print ("MU Name Cards")

# get input from user
paperType = input ("Enter the required paper type (A, B, C): ")
numberOfColours = int (input ("Enter number of colors (1, 2, 4): "))
numberOfLots = int (input ("Enter number of lots of 500: "))

# calculate the price in terms of inputed data
if paperType not in paperTypeList or numberOfColours not in colourList or numberOfLots <= 0 :
    print ("Error in the input")
else :
    if paperType == 'A' or paperType == 'a' :
        if numberOfColours == 1 :
            totalPrice = typeA1 * numberOfLots
        elif numberOfColours == 2 :
            totalPrice = typeA2 * numberOfLots
        else :
            totalPrice = typeA4 * numberOfLots
    elif paperType == 'B' or paperType == 'b' :
        if numberOfColours == 1 :
            totalPrice = typeB1 * numberOfLots
        elif numberOfColours == 2 :
            totalPrice = typeB2 * numberOfLots
        else :
            totalPrice = typeB4 * numberOfLots
    else :
        if numberOfColours == 1 :
            totalPrice = typeC1 * numberOfLots
        elif numberOfColours == 2 :
            totalPrice = typeC2 * numberOfLots
        else :
            totalPrice = typeC4 * numberOfLots

    print ("The amount to pay is $", int(totalPrice), sep='')

# for the purpose of displaying/seeing executing result
input ()