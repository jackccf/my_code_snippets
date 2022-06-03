# assignment q1g
# purpose: to calculate total price given the number of chicken pieces
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q1g (comp-s258, 2021Autumn)

# main code starts
price = 15
discountPrice = 12
discount = 0.9

chickenPurchased = int (input ("Enter the number of chicken pieces: "))

if chickenPurchased <= 0 :
    print ("Sorry the input is not an integer")
else :
    if chickenPurchased <= 6 :
        totalPrice = price * chickenPurchased
    else :
        totalPrice = (price * 6) + (discountPrice * (chickenPurchased - 6))
        if totalPrice >= 200 :
            totalPrice *= discount
    print ("Amount to pay is", format (totalPrice, '.2f'))

# for the purpose of displaying/seeing executing result
input ()
