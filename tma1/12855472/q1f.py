# assignment q1f
# purpose: to calculate mango cost for MU students with discount
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q1f (comp-s258, 2021Autumn)

# main code starts
PRICE = 10.50
mangoPurchased = int (input ("Enter the number of super mangos: "))

if mangoPurchased >= 10 :
    mangoPurchased -= 1
totalPrice = PRICE * mangoPurchased

print ("Amount to pay is", format (totalPrice, '.2f'))

# for the purpose of displaying/seeing executing result
input ()