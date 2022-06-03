# Write a program that converts a distance from miles to kilometers. The program should perform the following tasks in the given order.
#  Print a message to ask for a distance in miles.
#  Perform the conversion. (Hint: Distance (in kilometer) = Distance (in miles) * 1.61)
#  Print the result of the conversion to the screen.

def convert (miles):
    return miles * 1.61

miles_in = float(input("distance in miles: "))
print(f"distance in km: {convert(miles_in)}")