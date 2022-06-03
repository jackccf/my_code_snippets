# assignment q1e
# purpose: to calculate price of made-to-measure seed block in terms of length, width and height inputed
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q1e (comp-s258, 2021Autumn)

# main code starts
PRICE = 550000

print ("Made-to-measure seed block")
length = float (input ("Enter the length (m): "))
width = float (input ("Enter the width (m): "))
height = float (input ("Enter the height (m): "))

totalPrice = PRICE * (length * width * height)

print ("The price is $", format(totalPrice, '.2f'), sep='')

# for the purpose of displaying/seeing executing result
input ()